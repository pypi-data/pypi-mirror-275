import requests
from typing import Optional
import logging


class LRCProvider:
    """
    Base class for all of the synced (LRC format) lyrics providers.
    """

    def __init__(self) -> None:
        self.session = requests.Session()

        # Logging setup
        formatter = logging.Formatter("[%(name)s] %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.addHandler(handler)

    def get_lrc_by_id(self, track_id: str) -> Optional[str]:
        """
        Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.

        ### Arguments
        - track_id: The ID of the track defined in the provider database. e.g. Spotify/Deezer track ID
        """
        raise NotImplementedError

    def get_lrc(self, search_term: str) -> Optional[str]:
        """
        Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.
        """
        raise NotImplementedError
