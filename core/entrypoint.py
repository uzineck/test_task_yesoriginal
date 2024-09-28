from api import Api
from config import API_KEY
import asyncio

from utils import Utils

base_url = 'https://api.novaposhta.ua/v2.0/json/'

api = Api(url=base_url, api_key=API_KEY)

utils = Utils()

task_in_dict = utils.build_final_result(
    areas=utils.get_list_of_areas(areas=asyncio.run(api.get_areas())),
    cities=utils.get_cities_with_areas(cities=asyncio.run(api.get_cities())),
    warehouses=utils.get_warehouses_with_cities(warehouses=asyncio.run(api.get_warehouses()))
)


