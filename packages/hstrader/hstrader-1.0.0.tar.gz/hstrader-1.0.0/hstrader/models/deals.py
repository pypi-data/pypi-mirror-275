from .base import BaseModel
from .enums import *
from typing import Union

from .account import Account
from .symbol import Symbol


class Deal(BaseModel):
    account: Account = None
    account_id: int = None
    channel: int = None
    close_price: float = None
    closed_volume: float = None
    comment: str = None
    commission: float = None
    contract_size: float = None
    created_at: int = None
    created_by: int = None
    creation_method: int = None
    digits: float = None
    digits_currency: float = None
    direction: int = None
    external_id: str = None
    external_price: str = None
    external_volume: str = None
    id: int = None
    market_ask: float = None
    market_bid: float = None
    market_last: float = None
    open_price: float = None
    order_id: int = None
    position_id: int = None
    profit: float = None
    reason: int = None
    script_id: int = None
    side: int = None
    status: int = None
    stop_loss: float = None
    swap: float = None
    symbol: Symbol = None
    symbol_id: int = None
    take_profit: float = None
    updated_at: int = None
    updated_by: int = None
    volume: float = None
