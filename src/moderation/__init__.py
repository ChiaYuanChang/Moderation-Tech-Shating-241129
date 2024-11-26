from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ModerationBase(ABC):
    @abstractmethod
    async def check_content(self, text: str) -> Dict[str, Any]:
        """
        Check if content is appropriate
        Args:
            text: The text content to check
        Returns:
            Dict containing moderation results
        """
        pass

    @abstractmethod
    async def batch_check_content(self, texts: List[str]) -> List[Dict[str, Any]]:
        """
        Check multiple content items
        Args:
            texts: List of text content to check
        Returns:
            List of dicts containing moderation results
        """
        pass