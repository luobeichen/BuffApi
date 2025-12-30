from typing import Optional, Dict, Any

class RemainWithdrawCounts:
    def __init__(self, epay: int, alipay: int, together: int, airwallex: int, payoneer: int):
        self.epay = epay
        self.alipay = alipay
        self.together = together
        self.airwallex = airwallex
        self.payoneer = payoneer

    @classmethod
    def from_dict(cls, data: Dict[str, int]) -> "RemainWithdrawCounts":
        return cls(
            epay=data.get("epay", 0),
            alipay=data.get("alipay", 0),
            together=data.get("together", 0),
            airwallex=data.get("airwallex", 0),
            payoneer=data.get("payoneer", 0)
        )


class AssetGetBriefAsset:
    def __init__(
        self,
        cash_amount: str,
        cash_amount_outer: str,
        cash_amount_inner: str,
        frozen_amount: str,
        security_amount: str,
        epay_amount: str,
        epay_able_withdraw_amount: str,
        epay_unable_withdraw_amount: str,
        epay_frozen_amount: str,
        alipay_amount: str,
        alipay_able_withdraw_amount: str,
        alipay_unable_withdraw_amount: str,
        alipay_frozen_amount: str,
        realname: bool,
        remain_withdraw_counts: RemainWithdrawCounts,
        has_admin_frozen_asset: bool,
        allow_large_amount_withdraw: bool,
        allow_large_amount_withdraw_new: bool,
        ejzb_auth: Optional[Any],
        alipay_refund_info: Optional[Any],
        pending_divide_amount: str,
        pending_divide_alipay_amount_total: str,
        pending_divide_epay_amount_total: str,
        pending_divide_amount_using: str,
        pending_divide_epay_amount_enable: str,
        pending_divide_alipay_amount_enable: str,
        code: str = "OK",
        msg: Optional[str] = None
    ):
        self.code = code
        self.msg = msg
        self.cash_amount = cash_amount
        self.cash_amount_outer = cash_amount_outer
        self.cash_amount_inner = cash_amount_inner
        self.frozen_amount = frozen_amount
        self.security_amount = security_amount
        self.epay_amount = epay_amount
        self.epay_able_withdraw_amount = epay_able_withdraw_amount
        self.epay_unable_withdraw_amount = epay_unable_withdraw_amount
        self.epay_frozen_amount = epay_frozen_amount
        self.alipay_amount = alipay_amount
        self.alipay_able_withdraw_amount = alipay_able_withdraw_amount
        self.alipay_unable_withdraw_amount = alipay_unable_withdraw_amount
        self.alipay_frozen_amount = alipay_frozen_amount
        self.realname = realname
        self.remain_withdraw_counts = remain_withdraw_counts
        self.has_admin_frozen_asset = has_admin_frozen_asset
        self.allow_large_amount_withdraw = allow_large_amount_withdraw
        self.allow_large_amount_withdraw_new = allow_large_amount_withdraw_new
        self.ejzb_auth = ejzb_auth
        self.alipay_refund_info = alipay_refund_info
        self.pending_divide_amount = pending_divide_amount
        self.pending_divide_alipay_amount_total = pending_divide_alipay_amount_total
        self.pending_divide_epay_amount_total = pending_divide_epay_amount_total
        self.pending_divide_amount_using = pending_divide_amount_using
        self.pending_divide_epay_amount_enable = pending_divide_epay_amount_enable
        self.pending_divide_alipay_amount_enable = pending_divide_alipay_amount_enable

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AssetGetBriefAsset":
        asset_data = data.get("data", {})
        return cls(
            code=data.get("code", "ERROR"),
            msg=data.get("msg"),
            cash_amount=asset_data["cash_amount"],
            cash_amount_outer=asset_data["cash_amount_outer"],
            cash_amount_inner=asset_data["cash_amount_inner"],
            frozen_amount=asset_data["frozen_amount"],
            security_amount=asset_data["security_amount"],
            epay_amount=asset_data["epay_amount"],
            epay_able_withdraw_amount=asset_data["epay_able_withdraw_amount"],
            epay_unable_withdraw_amount=asset_data["epay_unable_withdraw_amount"],
            epay_frozen_amount=asset_data["epay_frozen_amount"],
            alipay_amount=asset_data["alipay_amount"],
            alipay_able_withdraw_amount=asset_data["alipay_able_withdraw_amount"],
            alipay_unable_withdraw_amount=asset_data["alipay_unable_withdraw_amount"],
            alipay_frozen_amount=asset_data["alipay_frozen_amount"],
            realname=asset_data["realname"],
            remain_withdraw_counts=RemainWithdrawCounts.from_dict(asset_data["remain_withdraw_counts"]),
            has_admin_frozen_asset=asset_data["has_admin_frozen_asset"],
            allow_large_amount_withdraw=asset_data["allow_large_amount_withdraw"],
            allow_large_amount_withdraw_new=asset_data["allow_large_amount_withdraw_new"],
            ejzb_auth=asset_data.get("ejzb_auth"),
            alipay_refund_info=asset_data.get("alipay_refund_info"),
            pending_divide_amount=asset_data["pending_divide_amount"],
            pending_divide_alipay_amount_total=asset_data["pending_divide_alipay_amount_total"],
            pending_divide_epay_amount_total=asset_data["pending_divide_epay_amount_total"],
            pending_divide_amount_using=asset_data["pending_divide_amount_using"],
            pending_divide_epay_amount_enable=asset_data["pending_divide_epay_amount_enable"],
            pending_divide_alipay_amount_enable=asset_data["pending_divide_alipay_amount_enable"]
        )