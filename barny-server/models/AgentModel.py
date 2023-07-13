from pydantic import BaseModel
from typing import Dict, Any

class AgentModel(BaseModel):
    name: str | None = None
    ip: str | None = None
    domain: str | None = None

    def dictionary(self, *args, **kwargs) -> Dict[str, Any]:
        kwargs.pop('exclude_none', None)
        return super().dict(*args, exclude_none=True, **kwargs)
