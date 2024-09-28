import time
from dataclasses import dataclass
from functools import wraps
from typing import Any

import aiohttp
from utils import timeit


@dataclass(eq=False)
class Api:
    url: str
    api_key: str

    @staticmethod
    def get_json_body(
            api_key: str,
            model_name: str,
            called_method: str,
            method_properties: dict[str, Any] | None = None,
            **kwargs
    ) -> dict[str, Any]:
        json_body_raw = {
            'apiKey': api_key,
            "modelName": model_name,
            "calledMethod": called_method,
            "methodProperties": method_properties,
            **kwargs,
        }
        return json_body_raw

    async def _make_post_request(self, request_body: dict[str, Any]) -> list[dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.url, json=request_body) as response:
                return await response.json()

    @timeit
    async def get_areas(
            self,
            model_name: str = "AddressGeneral",
            called_method: str = "getAreas",
            method_properties: dict[str, Any] | None = None,
            **kwargs
    ):
        request_body = self.get_json_body(
            api_key=self.api_key,
            model_name=model_name,
            called_method=called_method,
            method_properties=method_properties,
            **kwargs
        )
        return await self._make_post_request(request_body=request_body)

    @timeit
    async def get_cities(
            self,
            model_name: str = "AddressGeneral",
            called_method: str = "getCities",
            method_properties: dict[str, Any] | None = None,
            **kwargs
    ):
        request_body = self.get_json_body(
            api_key=self.api_key,
            model_name=model_name,
            called_method=called_method,
            method_properties=method_properties,
            **kwargs
        )
        return await self._make_post_request(request_body=request_body)

    @timeit
    async def get_warehouses(
            self,
            model_name: str = "AddressGeneral",
            called_method: str = "getWarehouses",
            method_properties: dict[str, Any] | None = None,
            **kwargs
    ):
        request_body = self.get_json_body(
            api_key=self.api_key,
            model_name=model_name,
            called_method=called_method,
            method_properties=method_properties,
            **kwargs
        )
        return await self._make_post_request(request_body=request_body)

    async def get_city_warehouses(
            self,
            city_name: str
    ):
        return await self.get_warehouses(method_properties={"CityName": city_name})
