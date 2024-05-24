from pydantic import BaseModel
from typing import Optional
from foundationallm.models.agents import OperationTypes
from foundationallm.models.authentication import AuthenticationTypes

class EndpointSettings(BaseModel):
    endpoint: str
    api_key: Optional[str] = None
    api_type: Optional[str] = None
    api_version: Optional[str] = None
    authentication_type: str = AuthenticationTypes.TOKEN
    operation_type: str = OperationTypes.CHAT
    provider: str
