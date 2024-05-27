from typing import Literal
from pydantic import BaseModel

from dendrite_python_sdk.dendrite_browser.common.status import Status


class InteractionResponse(BaseModel):
    message: str
    status: Status
