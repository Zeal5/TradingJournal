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
        'order_id': 'f07a0f2d-9c10-4edb-9d69-88a00c1a164e'
    },
        {
        "side": "Buy",
        "symbol": "average",
        "price": 21.721,
        "order_price": 21.721,
        "order_qty": 0.1,
        "exec_price": 20.687,
        "exec_qty": 0.1,
        "exec_value": 2.0687,
        "closed_size": 0,
        'order_id': '191427ac-15f6-45c4-87af-076eb7c408b8'
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
        'order_id': '191427ac-15f6-45c4-87af-076eb7c408b8'
    },
]
trade_counter = 1
buy_trade_histry = []
sell_trade_histry = []
buy_qty = 0
sell_qty = 0
for trade in reversed(data):
    if trade["closed_size"] != 0:
        if trade["side"] == "Sell":
            buy_trade_histry[-1].append({"exit": trade})
            buy_qty -= trade["closed_size"]

        if trade["side"] == "Buy":
            buy_trade_histry[-1].append({"exit": trade})
            sell_qty -= trade["closed_size"]

    else:
        if trade["closed_size"] == 0 :
            if trade["side"] == "Buy" and buy_qty == 0:
                buy_trade_histry.append([{"long_entry": trade}])
                buy_qty += trade["exec_qty"]

            if trade["side"] == "Sell" and sell_qty == 0:
                sell_trade_histry.append([{"short_entry": trade}])
                sell_qty += trade["exec_qty"]

        if trade["closed_size"] == 0: #average into trades
            for i in buy_trade_histry:
                for l in i:
                    for c in l.values():
                        if trade['order_id'] in c.values():
                            print('yessssssss')
            if trade["side"] == "Buy" and buy_qty != 0:
                buy_trade_histry.append([{"long_entry": trade}])
                buy_qty += trade["exec_qty"]

            if trade["side"] == "Sell" and sell_qty != 0:
                sell_trade_histry.append([{"short_entry": trade}])
                sell_qty += trade["exec_qty"]



print(buy_trade_histry)


# print(trade_histry)


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
# json_data = Orders("A").trade_records("SOLUSDT")["result"]["data"]
# print(json_data)

# df = pd.json_normalize(data)
# print(df)
