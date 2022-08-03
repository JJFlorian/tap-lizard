"""REST client handling, including lizardStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BasicAuthenticator


#SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class lizardStream(RESTStream):
    """lizard stream class."""


    url_base = "https://nens.lizard.net/api/v4/"

    # OR use a dynamic url_base:
    # @property
    # def url_base(self) -> str:
    #     """Return the API URL root, configurable via tap settings."""
    #     return self.config["api_url"]

    records_jsonpath = "$[results][*]"  # Or override `parse_response`.
    nextpage_jsonpath = "$.next"

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object."""
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config.get("username"),
            password=self.config.get("password"),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        nextpage_response = extract_jsonpath(
            self.nextpage_jsonpath, response.json()
        )
        nextpage_string = next(iter(nextpage_response), None)
        if nextpage_string is None:
            next_page_token = None
        else:
            next_page_token = nextpage_string.split("page=")[1]
            if "&" in next_page_token:
                next_page_token = int(next_page_token.split("&")[0])
            else:
                next_page_token = int(next_page_token)

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["page_size"] = 100
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["ordering"] = self.replication_key
            params[f"{self.replication_key}__gt"] = self.get_starting_replication_key_value(context)
        return params

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())


