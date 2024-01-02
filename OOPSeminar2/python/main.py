from Classes.market import Market
from Classes.ordinary_client import OrdinaryClient
from Classes.special_client import SpecialClient
from Classes.tax_inspector import TaxInspector
from Classes.promo_client import PromoClient


magnit = Market()

client1 = OrdinaryClient("boris")
client2 = SpecialClient("prezident", 1)
client3 = TaxInspector()
promo_client = PromoClient("Anna", "11.11", 1)

magnit.acceptToMarket(client1)
magnit.acceptToMarket(client2)
magnit.acceptToMarket(client3)
magnit.acceptToMarket(promo_client)

magnit.update()

promo_client.initiate_return(123)
promo_client.check_return_status(123)