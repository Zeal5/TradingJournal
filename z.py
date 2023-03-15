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
        "symbol": "average",
        "price": 21.721,
        "order_price": 21.721,
        "order_qty": 0.1,
        "exec_price": 20.687,
        "exec_qty": 0.1,
        "exec_value": 2.0687,
        "closed_size": 0,
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

for i in data:
    if 'closed_size' in i.keys():
        print('asd')