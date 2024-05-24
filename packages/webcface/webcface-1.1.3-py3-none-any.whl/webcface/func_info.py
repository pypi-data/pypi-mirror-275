from __future__ import annotations
from typing import Callable, Optional, List
from enum import IntEnum
from copy import deepcopy
import inspect
import threading
import logging
import webcface.field
import webcface.member


class ValType(IntEnum):
    NONE = 0
    STRING = 1
    STR = 1
    BOOL = 2
    INT = 3
    FLOAT = 4


def get_type_enum(t: type) -> int:
    if t == int:
        return ValType.INT
    if t == float:
        return ValType.FLOAT
    if t == bool:
        return ValType.BOOL
    if t == str:
        return ValType.STRING
    if (
        t == inspect.Parameter.empty
        or t == inspect.Signature.empty
        or t == type(None)
        or t is None
    ):
        return ValType.NONE
    return ValType.STRING


class Arg:
    _name: str
    _type: int
    _min: Optional[float]
    _max: Optional[float]
    _init: Optional[float | bool | str]
    _option: List[float | str]

    def __init__(
        self,
        name: str = "",
        type: int | type = ValType.NONE,
        min: Optional[float] = None,
        max: Optional[float] = None,
        init: Optional[float | bool | str] = None,
        option: List[float | str] = [],
    ) -> None:
        self._name = name
        if isinstance(type, int):
            self._type = type
        else:
            self._type = get_type_enum(type)
        self._min = min
        self._max = max
        self._init = init
        self._option = deepcopy(option)

    def merge_config(self, a: Arg) -> Arg:
        if a._name != "":
            self._name = a._name
        if a._type != ValType.NONE:
            self._type = a._type
        if a._init is not None:
            self._init = a._init
        if a._max is not None:
            self._max = a._max
        if a._min is not None:
            self._min = a._min
        if len(a._option) > 0:
            self._option = a._option
        return self

    def __repr__(self) -> str:
        s = f"name={repr(self._name)}, type={repr(self._type)}"
        if self._min is not None:
            s += f", min={repr(self._min)}"
        if self._max is not None:
            s += f", max={repr(self._max)}"
        if self._init is not None:
            s += f", init={repr(self._init)}"
        if len(self._option) > 0:
            s += f", option={repr(self._option)}"
        return "Arg(" + s + ")"

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> int:
        return self._type

    @property
    def init(self) -> Optional[float | bool | str]:
        return self._init

    @property
    def max(self) -> Optional[float]:
        return self._max

    @property
    def min(self) -> Optional[float]:
        return self._min

    @property
    def option(self) -> List[float | str]:
        return self._option


class FuncInfo:
    return_type: int
    args: List[Arg]
    hidden: bool
    func_impl: Optional[Callable]

    def __init__(
        self,
        func: Optional[Callable],
        return_type: Optional[int | type],
        args: Optional[List[Arg]],
        hidden: Optional[bool]
    ) -> None:
        self.func_impl = func
        self.hidden = hidden is True
        if args is None:
            self.args = []
        else:
            self.args = deepcopy(args)
        if func is None:
            sig = None
        else:
            sig = inspect.signature(func)
            for i, pname in enumerate(sig.parameters):
                p = sig.parameters[pname]
                if p.default != inspect.Parameter.empty:
                    init = p.default
                else:
                    init = None
                auto_arg = Arg(name=pname, type=p.annotation, init=init)
                if i < len(self.args):
                    self.args[i] = auto_arg.merge_config(self.args[i])
                else:
                    self.args.append(auto_arg)
        if isinstance(return_type, int):
            self.return_type = return_type
        elif isinstance(return_type, type):
            self.return_type = get_type_enum(return_type)
        elif sig is not None:
            self.return_type = get_type_enum(sig.return_annotation)
        else:
            raise ValueError()

    def run(self, args) -> float | bool | str:
        if len(args) != len(self.args):
            raise TypeError(f"requires {len(self.args)} arguments but got {len(args)}")
        new_args: List[int | float | bool | str] = []
        for i, a in enumerate(args):
            if self.args[i].type == ValType.INT:
                new_args.append(int(float(a)))
            elif self.args[i].type == ValType.FLOAT:
                new_args.append(float(a))
            elif self.args[i].type == ValType.BOOL:
                new_args.append(bool(a))
            elif self.args[i].type == ValType.STRING:
                new_args.append(str(a))
            else:
                new_args.append(a)
        ret = None
        if self.func_impl is not None:
            ret = self.func_impl(*new_args)
        if ret is None:
            ret = ""
        return ret


class FuncNotFoundError(RuntimeError):
    def __init__(self, base: webcface.field.FieldBase) -> None:
        super().__init__(f'member("{base._member}").func("{base._field}") is not set')


class AsyncFuncResult:
    """非同期で実行した関数の実行結果を表す。"""
    _caller_id: int
    _caller: str
    _started: bool
    _started_ready: bool
    _result: float | bool | str
    _result_ready: bool
    _result_is_error: bool
    _cv: threading.Condition
    _base: webcface.field.Field

    def __init__(
        self,
        caller_id: int,
        caller: str,
        base: webcface.field.Field,
    ) -> None:
        self._caller_id = caller_id
        self._caller = caller
        self._base = base
        self._started = False
        self._started_ready = False
        self._result = ""
        self._result_ready = False
        self._result_is_error = False
        self._cv = threading.Condition()

    @property
    def member(self) -> webcface.member.Member:
        """関数のMember"""
        return webcface.member.Member(self._base)

    @property
    def name(self) -> str:
        """関数のfield名"""
        return self._base._field

    @property
    def started(self) -> bool:
        """関数が開始したらTrue, 存在しなければFalse

        Falseの場合自動でresultにもFuncNotFoundErrorが入る
        """
        with self._cv:
            while not self._started_ready:
                self._cv.wait()
        return self._started

    @property
    def started_ready(self) -> bool:
        """startedが取得可能であればTrue"""
        return self._started_ready

    @property
    def result(self) -> float | bool | str:
        """実行結果または例外"""
        with self._cv:
            while not self._result_ready:
                self._cv.wait()
        if not self._started:
            raise FuncNotFoundError(self._base)
        if self._result_is_error:
            raise RuntimeError(self._result)
        return self._result

    @property
    def result_ready(self) -> bool:
        """resultが取得可能であればTrue"""
        return self._result_ready
