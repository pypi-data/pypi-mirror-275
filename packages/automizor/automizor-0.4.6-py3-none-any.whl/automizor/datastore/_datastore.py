from typing import Dict, List, Union

import requests

from automizor.exceptions import AutomizorError
from automizor.utils import get_api_config, get_headers

JSON = Union[str, int, float, bool, None, Dict[str, "JSON"], List["JSON"]]


class DataStore:
    """
    `DataStore` is a class designed to interface with the `Automizor Platform` to manage and
    manipulate data stored in various formats. It supports operations to retrieve and update
    data using a unified API.

    The class initializes an HTTP session with the necessary headers for authentication, and
    provides methods to retrieve values, and set values in the store.

    Attributes:
        url (str): The base URL for the API endpoint.
        token (str): The authentication token for API access.
        session (requests.Session): The HTTP session used for making API requests.
    """

    def __init__(self):
        self.url, self.token = get_api_config()
        self.session = requests.Session()
        self.session.headers.update(get_headers(self.token))

    def get_values(
        self,
        name: str,
        primary_key: str | None = None,
        secondary_key: str | None = None,
    ) -> JSON:
        """
        Retrieves values from the specified data store.

        Parameters:
            name (str): The name of the data store.
            primary_key (str, optional): The primary key for the values. Defaults to None.
            secondary_key (str, optional): The secondary key for the values. Defaults to None.

        Returns:
            JSON: The values from the data store.
        """

        return self._get_values(name, primary_key, secondary_key)

    def set_values(self, name: str, values: JSON) -> None:
        """
        Sets values in the specified data store.

        Parameters:
            name (str): The name of the data store.
            values (JSON): The values to set in the data store.
        """

        return self._set_values(name, values)

    def _get_values(
        self,
        name: str,
        primary_key: str | None = None,
        secondary_key: str | None = None,
    ) -> dict:
        params = (
            {"primary_key": primary_key, "secondary_key": secondary_key}
            if primary_key or secondary_key
            else {}
        )
        url = f"https://{self.url}/api/v1/workflow/datastore/{name}/values/"
        try:
            response = self.session.get(url, timeout=10, params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as exc:
            raise AutomizorError.from_response(
                exc.response, "Failed to get datastore values"
            ) from exc
        except Exception as exc:
            raise AutomizorError("Failed to get datastore values") from exc

    def _set_values(self, name: str, values: JSON) -> None:
        url = f"https://{self.url}/api/v1/workflow/datastore/{name}/values/"
        try:
            response = self.session.post(url, json=values, timeout=10)
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise AutomizorError.from_response(
                exc.response, "Failed to set datastore values"
            ) from exc
        except Exception as exc:
            raise AutomizorError("Failed to set datastore values") from exc
