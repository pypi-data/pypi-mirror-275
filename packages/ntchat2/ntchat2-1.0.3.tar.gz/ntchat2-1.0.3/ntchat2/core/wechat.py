import typing

import pyee
import json
from ntchat2.core.mgr import WeChatMgr
from ntchat2.const import notify_type
from threading import Event
from ntchat2.wc import wcprobe
from ntchat2.utils import generate_guid, fake_wechat_version
from ntchat2.utils import logger
from ntchat2.exception import WeChatNotLoginError
from functools import wraps
from typing import (
    List,
    Union,
    Tuple
)

log = logger.get_logger("WeChatInstance")


class ReqData:
    __response_message = None
    msg_type: int = 0
    request_data = None

    def __init__(self, msg_type, data):
        self.msg_type = msg_type
        self.request_data = data
        self.__wait_event = Event()

    def wait_response(self, timeout=None):
        self.__wait_event.wait(timeout)
        return self.get_response_data()

    def on_response(self, message):
        self.__response_message = message
        self.__wait_event.set()

    def get_response_data(self):
        if self.__response_message is None:
            return None
        return self.__response_message["data"]


class RaiseExceptionFunc:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            self.func(*args, **kwargs)
        except Exception as e:
            log.error('callback error, in function `%s`, error: %s', self.func.__name__, e)


class WeChat:
    version: str = "3.6.0.18"
    client_id: int = 0
    pid: int = 0
    status: bool = False
    login_status: bool = False

    def __init__(self):
        WeChatMgr().append_instance(self)
        self.__wait_login_event = Event()
        self.__req_data_cache = {}
        self.event_emitter = pyee.EventEmitter()
        self.__login_info = {}

    def on(self, msg_type, f):
        if not (isinstance(msg_type, list) or isinstance(msg_type, tuple)):
            msg_type = [msg_type]
        for event in msg_type:
            self.event_emitter.on(str(event), RaiseExceptionFunc(f))

    def msg_register(self, msg_type: Union[int, List[int], Tuple[int]]):
        def wrapper(f):
            wraps(f)
            self.on(msg_type, f)
            return f
        return wrapper

    def on_close(self):
        self.login_status = False
        self.status = False
        self.event_emitter.emit(str(notify_type.MT_RECV_WECHAT_QUIT_MSG), self)

        message = {
            "type": notify_type.MT_RECV_WECHAT_QUIT_MSG,
            "data": {}
        }
        self.event_emitter.emit(str(notify_type.MT_ALL), self, message)

    def bind_client_id(self, client_id):
        self.status = True
        self.client_id = client_id

    def on_recv(self, message):
        log.debug("on recv message: %s", message)
        msg_type = message["type"]
        extend = message.get("extend", None)

        if self.faked_wechat_version is not None and msg_type == notify_type.MT_RECV_LOGIN_HWND_MSG and message["data"]["login_hwnd"] != 0:
            if fake_wechat_version(self.pid, self.version, self.faked_wechat_version) == 0:
                log.info(f"wechat version faked: {self.version} -> {self.faked_wechat_version}")
            else:
                log.info(f"wechat version fake failed.")
        elif msg_type == notify_type.MT_USER_LOGIN_MSG:
            self.login_status = True
            self.__wait_login_event.set()
            self.__login_info = message.get("data", {})
            log.info("login success, wxid: %s, nickname: %s", self.__login_info["wxid"], self.__login_info["nickname"])
        elif msg_type == notify_type.MT_USER_LOGOUT_MSG:
            self.login_status = False
            log.info("logout, pid: %d", self.pid)

        if extend is not None and extend in self.__req_data_cache:
            req_data = self.__req_data_cache[extend]
            req_data.on_response(message)
            del self.__req_data_cache[extend]
        else:
            self.event_emitter.emit(str(msg_type), self, message)
            self.event_emitter.emit(str(notify_type.MT_ALL), self, message)

    def wait_login(self, timeout=None):
        log.info("wait login...")
        self.__wait_login_event.wait(timeout)

    def open(self, smart=False, show_login_qrcode=False, faked_wechat_version=None):
        if show_login_qrcode:
            wcprobe.show_login_qrcode()

        self.faked_wechat_version = faked_wechat_version
        self.pid = wcprobe.open(smart)
        log.info("open wechat pid: %d", self.pid)
        return self.pid != 0

    def attach(self, pid: int):
        self.pid = pid
        log.info("attach wechat pid: %d", self.pid)
        return wcprobe.attach(pid)

    def detach(self):
        log.info("detach wechat pid: %d", self.pid)
        return wcprobe.detach(self.pid)

    def _send(self, msg_type, data=None, extend=None):
        if not self.login_status:
            raise WeChatNotLoginError()

        message = {
            'type': msg_type,
            'data': {} if data is None else data,
        }
        if extend is not None:
            message["extend"] = extend
        message_json = json.dumps(message)
        log.debug("communicate wechat pid: %d,  data: %s", self.pid, message)
        return wcprobe.send(self.client_id, message_json)

    def _send_sync(self, msg_type, data=None, timeout=10):
        req_data = ReqData(msg_type, data)
        extend = self.__new_extend()
        self.__req_data_cache[extend] = req_data
        self._send(msg_type, data, extend)
        return req_data.wait_response(timeout)

    def send(self, data):
        return self._send(data["type"], data["data"])

    def send_sync(self, data):
        return self._send_sync(data["type"], data["data"])

    def __new_extend(self):
        while True:
            guid = generate_guid("req")
            if guid not in self.__req_data_cache:
                return guid

    def __repr__(self):
        return f"WeChatInstance(pid: {self.pid}, client_id: {self.client_id})"

    def refresh_qrcode(self):
        """刷新登录二维码"""
        data = {
            "type": 11087,
            "data": {}
        }
        return self.send(data)

    def logout(self):
        """退出登录"""
        data = {
            "type": 11104,
            "data": {}
        }
        return self.send(data)

    def exit(self):
        """退出微信"""
        data = {
            "type": 11105,
            "data": {}
        }
        return self.send(data)

    def get_self_info(self):
        """获取当前账号信息"""
        data = {
            "type": 11028,
            "data": {}
        }
        return self.send_sync(data)

    def get_contacts(self):
        """获取好友列表"""
        data = {
            "type": 11030,
            "data": {}
        }
        return self.send_sync(data)

    def get_contact(self, wxid: str):
        """获取好友信息"""
        data = {
            "type": 11029,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def get_rooms(self, detail: int = 1):
        """获取群列表"""
        data = {
            "type": 11031,
            "data": {
                "detail": detail
            }
        }
        return self.send_sync(data)

    def get_room(self, room_wxid: str):
        """获取群信息"""
        data = {
            "type": 11125,
            "data": {
                "room_wxid": room_wxid
            }
        }
        return self.send_sync(data)

    def get_room_members(self, room_wxid: str):
        """获取群成员列表"""
        data = {
            "type": 11032,
            "data": {
                "room_wxid": room_wxid
            }
        }
        return self.send_sync(data)

    def get_public(self):
        """获取公众号列表"""
        data = {
            "type": 11033,
            "data": {}
        }
        return self.send_sync(data)

    def get_contact_by_protocol(self, wxid: str):
        """获取好友简要信息（协议）"""
        data = {
            "type": 11034,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def get_room_member_by_net(self, room_wxid, wxid):
        """获取群成员信息"""
        data = {
            "type": 111035,
            "data": {
                "room_wxid": room_wxid,
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def send_text(self, to_wxid: str, content: str):
        """发送文本消息"""
        data = {
            "type": 11036,
            "data": {
                "to_wxid": to_wxid,
                "content": content
            }
        }
        return self.send(data)

    def send_room_at(self, to_wxid: str, content: str, at_list: typing.List[str]):
        """发送群at消息"""
        data = {
            "type": 11037,
            "data": {
                "to_wxid": to_wxid,
                "content": content,
                "at_list": at_list
            }
        }
        return self.send(data)

    def send_card(self, to_wxid: str, card_wxid: str):
        """发送名片消息"""
        data = {
            "type": 11038,
            "data": {
                "to_wxid": to_wxid,
                "card_wxid": card_wxid
            }
        }
        return self.send(data)

    def send_link(self, to_wxid: str, title: str, desc: str, url: str, image_url: str):
        """发送链接卡片消息"""
        data = {
            "type": 11039,
            "data": {
                "to_wxid": to_wxid,
                "title": title,
                "desc": desc,
                "url": url,
                "image_url": image_url
            }
        }
        return self.send(data)

    def send_image(self, to_wxid: str, file: str):
        """发送图片消息"""
        data = {
            "type": 11040,
            "data": {
                "to_wxid": to_wxid,
                "file": file
            }
        }
        return self.send(data)

    def send_file(self, to_wxid: str, file: str):
        """发送文件消息"""
        data = {
            "type": 11041,
            "data": {
                "to_wxid": to_wxid,
                "file": file
            }
        }
        return self.send(data)

    def send_video(self, to_wxid: str, file: str):
        """发送视频消息"""
        data = {
            "type": 11042,
            "data": {
                "to_wxid": to_wxid,
                "file": file
            }
        }
        return self.send(data)

    def send_emotion(self, to_wxid: str, file: str):
        """发送表情消息"""
        data = {
            "type": 11043,
            "data": {
                "to_wxid": to_wxid,
                "file": file
            }
        }
        return self.send(data)

    def send_xml(self, to_wxid: str, xml: str):
        """发送xml消息"""
        data = {
            "type": 11113,
            "data": {
                "to_wxid": to_wxid,
                "xml": xml
            }
        }
        return self.send(data)

    def send_pat(self, room_wxid: str, patted_wxid: str):
        """发送拍一拍消息"""
        data = {
            "type": 11250,
            "data": {
                "room_wxid": room_wxid,
                "patted_wxid": patted_wxid
            }
        }
        return self.send(data)

    def forward_msg(self, to_wxid: str, msg_id: str):
        """转发消息"""
        data = {
            "type": 11245,
            "data": {
                "to_wxid": to_wxid,
                "msgid": msg_id
            }
        }
        return self.send(data)

    def get_contact_detail_by_protocol(self, wxid: str):
        """获取好友详细信息（协议）"""
        data = {
            "type": 11174,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def get_contacts_by_protocol(self, wxids: typing.List[str]):
        """获取多个好友信息（协议）"""
        data = {
            "type": 11174,
            "data": {
                "username_list": wxids
            }
        }
        return self.send_sync(data)

    def modify_contact_remark(self, wxid: str, remark: str):
        """修改好友备注"""
        data = {
            "type": 11063,
            "data": {
                "wxid": wxid,
                "remark": remark
            }
        }
        return self.send_sync(data)

    def delete_friend(self, wxid: str):
        """删除好友"""
        data = {
            "type": 11064,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def accept_friend_request(self, encrypt_username: str, ticket: str, scene: int = 17):
        """同意好友请求"""
        data = {
            "type": 11065,
            "data": {
                "encryptusername": encrypt_username,
                "ticket": ticket,
                "scene": scene
            },
        }
        return self.send_sync(data)

    def search_friend(self, search: str):
        """搜索微信好友"""
        data = {
            "type": 11096,
            "data": {
                "search": search
            }
        }
        return self.send_sync(data)

    def add_friend(self, v1: str, v2: str, remark: str):
        """添加好友"""
        data = {
            "type": 11097,
            "data": {
                "v1": v1,
                "v2": v2,
                "remark": remark
            }
        }
        return self.send_sync(data)

    def add_friend_by_card(self, wxid: str, ticket: str, remark: str):
        """添加好友分享的名片"""
        data = {
            "type": 11062,
            "data": {
                "remark": remark,
                "source_type": 17,
                "wxid": wxid,
                "ticket": ticket
            }
        }
        return self.send_sync(data)

    def add_friend_by_room(self, room_wxid: str, wxid: str, remark: str):
        """添加群成员为好友"""
        data = {
            "type": 11062,
            "data": {
                "remark": remark,
                "source_type": 14,
                "wxid": wxid,
                "room_wxid": room_wxid
            }
        }
        return self.send_sync(data)

    def check_friend_status(self, wxid: str):
        """检查好友状态"""
        data = {
            "type": 11080,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def get_room_by_protocol(self, wxid: str):
        """获取群信息（协议）"""
        data = {
            "type": 11174,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def get_invitation_relationship(self, room_wxid: str):
        """获取群成员邀请关系"""
        data = {
            "type": 11134,
            "data": {
                "room_wxid": room_wxid
            }
        }
        return self.send_sync(data)

    def create_room(self, member_list: typing.List[str]):
        """创建群聊"""
        data = {
            "type": 11068,
            "data": member_list
        }
        return self.send(data)

    def create_room_by_protocol(self, member_list: typing.List[str]):
        """创建群聊（协议）"""
        data = {
            "type": 11246,
            "data": member_list
        }
        return self.send_sync(data)

    def add_room_member(self, room_wxid: str, member_list: typing.List[str]):
        """添加群成员"""
        data = {
            "type": 11069,
            "data": {
                "room_wxid": room_wxid,
                "member_list": member_list
            }
        }
        return self.send_sync(data)

    def invite_room_member(self, room_wxid: str, member_list: typing.List[str]):
        """邀请群成员"""
        data = {
            "type": 11070,
            "data": {
                "room_wxid": room_wxid,
                "member_list": member_list
            }
        }
        return self.send_sync(data)

    def remove_room_member(self, room_wxid: str, wxid: str):
        """移出群成员"""
        data = {
            "type": 11071,
            "data": {
                "room_wxid": room_wxid,
                "name": wxid
            }
        }
        return self.send_sync(data)

    def modify_room_name(self, room_wxid: str, name: str):
        """修改群名称"""
        data = {
            "type": 11072,
            "data": {
                "room_wxid": room_wxid,
                "name": name
            }
        }
        return self.send_sync(data)

    def modify_room_notice(self, room_wxid: str, notice: str):
        """修改群公告"""
        data = {
            "type": 11073,
            "data": {
                "room_wxid": room_wxid,
                "notice": notice
            }
        }
        return self.send_sync(data)

    def modify_room_member_nickname(self, room_wxid: str, nickname: str):
        """修改我在本群的昵称"""
        data = {
            "type": 11074,
            "data": {
                "room_wxid": room_wxid,
                "nickname": nickname
            }
        }
        return self.send_sync(data)

    def display_room_member_nickname(self, room_wxid: str, status: int = 1):
        """是否显示群成员昵称"""
        data = {
            "type": 11075,
            "data": {
                "room_wxid": room_wxid,
                "status": status
            }
        }
        return self.send_sync(data)

    def edit_address_book(self, room_wxid: str, status: int = 1):
        """保存/移出通讯录"""
        data = {
            "type": 11076,
            "data": {
                "room_wxid": room_wxid,
                "status": status
            }
        }
        return self.send_sync(data)

    def exit_room(self, room_wxid: str):
        """退出群聊"""
        data = {
            "type": 11077,
            "data": {
                "room_wxid": room_wxid
            }
        }
        return self.send_sync(data)

    def get_corporate_contacts(self):
        """获取企业联系人"""
        data = {
            "type": 11132,
            "data": {}
        }
        return self.send_sync(data)

    def get_corporate_rooms(self):
        """获取企业群"""
        data = {
            "type": 11129,
            "data": {}
        }
        return self.send_sync(data)

    def get_corporate_room_members(self, room_wxid):
        """获取企业微信群成员"""
        data = {
            "type": 11130,
            "data": {
                "room_wxid": room_wxid
            }
        }
        return self.send_sync(data)

    def cdn_init(self):
        """初始化CDN"""
        data = {
            "type": 11228,
            "data": {}
        }
        return self.send_sync(data)

    def cdn_upload(self, file_path):
        """CDN上传"""
        data = {
            "type": 11229,
            "data": {
                "file_type": 2,
                "file_path": file_path
            }
        }
        return self.send_sync(data)

    def cdn_download(self, file_id: str, aes_key: str, save_path: str, file_type: int = 2):
        """CDN下载"""
        data = {
            "type": 11230,
            "data": {
                "file_id": file_id,
                "file_type": file_type,
                "aes_key": aes_key,
                "save_path": save_path
            }
        }
        return self.send_sync(data)

    def cdn_download2(self, url: str, auth_key: str, aes_key: str, save_path: str):
        """企业微信CDN下载"""
        data = {
            "type": 11253,
            "data": {
                "url": url,
                "auth_key": auth_key,
                "aes_key": aes_key,
                "save_path": save_path
            }
        }
        return self.send_sync(data)

    def send_text_by_cdn(self, to_wxid, content):
        """发送文本消息（CDN）"""
        data = {
            "type": 11237,
            "data": {
                "to_wxid": to_wxid,
                "content": content
            }
        }
        return self.send_sync(data)

    def send_room_at_by_cdn(self, to_wxid, content, at_list=None, at_all=0):
        """发送群at消息（CDN）"""
        if at_all == 0:
            if not isinstance(at_list, list):
                raise TypeError("at_list must be a list.")

            data = {
                "type": 11240,
                "data": {
                    "to_wxid": to_wxid,
                    "content": content,  # {$@}
                    "at_list": at_list
                }
            }
        else:
            data = {
                "type": 11240,
                "data": {
                    "to_wxid": to_wxid,
                    "content": content,  # {$@}
                    "at_all": 1
                }
            }
        return self.send_sync(data)

    def send_image_by_cdn(self, to_wxid: str, file_id: str, file_md5: str, file_size: int, thumb_file_size: int,
                          crc32: int, aes_key: str):
        """发送图片消息（CDN）"""
        data = {
            "type": 11231,
            "data": {
                "aes_key": aes_key,
                "file_id": file_id,
                "file_md5": file_md5,
                "file_size": file_size,
                "thumb_file_size": thumb_file_size,
                "crc32": crc32,
                "to_wxid": to_wxid
            }
        }
        return self.send_sync(data)

    def send_video_by_cdn(self, to_wxid: str, file_id: str, file_md5: str, file_size: int, thumb_file_size: int,
                          aes_key: str):
        """发送视频消息（CDN）"""
        data = {
            "type": 11233,
            "data": {
                "aes_key": aes_key,
                "file_id": file_id,
                "file_md5": file_md5,
                "file_size": file_size,
                "thumb_file_size": thumb_file_size,
                "to_wxid": to_wxid
            }
        }
        return self.send_sync(data)

    def send_file_by_cdn(self, to_wxid: str, file_id: str, file_md5: str, file_size: int, file_name: str,
                         aes_key: str):
        """发送文件消息（CDN）"""
        data = {
            "type": 11235,
            "data": {
                "aes_key": aes_key,
                "file_id": file_id,
                "file_md5": file_md5,
                "file_name": file_name,
                "file_size": file_size,
                "to_wxid": to_wxid
            }
        }
        return self.send_sync(data)

    def send_link_card_by_cdn(self, to_wxid: str, title: str, desc: str, url: str, image_url: str):
        """发送链接卡片消息（CDN）"""
        data = {
            "type": 11236,
            "data": {
                "to_wxid": to_wxid,
                "title": title,
                "desc": desc,
                "url": url,
                "image_url": image_url
            }
        }
        return self.send_sync(data)

    def send_emotion_by_cdn(self, aes_key: str, file_id: str, file_md5: str, file_size: int, to_wxid: str):
        """发送表情消息（CDN）"""
        data = {
            "type": 11241,
            "data": {
                "aes_key": aes_key,
                "file_id": file_id,
                "file_md5": file_md5,
                "file_size": file_size,
                "to_wxid": to_wxid
            }
        }
        return self.send_sync(data)

    def send_emotion2_by_cdn(self, to_wxid: str, path: str):
        """发送表情消息2（CDN）"""
        data = {
            "type": 11254,
            "data": {
                "to_wxid": to_wxid,
                "path": path
            }
        }
        return self.send_sync(data)

    def send_mini_program_by_cdn(self, to_wxid: str, username: str, appid: str, appname: str, appicon: str, title: str,
                                 page_path: str, aes_key: str, file_id: str, file_md5: str, file_size: int):
        """发送小程序消息（CDN）"""
        data = {
            "type": 11242,
            "data": {
                "to_wxid": to_wxid,
                "username": username,
                "appid": appid,
                "appname": appname,
                "appicon": appicon,
                "title": title,
                "page_path": page_path,
                "file_id": file_id,
                "aes_key": aes_key,
                "file_md5": file_md5,
                "file_size": file_size
            }
        }
        return self.send_sync(data)

    def send_video_card_by_cdn(self, to_wxid: str, object_id: str, object_nonce_id: str, nickname: str, username: str,
                               avatar: str, desc: str, thumb_url: str, url: str):
        """发送视频号消息（CDN）"""
        data = {
            "type": 11243,
            "data": {
                "to_wxid": to_wxid,
                "object_id": object_id,
                "object_nonce_id": object_nonce_id,
                "nickname": nickname,
                "username": username,
                "avatar": avatar,
                "desc": desc,
                "thumb_url": thumb_url,
                "url": url
            }
        }
        return self.send_sync(data)

    def send_card_by_cdn(self, to_wxid: str, username: str, nickname: str, avatar: str):
        """发送名片消息（CDN）"""
        data = {
            "type": 11239,
            "data": {
                "to_wxid": to_wxid,
                "username": username,
                "nickname": nickname,
                "avatar": avatar
            }
        }
        return self.send_sync(data)

    def send_location_by_cdn(self, to_wxid: str, address: str, latitude: float, longitude: float, title: str):
        """发送位置消息（CDN）"""
        data = {
            "type": 11238,
            "data": {
                "to_wxid": to_wxid,
                "address": address,
                "latitude": latitude,
                "longitude": longitude,
                "title": title
            }
        }
        return self.send_sync(data)

    def revoke_msg_by_cdn(self, to_wxid: str, new_msg_id: str, client_msg_id: int, create_time: int):
        """撤回消息（CDN）"""
        data = {
            "type": 11244,
            "data": {
                "to_wxid": to_wxid,
                "client_msgid": client_msg_id,
                "create_time": create_time,
                "new_msgid": new_msg_id
            }
        }
        return self.send_sync(data)

    def send_xml_by_cdn(self, to_wxid: str, content: str):
        """发送xml消息（CDN）"""
        data = {
            "type": 11214,
            "data": {
                "to_wxid": to_wxid,
                "content": content
            }
        }
        return self.send_sync(data)

    def get_collections(self):
        """获取收藏列表"""
        data = {
            "type": 11109,
            "data": {}
        }
        return self.send_sync(data)

    def send_collection(self, to_wxid: str, local_id: int):
        """发送收藏消息"""
        data = {
            "type": 11110,
            "data": {
                "to_wxid": to_wxid,
                "local_id": local_id
            }
        }
        return self.send(data)

    def collect(self, msg_id: str):
        """收藏消息"""
        data = {
            "type": 11111,
            "data": {
                "msgid": msg_id
            }
        }
        return self.send(data)

    def get_tags(self):
        """获取标签列表"""
        data = {
            "type": 11142,
            "data": {}
        }
        return self.send_sync(data)

    def confirm_receipt(self, transfer_id: str):
        """确认收款"""
        data = {
            "type": 11066,
            "data": {
                "transferid": transfer_id
            }
        }
        return self.send(data)

    def add_tag(self, label_name: str):
        """添加标签"""
        data = {
            "type": 11137,
            "data": {
                "label_name": label_name
            }
        }
        return self.send_sync(data)

    def delete_tag(self, label_id: int):
        """删除标签"""
        data = {
            "type": 11138,
            "data": {
                "label_id": label_id
            }
        }
        return self.send_sync(data)

    def modify_tag(self, label_id: int, label_name: str):
        """修改标签"""
        data = {
            "type": 11139,
            "data": {
                "label_id": label_id,
                "label_name": label_name
            }
        }
        return self.send(data)

    def add_tags_to_contact(self, wxid: str, label_id_list: str):
        """批量给用户加标签"""
        data = {
            "type": 11140,
            "data": {
                "wxid": wxid,
                "labelid_list": label_id_list
            }
        }
        return self.send_sync(data)

    def get_contact_tags(self, wxid):
        """获取联系人所有标签"""
        data = {
            "type": 11141,
            "data": {
                "wxid": wxid
            }
        }
        return self.send_sync(data)

    def voice_to_text(self, msg_id: str):
        """语音消息转文本"""
        data = {
            "type": 11112,
            "data": {
                "msgid": msg_id
            }
        }
        return self.send_sync(data)

    def open_chat(self, to_wxid: str):
        """切换当前会话"""
        data = {
            "type": 11090,
            "data": {
                "to_wxid": to_wxid
            }
        }
        return self.send(data)

    def clear_chat_history(self):
        """清除聊天记录"""
        data = {
            "type": 11108,
            "data": {}
        }
        return self.send(data)

    def set_disturb(self, wxid: str, status: int):
        """开启/关闭消息免打扰"""
        data = {
            "type": 11078,
            "data": {
                "wxid": wxid,
                "status": status
            }
        }
        return self.send_sync(data)

    def pin_chat(self, wxid: str, status: int):
        """置顶/取消置顶聊天"""
        data = {
            "type": 11079,
            "data": {
                "wxid": wxid,
                "status": status
            }
        }
        return self.send(data)

    def get_mini_program_code(self, appid: str):
        """获取小程序授权code"""
        data = {
            "type": 11136,
            "data": {
                "appid": appid
            }
        }
        return self.send_sync(data)

    def get_moments(self, max_id: str = "0"):
        """获取朋友圈"""
        data = {
            "type": 11145,
            "data": {
                "max_id": max_id
            }
        }
        return self.send_sync(data)

    def get_friend_moments(self, username, first_page_md5="", max_id: str = "0"):
        """获取好友朋友圈"""
        data = {
            "type": 11150,
            "data": {
                "username": username,
                "first_page_md5": first_page_md5,
                "max_id": max_id
            }
        }
        return self.send_sync(data)

    def comment_moment(self, object_id: str, content: str):
        """评论"""
        data = {
            "data": {
                "object_id": object_id,
                "content": content
            },
            "type": 11146
        }
        return self.send_sync(data)

    def like_moment(self, object_id: str):
        """点赞"""
        data = {
            "data": {
                "object_id": object_id
            },
            "type": 11147
        }
        return self.send_sync(data)

    def post_moment(self, object_desc: str):
        """发朋友圈"""
        data = {
            "type": 11148,
            "data": {
                "object_desc": object_desc
            }
        }
        return self.send_sync(data)

    def upload_image(self, image_path: str):
        """上传图片"""
        data = {
            "type": 11149,
            "data": {
                "path": image_path
            }
        }
        return self.send_sync(data)

    def init_video_account(self):
        """视频号初始化"""
        data = {
            "type": 11160,
            "data": {}
        }
        return self.send_sync(data)

    def search_video_account(self, query: str, scene: int, last_buff: str = ""):
        """视频号搜索"""
        data = {
            "type": 11161,
            "data": {
                "query": query,
                "last_buff": last_buff,
                "scene": scene
            }
        }
        return self.send_sync(data)

    def get_video_account_user_page(self, username: str, last_buff: str = ""):
        """视频号用户主页"""
        data = {
            "type": 11170,
            "data": {
                "username": username,
                "last_buff": last_buff
            }
        }
        return self.send_sync(data)

    def view_video_details(self, object_id: str, object_nonce_id: str, last_buff: str = ""):
        """查看视频详细信息(包含评论)"""
        data = {
            "type": 11169,
            "data": {
                "object_id": object_id,
                "object_nonce_id": object_nonce_id,
                "last_buff": last_buff
            }
        }
        return self.send_sync(data)

    def follow_video_blogger(self, username: str):
        """关注博主"""
        data = {
            "type": 11167,
            "data": {
                "username": username
            }
        }
        return self.send_sync(data)

    def like_video(self, object_id: str, object_nonce_id: str):
        """视频号点赞"""
        data = {
            "type": 11168,
            "data": {
                "object_id": object_id,
                "object_nonce_id": object_nonce_id
            }
        }
        return self.send_sync(data)

    def get_message_session_id(self, to_username: str, role_type: int):
        """获取私信sessionId"""
        data = {
            "type": 11202,
            "data": {
                "to_username": to_username,
                "roleType": role_type
            }
        }
        return self.send_sync(data)

    def send_private_message(self, to_username: str, session_id: str, content: str):
        """发送私信"""
        data = {
            "type": 11203,
            "data": {
                "to_username": to_username,
                "session_id": session_id,
                "content": content
            }
        }
        return self.send_sync(data)

    def create_virtual_nickname(self, nickname: str, head_img_url: str):
        """创建虚拟昵称"""
        data = {
            "type": 11194,
            "data": {
                "nickname": nickname,
                "headimg_url": head_img_url
            }
        }
        return self.send(data)

    def switch_virtual_nickname(self, role_type: int):
        """切换虚拟昵称"""
        data = {
            "type": 11195,
            "data": {
                "role_type": role_type
            }
        }
        return self.send(data)

    def delete_virtual_nickname(self):
        """删除虚拟昵称"""
        data = {
            "type": 11197,
            "data": {}
        }
        return self.send(data)

    def enter_live_room(self, object_id: str, live_id: str, object_nonce_id: str):
        """进入直播间"""
        data = {
            "type": 11162,
            "data": {
                "object_id": object_id,
                "live_id": live_id,
                "object_nonce_id": object_nonce_id
            }
        }
        return self.send_sync(data)

    def get_live_room_online_users(self, object_id: str, live_id: str, object_nonce_id: str):
        """获取直播间在线人员"""
        data = {
            "type": 11172,
            "data": {
                "object_id": object_id,
                "live_id": live_id,
                "object_nonce_id": object_nonce_id,
                "last_buff": ""
            }
        }
        return self.send_sync(data)

    def get_live_room_updates(self):
        """获取直播间变动信息(人气，实时发言等)"""
        data = {
            "type": 11163,
            "data": {}
        }
        return self.send_sync(data)

    def speak_in_live_room(self, content: str):
        """直播间发言"""
        data = {
            "type": 11164,
            "data": {
                "content": content
            }
        }
        return self.send_sync(data)

    def like_in_live_room(self, count):
        """直播间点赞"""
        data = {
            "type": 11185,
            "data": {
                "count": count
            }
        }
        return self.send_sync(data)

    def get_live_room_shelves(self, live_username: str, request_id: str):
        """获取直播间货架"""
        data = {
            "type": 11186,
            "data": {
                "live_username": live_username,
                "request_id": request_id
            }
        }
        return self.send_sync(data)

    def get_shelf_product_details(self, appid: str, request_id: str, product_id: str, real_appid: str,
                                  live_username: str):
        """获取货架商品详细信息"""
        data = {
            "type": 11187,
            "data": {
                "appid": appid,
                "request_id": request_id,
                "product_id": product_id,
                "live_username": live_username,
                "real_appid": real_appid
            }
        }
        return self.send_sync(data)

    def get_a8key(self, url: str, scene: int):
        """A8Key接口"""
        data = {
            "type": 11135,
            "data": {
                "url": url,
                "scene": scene
            }
        }
        return self.send_sync(data)

    def set_auto_accept_friend(self, auto: int):
        """自动同意好友申请"""
        data = {
            "type": 10081,
            "data": {
                "auto": auto
            }
        }
        return self.send(data)

    def set_auto_accept_wcpay(self, auto: int):
        """自动同意好友转账"""
        data = {
            "type": 10082,
            "data": {
                "auto": auto
            }
        }
        return self.send(data)

    def set_auto_accept_room(self, auto: int):
        """自动同意加群邀请"""
        data = {
            "type": 10083,
            "data": {
                "auto": auto
            }
        }
        return self.send(data)

    def set_auto_accept_card(self, auto: int):
        """自动加名片"""
        data = {
            "type": 10084,
            "data": {
                "auto": auto
            }
        }
        return self.send(data)

    def decode_image(self, src_file: str, dest_file: str):
        """解密图片"""
        data = {
            "type": 10085,
            "data": {
                "src_file": src_file,
                "dest_file": dest_file
            }
        }
        return self.send(data)

    def exec_sql(self, sql: str, db: int):
        """执行SQL命令"""
        data = {
            "type": 11027,
            "data": {
                "sql": sql,
                "db": db
            }
        }
        return self.send_sync(data)

    def search_contacts(self,
                        wxid: Union[None, str] = None,
                        account: Union[None, str] = None,
                        nickname: Union[None, str] = None,
                        remark: Union[None, str] = None,
                        fuzzy_search: bool = True):
        """
        根据wxid、微信号、昵称和备注模糊搜索联系人
        """
        conds = {}
        if wxid:
            conds["username"] = wxid
        if account:
            conds["alias"] = account
        if nickname:
            conds["nickname"] = nickname
        if remark:
            conds["remark"] = remark
        if not conds:
            return []

        cond_pairs = []
        tag = '%' if fuzzy_search else ''
        for k, v in conds.items():
            cond_pairs.append(f"{k} like '{tag}{v}{tag}'")

        cond_str = " or ".join(cond_pairs)
        sql = f"select username from contact where {cond_str}"
        message = self.exec_sql(sql, 1)
        if not message:
            return []

        result = message["result"]
        if not result:
            return []

        contacts = []
        for wxid_list in result:
            if len(wxid_list) > 0:
                wxid = wxid_list[0]
                contact = self.get_contact(wxid)
                contacts.append(contact)
        return contacts

    def get_room_name(self, room_wxid: str) -> str:
        """
        获取群名
        """
        sql = f"select nickname from contact where username='{room_wxid}'"
        result = self.sql_query(sql, 1)["result"]
        if result:
            return result[0][0]
        return ''
