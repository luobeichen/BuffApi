from typing import Optional, Dict, Any

class LeaderboardConfig:
    def __init__(self, csgo: bool, dota2: bool):
        self.csgo = csgo
        self.dota2 = dota2

    @classmethod
    def from_dict(cls, data: Dict[str, bool]) -> "LeaderboardConfig":
        return cls(csgo=data.get("csgo", False), dota2=data.get("dota2", False))


class SteamAssetConfig:
    def __init__(self, csgo: bool, dota2: bool):
        self.csgo = csgo
        self.dota2 = dota2

    @classmethod
    def from_dict(cls, data: Dict[str, bool]) -> "SteamAssetConfig":
        return cls(csgo=data.get("csgo", False), dota2=data.get("dota2", False))


class info:
    def __init__(
        self,

        # 用户基本信息
        id: str,                    # 用户ID
        nickname: str,              # 用户昵称
        avatar: str,                # 用户头像
        mobile: str,                # 手机号码
        steamid: str,               # Steam ID
        is_need_steam_verify: bool, # 是否需要Steam验证
        login_from: int,            # 登录来源
        is_new: bool,               # 是否是新用户
        partner_role_info: Dict[str, Any],  # 合作角色信息
        trade_url: str,             # 交易链接
        trade_url_state: int,       # 交易链接状态
        is_foreigner: bool,         # 是否为外国用户
        nickname_remaining: int,    # 昵称剩余修改次数
        can_unbind_steam: bool,     # 是否可以解绑Steam
        allow_nickname_sign: bool,  # 是否允许昵称签名
        allow_epay: bool,           # 是否允许电子支付
        allow_pubg_recycle: bool,
        seller_exam_state: int,
        buyer_exam_state: int,
        allow_comment_push: bool,
        allow_up_push: bool,
        allow_buyer_bargain: bool,
        allow_buyer_bargain_chat: bool,
        allow_shop_display: bool,
        language: str,
        steam_price_currency: str,
        steam_price_currency_desc: str,
        buff_price_currency: str,
        buff_price_currency_desc: str,
        buff_price_currency_symbol: str,
        buff_price_currency_rate_base_cny: float,
        buff_price_currency_rate_base_usd: float,
        inventory_price: str,
        allow_wechat_trade_message: bool,
        force_buyer_send_offer: bool,
        allow_price_change_notify: bool,
        allow_sms_notification: bool,
        allow_mail_notification: bool,
        allow_item_recommendation: bool,
        allow_buyer_notify_delivery_by_call: bool,
        allow_bargain_rejected_push: bool,
        allow_deliver_push: bool,
        allow_bargain_chat_message_push: bool,
        allow_auction_push: bool,
        allow_social_comment: bool,
        allow_feedback_new_entry: bool,
        allow_image_search: bool,
        allow_export_bill_order: bool,
        allow_preview_audit: bool,
        allow_preview_recommend: bool,
        allow_csgo_trade_up: bool,
        allow_csgo_trade_up_community: bool,
        is_premium: bool,
        allow_purchase_premium: bool,
        allow_multi_steamid: bool,
        show_leaderboard: LeaderboardConfig,
        show_leaderboard_v2: LeaderboardConfig,
        show_steam_asset_remark: SteamAssetConfig,
        show_steam_asset_buy_price: SteamAssetConfig,
        allow_auto_remark: bool,
        partner_role_detail: Dict[str, Any],
        steam_api_key_state: int,
        code: str = "ERROR",
        msg: Optional[str] = None
    ):
        self.code = code
        self.msg = msg
        self.id = id
        self.nickname = nickname
        self.avatar = avatar
        self.mobile = mobile
        self.steamid = steamid
        self.is_need_steam_verify = is_need_steam_verify
        self.login_from = login_from
        self.is_new = is_new
        self.partner_role_info = partner_role_info
        self.trade_url = trade_url
        self.trade_url_state = trade_url_state
        self.is_foreigner = is_foreigner
        self.nickname_remaining = nickname_remaining
        self.can_unbind_steam = can_unbind_steam
        self.allow_nickname_sign = allow_nickname_sign
        self.allow_epay = allow_epay
        self.allow_pubg_recycle = allow_pubg_recycle
        self.seller_exam_state = seller_exam_state
        self.buyer_exam_state = buyer_exam_state
        self.allow_comment_push = allow_comment_push
        self.allow_up_push = allow_up_push
        self.allow_buyer_bargain = allow_buyer_bargain
        self.allow_buyer_bargain_chat = allow_buyer_bargain_chat
        self.allow_shop_display = allow_shop_display
        self.language = language
        self.steam_price_currency = steam_price_currency
        self.steam_price_currency_desc = steam_price_currency_desc
        self.buff_price_currency = buff_price_currency
        self.buff_price_currency_desc = buff_price_currency_desc
        self.buff_price_currency_symbol = buff_price_currency_symbol
        self.buff_price_currency_rate_base_cny = buff_price_currency_rate_base_cny
        self.buff_price_currency_rate_base_usd = buff_price_currency_rate_base_usd
        self.inventory_price = inventory_price
        self.allow_wechat_trade_message = allow_wechat_trade_message
        self.force_buyer_send_offer = force_buyer_send_offer
        self.allow_price_change_notify = allow_price_change_notify
        self.allow_sms_notification = allow_sms_notification
        self.allow_mail_notification = allow_mail_notification
        self.allow_item_recommendation = allow_item_recommendation
        self.allow_buyer_notify_delivery_by_call = allow_buyer_notify_delivery_by_call
        self.allow_bargain_rejected_push = allow_bargain_rejected_push
        self.allow_deliver_push = allow_deliver_push
        self.allow_bargain_chat_message_push = allow_bargain_chat_message_push
        self.allow_auction_push = allow_auction_push
        self.allow_social_comment = allow_social_comment
        self.allow_feedback_new_entry = allow_feedback_new_entry
        self.allow_image_search = allow_image_search
        self.allow_export_bill_order = allow_export_bill_order
        self.allow_preview_audit = allow_preview_audit
        self.allow_preview_recommend = allow_preview_recommend
        self.allow_csgo_trade_up = allow_csgo_trade_up
        self.allow_csgo_trade_up_community = allow_csgo_trade_up_community
        self.is_premium = is_premium
        self.allow_purchase_premium = allow_purchase_premium
        self.allow_multi_steamid = allow_multi_steamid
        self.show_leaderboard = show_leaderboard
        self.show_leaderboard_v2 = show_leaderboard_v2
        self.show_steam_asset_remark = show_steam_asset_remark
        self.show_steam_asset_buy_price = show_steam_asset_buy_price
        self.allow_auto_remark = allow_auto_remark
        self.partner_role_detail = partner_role_detail
        self.steam_api_key_state = steam_api_key_state

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "info":
        user_data = data.get("data", {})
        return cls(
            code=data.get("code", "ERROR"),
            msg=data.get("msg"),
            id=user_data["id"],
            nickname=user_data["nickname"],
            avatar=user_data["avatar"],
            mobile=user_data["mobile"],
            steamid=user_data["steamid"],
            is_need_steam_verify=user_data["is_need_steam_verify"],
            login_from=user_data["login_from"],
            is_new=user_data["is_new"],
            partner_role_info=user_data.get("partner_role_info", {}),
            trade_url=user_data["trade_url"],
            trade_url_state=user_data["trade_url_state"],
            is_foreigner=user_data["is_foreigner"],
            nickname_remaining=user_data["nickname_remaining"],
            can_unbind_steam=user_data["can_unbind_steam"],
            allow_nickname_sign=user_data["allow_nickname_sign"],
            allow_epay=user_data["allow_epay"],
            allow_pubg_recycle=user_data["allow_pubg_recycle"],
            seller_exam_state=user_data["seller_exam_state"],
            buyer_exam_state=user_data["buyer_exam_state"],
            allow_comment_push=user_data["allow_comment_push"],
            allow_up_push=user_data["allow_up_push"],
            allow_buyer_bargain=user_data["allow_buyer_bargain"],
            allow_buyer_bargain_chat=user_data["allow_buyer_bargain_chat"],
            allow_shop_display=user_data["allow_shop_display"],
            language=user_data["language"],
            steam_price_currency=user_data["steam_price_currency"],
            steam_price_currency_desc=user_data["steam_price_currency_desc"],
            buff_price_currency=user_data["buff_price_currency"],
            buff_price_currency_desc=user_data["buff_price_currency_desc"],
            buff_price_currency_symbol=user_data["buff_price_currency_symbol"],
            buff_price_currency_rate_base_cny=user_data["buff_price_currency_rate_base_cny"],
            buff_price_currency_rate_base_usd=user_data["buff_price_currency_rate_base_usd"],
            inventory_price=user_data["inventory_price"],
            allow_wechat_trade_message=user_data["allow_wechat_trade_message"],
            force_buyer_send_offer=user_data["force_buyer_send_offer"],
            allow_price_change_notify=user_data["allow_price_change_notify"],
            allow_sms_notification=user_data["allow_sms_notification"],
            allow_mail_notification=user_data["allow_mail_notification"],
            allow_item_recommendation=user_data["allow_item_recommendation"],
            allow_buyer_notify_delivery_by_call=user_data["allow_buyer_notify_delivery_by_call"],
            allow_bargain_rejected_push=user_data["allow_bargain_rejected_push"],
            allow_deliver_push=user_data["allow_deliver_push"],
            allow_bargain_chat_message_push=user_data["allow_bargain_chat_message_push"],
            allow_auction_push=user_data["allow_auction_push"],
            allow_social_comment=user_data["allow_social_comment"],
            allow_feedback_new_entry=user_data["allow_feedback_new_entry"],
            allow_image_search=user_data["allow_image_search"],
            allow_export_bill_order=user_data["allow_export_bill_order"],
            allow_preview_audit=user_data["allow_preview_audit"],
            allow_preview_recommend=user_data["allow_preview_recommend"],
            allow_csgo_trade_up=user_data["allow_csgo_trade_up"],
            allow_csgo_trade_up_community=user_data["allow_csgo_trade_up_community"],
            is_premium=user_data["is_premium"],
            allow_purchase_premium=user_data["allow_purchase_premium"],
            allow_multi_steamid=user_data["allow_multi_steamid"],
            show_leaderboard=LeaderboardConfig.from_dict(user_data["show_leaderboard"]),
            show_leaderboard_v2=LeaderboardConfig.from_dict(user_data["show_leaderboard_v2"]),
            show_steam_asset_remark=SteamAssetConfig.from_dict(user_data["show_steam_asset_remark"]),
            show_steam_asset_buy_price=SteamAssetConfig.from_dict(user_data["show_steam_asset_buy_price"]),
            allow_auto_remark=user_data["allow_auto_remark"],
            partner_role_detail=user_data.get("partner_role_detail", {}),
            steam_api_key_state=user_data["steam_api_key_state"]
        )