from pydantic import BaseModel, Field, ConfigDict


class RespondRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    message: str = Field(min_length=1, max_length=8000)


class IntentAnalysis(BaseModel):
    intent: str
    summary: str
    requires_action: bool = False
    priority: str = "normal"


class RespondResponse(BaseModel):
    analysis: IntentAnalysis
    markdown_response: str
