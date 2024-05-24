import threading
import logging
from typing import List
import webcface.client_data
import webcface.message
import webcface.client
import webcface.canvas2d_base
import webcface


def on_recv(
    wcli: "webcface.client.Client",
    data: webcface.client_data.ClientData,
    message: bytes,
) -> None:
    sync_members: List[str] = []
    if len(message) > 0:
        for m in webcface.message.unpack(message):
            if isinstance(m, webcface.message.SvrVersion):
                data.svr_name = m.svr_name
                data.svr_version = m.ver
            if isinstance(m, webcface.message.Ping):
                data.queue_msg([webcface.message.Ping.new()])
            if isinstance(m, webcface.message.PingStatus):
                data.ping_status = m.status
                for member2 in wcli.members():
                    data.signal("ping", member2.name).send(member2)
            if isinstance(m, webcface.message.Sync):
                member = data.get_member_name_from_id(m.member_id)
                data.sync_time_store.set_recv(member, m.time)
                sync_members.append(member)
            if isinstance(m, webcface.message.SyncInit):
                data.value_store.add_member(m.member_name)
                data.text_store.add_member(m.member_name)
                data.func_store.add_member(m.member_name)
                data.view_store.add_member(m.member_name)
                data.canvas2d_store.add_member(m.member_name)
                data.canvas3d_store.add_member(m.member_name)
                data.member_ids[m.member_name] = m.member_id
                data.member_lib_name[m.member_id] = m.lib_name
                data.member_lib_ver[m.member_id] = m.lib_ver
                data.member_remote_addr[m.member_id] = m.addr
                data.signal("member_entry").send(wcli.member(m.member_name))
            if isinstance(m, webcface.message.ValueRes):
                member, field = data.value_store.get_req(m.req_id, m.sub_field)
                data.value_store.set_recv(member, field, m.data)
                data.signal("value_change", member, field).send(
                    wcli.member(member).value(field)
                )
            if isinstance(m, webcface.message.ValueEntry):
                member = data.get_member_name_from_id(m.member_id)
                data.value_store.set_entry(member, m.field)
                data.signal("value_entry", member).send(
                    wcli.member(member).value(m.field)
                )
            if isinstance(m, webcface.message.TextRes):
                member, field = data.text_store.get_req(m.req_id, m.sub_field)
                data.text_store.set_recv(member, field, m.data)
                data.signal("text_change", member, field).send(
                    wcli.member(member).text(field)
                )
            if isinstance(m, webcface.message.TextEntry):
                member = data.get_member_name_from_id(m.member_id)
                data.text_store.set_entry(member, m.field)
                data.signal("text_entry", member).send(
                    wcli.member(member).text(m.field)
                )
            if isinstance(m, webcface.message.ViewRes):
                member, field = data.view_store.get_req(m.req_id, m.sub_field)
                v_prev = data.view_store.get_recv(member, field)
                if v_prev is None:
                    v_prev = []
                    data.view_store.set_recv(member, field, v_prev)
                for i, c in m.data_diff.items():
                    if int(i) >= len(v_prev):
                        v_prev.append(c)
                    else:
                        v_prev[int(i)] = c
                if len(v_prev) >= m.length:
                    del v_prev[m.length :]
                data.signal("view_change", member, field).send(
                    wcli.member(member).view(field)
                )
            if isinstance(m, webcface.message.ViewEntry):
                member = data.get_member_name_from_id(m.member_id)
                data.view_store.set_entry(member, m.field)
                data.signal("view_entry", member).send(
                    wcli.member(member).view(m.field)
                )
            if isinstance(m, webcface.message.Canvas2DRes):
                member, field = data.canvas2d_store.get_req(m.req_id, m.sub_field)
                c2_prev = data.canvas2d_store.get_recv(member, field)
                if c2_prev is None:
                    c2_prev = webcface.canvas2d_base.Canvas2DData(1.0, 1.0)
                    data.canvas2d_store.set_recv(member, field, c2_prev)
                c2_prev.width = m.width
                c2_prev.height = m.height
                for i, c2 in m.data_diff.items():
                    if int(i) >= len(c2_prev.components):
                        c2_prev.components.append(c2)
                    else:
                        c2_prev.components[int(i)] = c2
                if len(c2_prev.components) >= m.length:
                    del c2_prev.components[m.length :]
                data.signal("canvas2d_change", member, field).send(
                    wcli.member(member).canvas2d(field)
                )
            if isinstance(m, webcface.message.Canvas2DEntry):
                member = data.get_member_name_from_id(m.member_id)
                data.canvas2d_store.set_entry(member, m.field)
                data.signal("canvas2d_entry", member).send(
                    wcli.member(member).canvas2d(m.field)
                )
            if isinstance(m, webcface.message.Canvas3DRes):
                member, field = data.canvas3d_store.get_req(m.req_id, m.sub_field)
                c3_prev = data.canvas3d_store.get_recv(member, field)
                if c3_prev is None:
                    c3_prev = []
                    data.canvas3d_store.set_recv(member, field, c3_prev)
                for i, c3 in m.data_diff.items():
                    if int(i) >= len(c3_prev):
                        c3_prev.append(c3)
                    else:
                        c3_prev[int(i)] = c3
                if len(c3_prev) >= m.length:
                    del c3_prev[m.length :]
                data.signal("canvas3d_change", member, field).send(
                    wcli.member(member).canvas3d(field)
                )
            if isinstance(m, webcface.message.Canvas3DEntry):
                member = data.get_member_name_from_id(m.member_id)
                data.canvas3d_store.set_entry(member, m.field)
                data.signal("canvas3d_entry", member).send(
                    wcli.member(member).canvas3d(m.field)
                )
            if isinstance(m, webcface.message.FuncInfo):
                member = data.get_member_name_from_id(m.member_id)
                data.func_store.set_entry(member, m.field)
                data.func_store.set_recv(member, m.field, m.func_info)
                data.signal("func_entry", member).send(
                    wcli.member(member).func(m.field)
                )
            if isinstance(m, webcface.message.Call):
                func_info = data.func_store.get_recv(data.self_member_name, m.field)
                if func_info is not None:

                    def do_call():
                        data.queue_msg(
                            [
                                webcface.message.CallResponse.new(
                                    m.caller_id, m.caller_member_id, True
                                )
                            ]
                        )
                        try:
                            result = func_info.run(m.args)
                            is_error = False
                        except Exception as e:
                            is_error = True
                            result = str(e)
                        data.queue_msg(
                            [
                                webcface.message.CallResult.new(
                                    m.caller_id,
                                    m.caller_member_id,
                                    is_error,
                                    result,
                                )
                            ]
                        )

                    threading.Thread(target=do_call).start()
                else:
                    data.queue_msg(
                        [
                            webcface.message.CallResponse.new(
                                m.caller_id, m.caller_member_id, False
                            )
                        ]
                    )
            if isinstance(m, webcface.message.CallResponse):
                try:
                    r = data.func_result_store.get_result(m.caller_id)
                    with r._cv:
                        r._started = m.started
                        r._started_ready = True
                        if not m.started:
                            r._result_is_error = True
                            r._result_ready = True
                        r._cv.notify_all()
                except IndexError:
                    data.logger_internal.error(
                        f"error receiving call response id={m.caller_id}"
                    )
            if isinstance(m, webcface.message.CallResult):
                try:
                    r = data.func_result_store.get_result(m.caller_id)
                    with r._cv:
                        r._result_is_error = m.is_error
                        r._result = m.result
                        r._result_ready = True
                        r._cv.notify_all()
                except IndexError:
                    data.logger_internal.error(
                        f"error receiving call result id={m.caller_id}"
                    )
            if isinstance(m, webcface.message.Log):
                member = data.get_member_name_from_id(m.member_id)
                log_s = data.log_store.get_recv(member)
                if log_s is None:
                    log_s = []
                    data.log_store.set_recv(member, log_s)
                log_s.extend(m.log)
                data.signal("log_append", member).send(wcli.member(member).log())
        for member in sync_members:
            data.signal("sync", member).send(wcli.member(member))


def sync_data_first(
    wcli: "webcface.client.Client", data: webcface.client_data.ClientData
) -> List[webcface.message.MessageBase]:
    msgs: List[webcface.message.MessageBase] = []
    msgs.append(
        webcface.message.SyncInit.new(wcli.name, "python", webcface.__version__)
    )

    with data.value_store.lock:
        for m, r in data.value_store.transfer_req().items():
            for k, i in r.items():
                msgs.append(webcface.message.ValueReq.new(m, k, i))
    with data.text_store.lock:
        for m, r in data.text_store.transfer_req().items():
            for k, i in r.items():
                msgs.append(webcface.message.TextReq.new(m, k, i))
    with data.view_store.lock:
        for m, r in data.view_store.transfer_req().items():
            for k, i in r.items():
                msgs.append(webcface.message.ViewReq.new(m, k, i))
    with data.canvas2d_store.lock:
        for m, r in data.canvas2d_store.transfer_req().items():
            for k, i in r.items():
                msgs.append(webcface.message.Canvas2DReq.new(m, k, i))
    with data.canvas3d_store.lock:
        for m, r in data.canvas3d_store.transfer_req().items():
            for k, i in r.items():
                msgs.append(webcface.message.Canvas3DReq.new(m, k, i))
    with data.log_store.lock:
        for m, r2 in data.log_store.transfer_req().items():
            msgs.append(webcface.message.LogReq.new(m))

    msgs.extend(sync_data(wcli, data, True))
    return msgs


def sync_data(
    wcli: "webcface.client.Client",
    data: webcface.client_data.ClientData,
    is_first: bool,
) -> List[webcface.message.MessageBase]:
    msgs: List[webcface.message.MessageBase] = []
    msgs.append(webcface.message.Sync.new())

    with data.value_store.lock:
        for k, v in data.value_store.transfer_send(is_first).items():
            msgs.append(webcface.message.Value.new(k, v))
    with data.text_store.lock:
        for k, v2 in data.text_store.transfer_send(is_first).items():
            msgs.append(webcface.message.Text.new(k, v2))
    with data.view_store.lock:
        view_send_prev = data.view_store.get_send_prev(is_first)
        view_send = data.view_store.transfer_send(is_first)
        for k, v4 in view_send.items():
            v_prev = view_send_prev.get(k, [])
            v_diff = {}
            for i, c in enumerate(v4):
                if i >= len(v_prev) or v_prev[i] != c:
                    v_diff[str(i)] = c
            msgs.append(webcface.message.View.new(k, v_diff, len(v4)))
    with data.canvas2d_store.lock:
        canvas2d_send_prev = data.canvas2d_store.get_send_prev(is_first)
        canvas2d_send = data.canvas2d_store.transfer_send(is_first)
        for k, v5 in canvas2d_send.items():
            c2_prev = canvas2d_send_prev.get(
                k, webcface.canvas2d_base.Canvas2DData(1.0, 1.0)
            )
            c2_diff = {}
            for i, c2 in enumerate(v5.components):
                if i >= len(c2_prev.components) or c2_prev.components[i] != c2:
                    c2_diff[str(i)] = c2
            msgs.append(
                webcface.message.Canvas2D.new(
                    k, v5.width, v5.height, c2_diff, len(v5.components)
                )
            )
    with data.canvas3d_store.lock:
        canvas3d_send_prev = data.canvas3d_store.get_send_prev(is_first)
        canvas3d_send = data.canvas3d_store.transfer_send(is_first)
        for k, v6 in canvas3d_send.items():
            c3_prev = canvas3d_send_prev.get(k, [])
            c3_diff = {}
            for i, c3 in enumerate(v6):
                if i >= len(c3_prev) or c3_prev[i] != c3:
                    c3_diff[str(i)] = c3
            msgs.append(webcface.message.Canvas3D.new(k, c3_diff, len(v6)))
    with data.log_store.lock:
        log_all = data.log_store.get_recv(data.self_member_name)
        assert log_all is not None
        if is_first:
            log_send = log_all
        else:
            log_send = log_all[data.log_sent_lines :]
        data.log_sent_lines = len(log_all)
        if len(log_send) > 0:
            msgs.append(webcface.message.Log.new(log_send))
    with data.func_store.lock:
        for k, v3 in data.func_store.transfer_send(is_first).items():
            if not v3.hidden:
                msgs.append(webcface.message.FuncInfo.new(k, v3))

    return msgs
