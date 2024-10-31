import json
import time
from collections import defaultdict
from functools import wraps
from operator import itemgetter
from typing import Any


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{func.__name__} took {total_time:.5f} s')
        return result
    return timeit_wrapper


class Utils:

    @staticmethod
    @timeit
    def write_to_file_json(file_to_write, name_of_file: str):
        with open(f'../{name_of_file}.json', 'w', encoding="UTF-8") as outfile:
            outfile.write(json.dumps(file_to_write, indent=4, ensure_ascii=False))

    @staticmethod
    def _get_item_description(dictionary: dict[str, Any]) -> list[str]:
        return [item.get("Description") for item in dictionary.get("data")]

    @timeit
    def get_list_of_areas(self, areas: dict[str, Any]) -> list[str]:
        return self._get_item_description(dictionary=areas)

    @staticmethod
    @timeit
    def get_cities_with_areas(cities: dict[str, Any]) -> dict[str, Any]:
        cities_with_areas = defaultdict(list)
        for item in cities.get("data"):
            cities_with_areas[item.get("AreaDescription")].append(item.get("Description"))
        return cities_with_areas

    @timeit
    def get_list_of_names_of_city_warehouses(self, warehouses: list[dict[str, Any]]) -> list[str]:
        return self._get_item_description(dictionary=warehouses[0])

    @staticmethod
    @timeit
    def get_warehouses_with_cities(warehouses: dict[str, Any]) -> dict[str, Any]:
        warehouses_by_city = defaultdict(list)
        for item in warehouses.get("data"):
            warehouses_by_city[item.get("CityDescription")].append(item.get("Description"))

        return warehouses_by_city

    @staticmethod
    @timeit
    def build_final_result(areas: list[str], cities: dict[str, Any], warehouses: dict[str, Any]):
        result = defaultdict(dict)

        for area in areas:
            for city_description in cities.get(area, []):
                result[area][city_description] = warehouses.get(city_description, [])

        return result
