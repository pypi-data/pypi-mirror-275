import os
from typing import Optional

from bigdata.auth import Auth
from bigdata.connection import BigdataConnection, UploadsConnection
from bigdata.services.content_search import ContentSearch
from bigdata.services.knowledge_graph import KnowledgeGraph
from bigdata.services.uploads import Uploads
from bigdata.services.watchlists import Watchlists
from bigdata.settings import settings


class Bigdata:
    """
    Represents a connection to RavenPack's Bigdata API.

    :ivar knowledge_graph: Proxy for the knowledge graph search functionality.
    :ivar content_search: Proxy object for the content search functionality.
    :ivar watchlists: Proxy object for the watchlist functionality.
    :ivar uploads: Proxy object for the internal content functionality.
    """

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        bigdata_api_url: Optional[str] = None,
        upload_api_url: Optional[str] = None,
    ):
        if password is None:
            password = os.environ.get("BIGDATA_PASSWORD")
        if username is None:
            username = os.environ.get("BIGDATA_USER")
        if username is None or password is None:
            raise ValueError("Username and password must be provided")

        auth = Auth.from_username_and_password(username, password)

        if bigdata_api_url is None:
            bigdata_api_url = str(settings.BIGDATA_API_URL)
        if upload_api_url is None:
            upload_api_url = str(settings.UPLOAD_API_URL)

        self._api = BigdataConnection(auth, bigdata_api_url)
        self._upload_api = UploadsConnection(auth, upload_api_url)
        self.knowledge_graph = KnowledgeGraph(self._api)
        self.content_search = ContentSearch(self._api)
        self.watchlists = Watchlists(self._api)
        self.uploads = Uploads(self._upload_api)
