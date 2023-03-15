from pybit import usdt_perpetual
import pybit.exceptions
from pprint import pprint
import pandas as pd

########
from dotenv import dotenv_values

config = dotenv_values("trades\.env")
###########
data = [
    {
        "side": "Sell",
        "symbol": "SOLUSDT",
        "price": 19.662,
        "order_price": 19.662,
        "order_qty": 0.1,
        "exec_price": 20.696,
        "exec_qty": 0.1,
        "exec_value": 2.0696,
        "closed_size": 0.1,
    },
    {
        "side": "Buy",
        "symbol": "SOLUSDT",
        "price": 21.721,
        "order_price": 21.721,
        "order_qty": 0.1,
        "exec_price": 20.687,
        "exec_qty": 0.1,
        "exec_value": 2.0687,
        "closed_size": 0,

    },
]


class Orders:
    """Creates an Instance for all accounts \n\n
    name = account name\n
    long/short_tp == is actuall price for tps\n
    stop_loss is in% term from entries is fixed for all entries"""

    def __init__(
        self,
        name,
        api_key: str = None,
        api_secret: str = None,
    ):
        self.session = usdt_perpetual.HTTP(
            endpoint="https://api.bybit.com",
            api_key=config["A1"],
            api_secret=config["S1"],  # api_key=api_key, api_secret=api_secret
        )
        self.name = str(name)

    def __str__(self) -> str:
        return f"Account {(self.name).upper()}"

    def trade_records(self, ticker):
        records = self.session.user_trade_records(symbol=ticker)
        return records


# sol matic xrp
# json_data = Orders("A").trade_records("MATICUSDT")["result"]["data"]
# print(json_data)

# df = pd.json_normalize(data)
# print(df)