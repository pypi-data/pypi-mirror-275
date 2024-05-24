from __future__ import annotations
from typing import Optional, Callable, List
from copy import deepcopy
import blinker
import webcface.field
import webcface.view_base
import webcface.view_components
import webcface.client_data
import webcface.func


class ViewComponent(webcface.view_base.ViewComponentBase):
    _data: Optional[webcface.client_data.ClientData]
    _on_click_func_tmp: Optional[webcface.func.AnonymousFunc]

    @staticmethod
    def from_base(
        base: webcface.view_base.ViewComponentBase,
        data: Optional[webcface.client_data.ClientData]
    ) -> ViewComponent:
        vc = ViewComponent(
            base._type,
            base._text,
            base._on_click_func,
            base._text_color,
            base._bg_color,
        )
        vc._data = data
        return vc

    def __init__(
        self,
        type: int = 0,
        text: str = "",
        on_click: Optional[webcface.field.FieldBase | Callable] = None,
        text_color: int = 0,
        bg_color: int = 0,
    ) -> None:
        """コンポーネントを作成

        :arg type: コンポーネントの種類 (text(), button()などコンポーネントを作成する各種関数を使えば自動で設定される)
        :arg text: 表示する文字列
        :arg on_click: クリック時に実行する関数
        :arg text_color: 文字の色 (ViewColorのEnumを使う)
        :arg bg_color: 背景の色 (ViewColorのEnumを使う)
        """
        super().__init__(type, text, None, text_color, bg_color)
        self._data = None
        self._on_click_func = None
        self._on_click_func_tmp = None
        if isinstance(on_click, webcface.func.AnonymousFunc):
            self._on_click_func_tmp = on_click
        elif isinstance(on_click, webcface.field.FieldBase):
            self._on_click_func = on_click
        elif callable(on_click):
            self._on_click_func_tmp = webcface.func.AnonymousFunc(None, on_click)
        if isinstance(on_click, webcface.field.Field) and on_click._data is not None:
            self._data = on_click._data

    def lock_tmp(
        self, data: webcface.client_data.ClientData, field_id: str
    ) -> ViewComponent:
        """AnonymousFuncをFuncオブジェクトにlockする"""
        if self._on_click_func_tmp is not None:
            on_click = webcface.func.Func(
                webcface.field.Field(data, data.self_member_name), field_id
            )
            self._on_click_func_tmp.lock_to(on_click)
            on_click.hidden = True
            self._on_click_func = on_click
        self._data = data
        return self

    def __eq__(self, other) -> bool:
        """プロパティの比較

        :return: プロパティが全部等しければTrueになる
        """
        return (
            isinstance(other, ViewComponent)
            and self._type == other._type
            and self._text == other._text
            and (
                (self._on_click_func is None and other._on_click_func is None)
                or (
                    self._on_click_func is not None
                    and other._on_click_func is not None
                    and self._on_click_func._member == other._on_click_func._member
                    and self._on_click_func._field == other._on_click_func._field
                )
            )
            and self._text_color == other._text_color
            and self._bg_color == other._bg_color
        )

    def __ne__(self, other) -> bool:
        return not self == other

    @property
    def type(self) -> int:
        """コンポーネントの種類

        ViewComponentType Enumを使う
        """
        return self._type

    @property
    def text(self) -> str:
        """表示する文字列"""
        return self._text

    @property
    def on_click(self) -> Optional[webcface.func.Func]:
        """クリックしたときに呼び出す関数"""
        if self._on_click_func is not None:
            if self._data is None:
                raise RuntimeError("internal data not set")
            return webcface.func.Func(
                webcface.field.Field(
                    self._data, self._on_click_func._member, self._on_click_func._field
                )
            )
        return None

    @property
    def text_color(self) -> int:
        """文字の色

        ViewColor Enumを使う
        """
        return self._text_color

    @property
    def bg_color(self) -> int:
        """背景の色

        ViewColor Enumを使う
        """
        return self._bg_color


class View(webcface.field.Field):
    _components: List[ViewComponent | str | bool | float | int]
    _modified: bool

    def __init__(self, base: webcface.field.Field, field: str = "") -> None:
        """Viewを指すクラス

        このコンストラクタを直接使わず、
        Member.view(), Member.views(), Member.onViewEntry などを使うこと

        詳細は `Viewのドキュメント <https://na-trium-144.github.io/webcface/md_13__view.html>`_ を参照
        """
        super().__init__(
            base._data, base._member, field if field != "" else base._field
        )
        self._components = []
        self._modified = False

    @property
    def member(self) -> webcface.member.Member:
        """Memberを返す"""
        return webcface.member.Member(self)

    @property
    def name(self) -> str:
        """field名を返す"""
        return self._field

    @property
    def signal(self) -> blinker.NamedSignal:
        """値が変化したときのイベント

        コールバックの引数にはViewオブジェクトが渡される。

        まだリクエストされてなければ自動でリクエストする。
        """
        self.request()
        return self._data_check().signal("view_change", self._member, self._field)

    def child(self, field: str) -> View:
        """子フィールドを返す

        :return: 「(thisのフィールド名).(子フィールド名)」をフィールド名とするView
        """
        return View(self, self._field + "." + field)

    def request(self) -> None:
        """値の受信をリクエストする"""
        req = self._data_check().view_store.add_req(self._member, self._field)
        if req > 0:
            self._data_check().queue_msg(
                [webcface.message.ViewReq.new(self._member, self._field, req)]
            )

    def try_get(self) -> Optional[List[ViewComponent]]:
        """ViewをlistまたはNoneで返す、まだリクエストされてなければ自動でリクエストされる"""
        self.request()
        v = self._data_check().view_store.get_recv(self._member, self._field)
        v2: Optional[List[ViewComponent]] = None
        if v is not None:
            v2 = [ViewComponent.from_base(vb, self._data) for vb in v]
        return v2

    def get(self) -> List[ViewComponent]:
        """Viewをlistで返す、まだリクエストされてなければ自動でリクエストされる"""
        v = self.try_get()
        return v if v is not None else []

    def set(self, components: List[ViewComponent | str | bool | float | int]) -> View:
        """Viewのリストをセットする"""
        data2 = []
        for c in components:
            if isinstance(c, ViewComponent):
                data2.append(c)
            elif isinstance(c, str):
                while "\n" in c:
                    s = c[: c.find("\n")]
                    data2.append(webcface.view_components.text(s))
                    data2.append(webcface.view_components.new_line())
                    c = c[c.find("\n") + 1 :]
                if c != "":
                    data2.append(webcface.view_components.text(c))
            else:
                data2.append(webcface.view_components.text(str(c)))
        for i, c in enumerate(data2):
            data2[i] = c.lock_tmp(self._set_check(), f"{self._field}_f{i}")
        self._set_check().view_store.set_send(self._field, list(data2))
        self.signal.send(self)
        return self

    def __enter__(self) -> View:
        """with構文の最初で自動でinit()を呼ぶ"""
        self.init()
        return self

    def init(self) -> View:
        """このViewオブジェクトにaddした内容を初期化する"""
        self._components = []
        self._modified = True
        return self

    def __exit__(self, type, value, tb) -> None:
        """with構文の終わりに自動でsync()を呼ぶ"""
        self.sync()

    def sync(self) -> View:
        """Viewの内容をclientに反映し送信可能にする"""
        self._set_check()
        if self._modified:
            self.set(self._components)
            self._modified = False
        return self

    def add(self, *args: ViewComponent | str | bool | float | int) -> View:
        """コンポーネントを追加

        Viewオブジェクトが生成されて最初のaddのとき自動でinit()をする
        """
        for c in args:
            self._components.append(c)
        self._modified = True
        return self
