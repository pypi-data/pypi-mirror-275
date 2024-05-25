import dataclasses
from decimal import (
    Decimal,
)
import typing

import httpx

from .exceptions import (
    InvalidKey,
    NothingFound,
    UnexpectedResponse,
)

__all__ = ("Client",)


@dataclasses.dataclass
class Client:
    """Yandex geocoder API client.

    :Example:
        >>> from yandex_geocoder import Client
        >>> client = Client("your-api-key")

        >>> coordinates = client.coordinates("Москва Льва Толстого 16")
        >>> assert coordinates == (Decimal("37.587093"), Decimal("55.733969"))

        >>> address = client.address(Decimal("37.587093"), Decimal("55.733969"))
        >>> assert address == "Россия, Москва, улица Льва Толстого, 16"

    """

    __slots__ = ("api_key",)

    api_key: str

    def _request(self, address: str) -> dict[str, typing.Any]:
        """Make a synchronous request to the Yandex Geocoder API."""
        with httpx.Client() as client:
            response = client.get(
                "https://geocode-maps.yandex.ru/1.x/",
                params={"format": "json", "apikey": self.api_key, "geocode": address},
            )
        return self.__handle_response(response)

    async def _arequest(self, address: str) -> dict[str, typing.Any]:
        """Make an asynchronous request to the Yandex Geocoder API."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://geocode-maps.yandex.ru/1.x/",
                params={"format": "json", "apikey": self.api_key, "geocode": address},
            )
        return self.__handle_response(response)

    @staticmethod
    def __handle_response(response: httpx.Response) -> dict[str, typing.Any]:
        """Handle the API response."""
        if response.status_code == 200:
            return response.json()["response"]
        elif response.status_code == 403:
            raise InvalidKey("Invalid API key.")
        else:
            raise UnexpectedResponse(
                f"Unexpected response: status_code={response.status_code}, body={response.content!r}"
            )

    def coordinates(self, address: str) -> tuple[Decimal, ...]:
        """Fetch coordinates (longitude, latitude) for passed address."""
        data = self._request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        coordinates: str = data[0]["GeoObject"]["Point"]["pos"]
        longitude, latitude = tuple(coordinates.split(" "))

        return Decimal(longitude), Decimal(latitude)

    async def aiocoordinates(self, address: str) -> tuple[Decimal, ...]:
        """Fetch coordinates (longitude, latitude) for passed address."""
        d = await self._arequest(address)
        data = d["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        coordinates = data[0]["GeoObject"]["Point"]["pos"]
        longitude, latitude = tuple(coordinates.split(" "))
        return Decimal(longitude), Decimal(latitude)

    def address(self, longitude: Decimal, latitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        data = self._request(f"{longitude},{latitude}")["GeoObjectCollection"][
            "featureMember"
        ]

        if not data:
            raise NothingFound(f'Nothing found for "{longitude} {latitude}"')

        got: str = data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
        return got

    async def aioaddress(self, longitude: Decimal, latitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        response = await self._arequest(f"{longitude},{latitude}")
        data = response.get("GeoObjectCollection", {}).get("featureMember", [])

        if not data:
            raise NothingFound(f'Nothing found for "{longitude} {latitude}"')

        address_details: str = data[0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"
        ]["text"]
        return address_details
