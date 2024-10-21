import os
from dotenv import load_dotenv

load_dotenv()

class SDKConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SDKConnection, cls).__new__(cls)
            cls._instance._initialize_connection(*args, **kwargs)
        return cls._instance

    def _initialize_connection(self, api_url=None, api_key=None, **kwargs):

        api_url = api_url or os.getenv("ARGILLA_API_URL")
        api_key = api_key or os.getenv("ARGILLA_API_KEY")

        if not api_url:
            raise ValueError("ARGILLA_API_URL is not set in the environment variables")
        if not api_key:
            raise ValueError("ARGILLA_API_KEY is not set in the environment variables")

        import argilla as rg
        self._instance = rg.Argilla(
            api_url=api_url,
            api_key=api_key,
            **kwargs
        )
