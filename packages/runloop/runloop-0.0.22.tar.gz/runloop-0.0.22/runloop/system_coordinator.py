import abc
from typing import Dict, List

from runloop.devbox import Devbox


class SystemCoordinator(abc.ABC):
    """The runloop SystemCoordinator provides the ability to spawn and manage devboxes."""

    @abc.abstractmethod
    def create_devbox(
        self,
        code_handle_id: str | None,
        env_vars: Dict[str, str] | None,
        secrets: Dict[str, str] | None,
        user_entry_point_script: List[str] | None,
    ) -> Devbox: ...
