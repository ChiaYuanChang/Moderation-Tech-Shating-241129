from typing import List, Dict, Any
import openai
from ..import ModerationBase

class OpenAIModerator(ModerationBase):
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    async def check_content(self, text: str) -> Dict[str, Any]:
        """
        Check content using OpenAI's moderation API
        Args:
            text: The text content to check
        Returns:
            Dict containing moderation results
        """
        response = await self.client.moderations.create(input=text)
        return {
            "flagged": response.results[0].flagged,
            "categories": response.results[0].categories,
            "category_scores": response.results[0].category_scores,
        }

    async def batch_check_content(self, texts: List[str]) -> List[Dict[str, Any]]:
        """
        Batch check content using OpenAI's moderation API
        Args:
            texts: List of text content to check
        Returns:
            List of dicts containing moderation results
        """
        response = await self.client.moderations.create(input=texts)
        return [{
            "flagged": result.flagged,
            "categories": result.categories,
            "category_scores": result.category_scores,
        } for result in response.results]