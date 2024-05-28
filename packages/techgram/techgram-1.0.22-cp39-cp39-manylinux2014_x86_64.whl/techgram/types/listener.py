from asyncio import Future
from dataclasses import dataclass
from typing import Callable

import techgram
from techgram.enums import ListenerTypes

from .identifier import Identifier


@dataclass
class Listener:
    listener_type: ListenerTypes
    filters: techgram.filters.Filter
    unallowed_click_alert: bool
    identifier: Identifier
    future: Future = None
    callback: Callable = None
