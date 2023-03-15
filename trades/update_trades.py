from pybit import usdt_perpetual
import pybit.exceptions
import logging
from pprint import pprint

########
from dotenv import dotenv_values

config = dotenv_values(".env")
###########
# stop imported moduels from logging
logging.getLogger().setLevel(logging.WARNING)
for handler in logging.getLogger().handlers:
    handler.setLevel(logging.WARNING)


# logging.basicConfig(
#     level=logging.INFO,
#     filename="Live_Positions.log",
#     format="%(levelname)s - %(asctime)s -  %(message)s",
#     datefmt="%m-%d %H:%M:%S",
# )
# initiate custom moduel
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("Live_Positions.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Orders:
    """Creates an Instance for all accounts \n\n
    name = account name\n
    long/short_tp == is actuall price for tps\n
    stop_loss is in% term from entries is fixed for all entries"""

    def __init__(
        self,
        name,
        api_key: str,
        api_secret: str,
    ):
        self.session = usdt_perpetual.HTTP(
            endpoint="https://api.bybit.com", api_key=api_key, api_secret=api_secret
        )
        self.ws = usdt_perpetual.WebSocket(
            test=False, api_key=api_secret, api_secret=api_secret
        )

        self.name = str(name)
        logger.info(f"{self.name} account initiated")

    def __str__(self) -> str:
        return f"Account {(self.name).upper()}"

