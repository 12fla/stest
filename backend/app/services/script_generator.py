from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
import os
from typing import Optional, Tuple

class ScriptGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.model = ChatOpenAI(
            openai_api_key=api_key,
            temperature=0.7,
            base_url="https://api.deepseek.com/v1",
            model="deepseek-chat",
            timeout=30,
            max_retries=2
        )
        self.wikipedia = WikipediaAPIWrapper(
            lang="zh",
            timeout=15,
            extract_format="plaintext",
            sentences=10,
            wiki_base_url="https://zh.wikipedia.org/w/api.php"
        )
    
    def generate_script(
        self, 
        subject: str, 
        video_length: float = 1.0, 
        creativity: float = 0.7
    ) -> Tuple[str, str, str]:
        # 生成标题
        title_template = ChatPromptTemplate.from_messages([
            ("human", "请为'{subject}'主题的短视频创作1个吸引人的标题，严格遵循：\n"  
                      "1. 用年轻人熟悉的网络热词/疑问句/反差感\n"  
                      "2. 20字以内，无专业术语，一眼抓注意力\n"  
                      "3. 适配抖音/小红书等短视频平台传播逻辑")
        ])
        title_chain = title_template | self.model
        title = title_chain.invoke({"subject": subject}).content.strip()
        
        # 获取维基百科信息
        search_result = ""
        try:
            search_result = self.wikipedia.run(subject)
            if not search_result.strip():
                search_result = "维基百科未找到相关详细信息，以下基于公开常识生成内容"
        except Exception as e:
            search_result = f"维基百科搜索异常：{str(e)[:50]}...，以下基于公开常识生成内容"
        
        # 生成脚本
        word_count = int(video_length * 200)
        script_template = ChatPromptTemplate.from_messages([
            ("human", """你是抖音/小红书风格的年轻向短视频博主，说话接地气、有网感，避免说教式表达。
             请根据以下信息生成结构化视频脚本，严格遵守要求：

             核心约束：
             - 视频标题：{title}
             - 目标时长：{duration}分钟（1分钟≈200字，总字数控制在 {word_count} 字左右）
             - 参考资料：维基百科搜索结果（仅提取相关干货，无关内容直接忽略）

             脚本结构要求（必须明确分隔）：
             1. 【开头】（30字内）：用反转/疑问/热点引入，瞬间抓住注意力；
             2. 【中间】（核心干货）：提炼维基百科关键信息，用大白话解释，无专业术语；
             3. 【结尾】（30字内）：留悬念/引导互动；

             风格要求：
             - 全程口语化，像和朋友聊天，适当用表情符号增强感染力；
             - 避免长句，每句不超过15字，符合短视频快节奏表达；
             - 网络热词自然融入，不堆砌。

             参考资料：
             ```{wikipedia_search}```""")
        ])
        script_chain = script_template | self.model
        script = script_chain.invoke({
            "title": title,
            "duration": video_length,
            "word_count": word_count,
            "wikipedia_search": search_result
        }).content.strip()
        
        return search_result, title, script