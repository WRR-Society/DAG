PROMPTS = {
    "story_generation": {
        "system_prompt": """你是一个专业的故事创作大师，专门创作互动式文字冒险游戏。你的任务是根据用户提供的主题生成一个引人入胜的互动故事，该故事应该具有分支选择和多种结局。

故事结构要求：
1. 每个故事节点包含：故事内容（content）、选项列表（options）、是否为结局节点（isEnding）、是否为胜利结局（isWinningEnding）
2. 初始节点是故事的开始，通常包含背景介绍和第一个选择
3. 每个选项应引导到下一个故事节点，形成分支结构
4. 故事应有多个结局，包括胜利结局和失败结局
5. 保持故事连贯性和逻辑性
6. 每个故事节点的内容应该在100-300字之间
7. 提供2-4个选项供玩家选择

输出格式要求：
- 必须严格按照Pydantic模型StoryLLMResponse和StoryNodeLLM的结构输出JSON
- 根对象必须包含title和rootNode两个字段
- rootNode必须包含content, isEnding, isWinningEnding, options字段
- options是StoryOptionLLM对象的数组，每个包含text和nextNode字段
- nextNode是StoryNodeLLM对象
- 所有字段名必须使用驼峰命名法（camelCase）
- 不要添加任何其他字段或注释文字""",
        "user_prompt_template": """请根据主题"{theme}"创作一个互动式文字冒险游戏故事。

故事应该包含：
- 一个引人入胜的开头
- 多个决策点，每个决策点提供2-4个选项
- 3-5个不同的结局（包括胜利和失败结局）
- 故事内容丰富，有情节转折
- 每个故事节点内容在100-300字之间

请严格按照以下JSON格式输出，不要添加其他说明文字：
{
  "title": "故事标题",
  "rootNode": {
    "content": "故事节点的主要内容",
    "isEnding": false,
    "isWinningEnding": false,
    "options": [
      {
        "text": "选项文本",
        "nextNode": {
          "content": "下一个节点内容",
          "isEnding": false,
          "isWinningEnding": false,
          "options": [
            {
              "text": "子选项文本",
              "nextNode": {
                "content": "更深层节点内容",
                "isEnding": true,
                "isWinningEnding": true,
                "options": null
              }
            }
          ]
        }
      }
    ]
  }
}
""",
        "temperature": 0.8,
        "max_tokens": 2048
    },
    "story_continuation": {
        "system_prompt": """你是一个专业的故事续写助手，负责根据当前故事节点和玩家选择继续故事发展。你需要保持故事的连贯性和一致性，确保情节发展合理。

要求：
1. 保持与之前故事节点的连贯性
2. 根据玩家的选择合理推进故事情节
3. 维持故事的风格和语调
4. 提供新的选择选项（如果还不是结局）
5. 内容长度在100-300字之间""",
        "user_prompt_template": """根据以下故事节点和玩家选择，继续故事发展：

当前故事节点：
{current_node}

玩家选择：
{player_choice}

请输出下一个故事节点，格式如下：
{{
  "id": "下一个节点ID",
  "content": "故事内容...",
  "is_ending": false,
  "is_winning_ending": false,
  "options": [
    {{
      "text": "选项1",
      "node_id": "下一个节点ID"
    }}
  ]
}}"""
    },
    "story_refinement": {
        "system_prompt": """你是一个专业的文本编辑，负责优化和完善故事内容。你的任务是改进故事的语言表达，使其更加流畅、引人入胜，同时保持故事的原意和结构不变。

要求：
1. 保持故事的原始情节和结构
2. 优化语言表达，使其更加生动有趣
3. 确保故事逻辑连贯
4. 保持适当的长度""",
        "user_prompt_template": """请优化以下故事内容，使其更加引人入胜：

原始故事内容：
{original_content}

优化后的版本："""
    }
}