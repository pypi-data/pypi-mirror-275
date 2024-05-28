from pydantic import BaseModel


class ClientOptions(BaseModel):
    """
    Options for the client.
    """

    event_api_url: str
    connection_service_url: str
    api_token: str
    log_level: str = "ERROR"
