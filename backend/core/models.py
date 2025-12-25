from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="展示给用户的文本")
    nextNode: Dict[str, Any] = Field(description="下一个节点的内容与选择")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="这一节点的主要内容")
    isEnding: bool = Field(description="这一节点是否为结局节点")
    isWinningEnding: bool = Field(description="这一节点是否为胜利结局")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="这一节点的选项")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="故事的名称")
    rootNode: StoryNodeLLM = Field(description="故事的根节点")
