import os
from typing import Optional

import argilla as rg
from dotenv import load_dotenv

load_dotenv()


class SDKConnection:

    client = None

    def __init__(
        self, api_url: Optional[str] = None, api_key: Optional[str] = None, **kwargs
    ):

        self.api_url = api_url or os.getenv("ARGILLA_API_URL")
        self.api_key = api_key or os.getenv("ARGILLA_API_KEY")

        self._initialize_connection(**kwargs)

    def _initialize_connection(self, **kwargs):
        """
        Initialize the connection to the Argilla API.
        """
        if not self.api_url:
            raise ValueError("ARGILLA_API_URL is not set in the environment variables")
        if not self.api_key:
            raise ValueError("ARGILLA_API_KEY is not set in the environment variables")

        self.client = rg.Argilla(api_url=self.api_url, api_key=self.api_key, **kwargs)

    def get_client(self):
        return self.client
