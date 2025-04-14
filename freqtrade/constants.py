# pragma pylint: disable=too-few-public-methods

"""
bot constants
"""

from typing import Any, Literal

from freqtrade.enums import CandleType, PriceType


DOCS_LINK = "https://www.freqtrade.io/en/stable"
DEFAULT_CONFIG = "config.json"
PROCESS_THROTTLE_SECS = 5  # sec
HYPEROPT_EPOCH = 100  # epochs
RETRY_TIMEOUT = 30  # sec
TIMEOUT_UNITS = ["minutes", "seconds"]
EXPORT_OPTIONS = ["none", "trades", "signals"]
DEFAULT_DB_PROD_URL = "sqlite:///tradesv3.sqlite"
DEFAULT_DB_DRYRUN_URL = "sqlite:///tradesv3.dryrun.sqlite"
UNLIMITED_STAKE_AMOUNT = "unlimited"
DEFAULT_AMOUNT_RESERVE_PERCENT = 0.05
REQUIRED_ORDERTIF = ["entry", "exit"]
REQUIRED_ORDERTYPES = ["entry", "exit", "stoploss", "stoploss_on_exchange"]
PRICING_SIDES = ["ask", "bid", "same", "other"]
ORDERTYPE_POSSIBILITIES = ["limit", "market"]
_ORDERTIF_POSSIBILITIES = ["GTC", "FOK", "IOC", "PO"]
ORDERTIF_POSSIBILITIES = _ORDERTIF_POSSIBILITIES + [t.lower() for t in _ORDERTIF_POSSIBILITIES]
STOPLOSS_PRICE_TYPES = [p for p in PriceType]
HYPEROPT_LOSS_BUILTIN = [
    "ShortTradeDurHyperOptLoss",
    "OnlyProfitHyperOptLoss",
    "SharpeHyperOptLoss",
    "SharpeHyperOptLossDaily",
    "SortinoHyperOptLoss",
    "SortinoHyperOptLossDaily",
    "CalmarHyperOptLoss",
    "MaxDrawDownHyperOptLoss",
    "MaxDrawDownRelativeHyperOptLoss",
    "MaxDrawDownPerPairHyperOptLoss",
    "ProfitDrawDownHyperOptLoss",
    "MultiMetricHyperOptLoss",
]
AVAILABLE_PAIRLISTS = [
    "StaticPairList",
    "VolumePairList",
    "PercentChangePairList",
    "ProducerPairList",
    "RemotePairList",
    "MarketCapPairList",
    "AgeFilter",
    "FullTradesFilter",
    "OffsetFilter",
    "PerformanceFilter",
    "PrecisionFilter",
    "PriceFilter",
    "RangeStabilityFilter",
    "ShuffleFilter",
    "SpreadFilter",
    "VolatilityFilter",
]
AVAILABLE_DATAHANDLERS = ["json", "jsongz", "feather", "parquet"]
BACKTEST_BREAKDOWNS = ["day", "week", "month", "year"]
BACKTEST_CACHE_AGE = ["none", "day", "week", "month"]
BACKTEST_CACHE_DEFAULT = "day"
DRY_RUN_WALLET = 1000
DATETIME_PRINT_FORMAT = "%Y-%m-%d %H:%M:%S"
MATH_CLOSE_PREC = 1e-14  # Precision used for float comparisons
DEFAULT_DATAFRAME_COLUMNS = ["date", "open", "high", "low", "close", "volume"]
# Don't modify sequence of DEFAULT_TRADES_COLUMNS
# it has wide consequences for stored trades files
DEFAULT_TRADES_COLUMNS = ["timestamp", "id", "type", "side", "price", "amount", "cost"]
DEFAULT_ORDERFLOW_COLUMNS = ["level", "bid", "ask", "delta"]
TRADES_DTYPES = {
    "timestamp": "int64",
    "id": "str",
    "type": "str",
    "side": "str",
    "price": "float64",
    "amount": "float64",
    "cost": "float64",
}
TRADING_MODES = ["spot", "margin", "futures"]
MARGIN_MODES = ["cross", "isolated", ""]

LAST_BT_RESULT_FN = ".last_result.json"
FTHYPT_FILEVERSION = "fthypt_fileversion"

USERPATH_HYPEROPTS = "hyperopts"
USERPATH_STRATEGIES = "strategies"
USERPATH_NOTEBOOKS = "notebooks"
USERPATH_FREQAIMODELS = "freqaimodels"

TELEGRAM_SETTING_OPTIONS = ["on", "off", "silent"]
WEBHOOK_FORMAT_OPTIONS = ["form", "json", "raw"]
FULL_DATAFRAME_THRESHOLD = 100
CUSTOM_TAG_MAX_LENGTH = 255
DL_DATA_TIMEFRAMES = ["1m", "5m"]

ENV_VAR_PREFIX = "FREQTRADE__"

CANCELED_EXCHANGE_STATES = ("cancelled", "canceled", "expired", "rejected")
NON_OPEN_EXCHANGE_STATES = (*CANCELED_EXCHANGE_STATES, "closed")

# Define decimals per coin for outputs
# Only used for outputs.
DECIMAL_PER_COIN_FALLBACK = 3  # Should be low to avoid listing all possible FIAT's
DECIMALS_PER_COIN = {
    "BTC": 8,
    "ETH": 5,
}

DUST_PER_COIN = {"BTC": 0.0001, "ETH": 0.01}

# Source files with destination directories within user-directory
USER_DATA_FILES = {
    "sample_strategy.py": USERPATH_STRATEGIES,
    "sample_hyperopt_loss.py": USERPATH_HYPEROPTS,
    "strategy_analysis_example.ipynb": USERPATH_NOTEBOOKS,
}

SUPPORTED_FIAT = [
    "AUD",
    "BRL",
    "CAD",
    "CHF",
    "CLP",
    "CNY",
    "CZK",
    "DKK",
    "EUR",
    "GBP",
    "HKD",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "JPY",
    "KRW",
    "MXN",
    "MYR",
    "NOK",
    "NZD",
    "PHP",
    "PKR",
    "PLN",
    "RUB",
    "UAH",
    "SEK",
    "SGD",
    "THB",
    "TRY",
    "TWD",
    "ZAR",
    "USD",
    "BTC",
    "ETH",
    "XRP",
    "LTC",
    "BCH",
    "BNB",
    "",  # Allow empty field in config.
]

MINIMAL_CONFIG = {
    "stake_currency": "",
    "dry_run": True,
    "exchange": {
        "name": "",
        "key": "",
        "secret": "",
        "pair_whitelist": [],
        "ccxt_async_config": {},
    },
}


CANCEL_REASON = {
    "TIMEOUT": "因超时而取消",
    "PARTIALLY_FILLED_KEEP_OPEN": "部分成交 - 保持订单开放",
    "PARTIALLY_FILLED": "部分成交",
    "FULLY_CANCELLED": "完全取消",
    "ALL_CANCELLED": "已取消(所有未成交和部分成交的开放订单已取消)",
    "CANCELLED_ON_EXCHANGE": "在交易所取消",
    "FORCE_EXIT": "强制卖出",
    "REPLACE": "取消以替换为新的限价订单",
    "REPLACE_FAILED": "替换订单失败, 删除交易",
    "USER_CANCEL": "用户请求取消订单",
}

# List of pairs with their timeframes
PairWithTimeframe = tuple[str, str, CandleType]
ListPairsWithTimeframes = list[PairWithTimeframe]

# Type for trades list
TradeList = list[list]
# ticks, pair, timeframe, CandleType
TickWithTimeframe = tuple[str, str, CandleType, int | None, int | None]
ListTicksWithTimeframes = list[TickWithTimeframe]

LongShort = Literal["long", "short"]
EntryExit = Literal["entry", "exit"]
BuySell = Literal["buy", "sell"]
MakerTaker = Literal["maker", "taker"]
BidAsk = Literal["bid", "ask"]
OBLiteral = Literal["asks", "bids"]

Config = dict[str, Any]
# Exchange part of the configuration.
ExchangeConfig = dict[str, Any]
IntOrInf = float


EntryExecuteMode = Literal["initial", "pos_adjust", "replace"]
