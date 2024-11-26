from typing import List, Union

from openai import AsyncOpenAI, OpenAI
from openai.types import ModerationCreateResponse

from credentials import get_credential
from models.moderation_models import OpenAIModerationModels


class OpenAIModel:
    """
    A class to handle content moderation using OpenAI's Moderation API.
    """

    def __init__(self):
        openai_credential = get_credential("openai.json")
        openai_api_key = openai_credential["openai_api_key"]
        self.client = OpenAI(api_key=openai_api_key)
        self.async_client = AsyncOpenAI(api_key=openai_api_key)

    def detect_moderation(self, model: OpenAIModerationModels = OpenAIModerationModels.TEXT_LATEST, content: Union[str, List[str]] = "I want to kill you bro : P") -> ModerationCreateResponse:
        """
        Synchronously detect and moderate content for potentially harmful or inappropriate material.

        Parameters:
            model (OpenAIModerationModels): The moderation model to use for content detection
                Defaults to the latest text moderation model
            content (Union[str, List[str]]): The text content to be moderated
                Can be a single string or list of strings
                Defaults to a test string

        Returns:
            ModerationCreateResponse: The moderation results containing detection scores and categories
                Including fields like 'flagged', 'categories', and 'category_scores'
        """
        response = self.client.moderations.create(model=model, input=content)
        return response

    async def detect_moderation_async(self, model: OpenAIModerationModels = OpenAIModerationModels.TEXT_LATEST, content: Union[str, List[str]] = "I want to kill you bro : P") -> ModerationCreateResponse:
        """
        Asynchronously detect and moderate content for potentially harmful or inappropriate material.

        Parameters:
            model (OpenAIModerationModels): The moderation model to use for content detection
                Defaults to the latest text moderation model
            content (Union[str, List[str]]): The text content to be moderated
                Can be a single string or list of strings
                Defaults to a test string

        Returns:
            ModerationCreateResponse: The moderation results containing detection scores and categories
                Including fields like 'flagged', 'categories', and 'category_scores'
        """
        response = await self.async_client.moderations.create(model=model, input=content)
        return response


if __name__ == "__main__":
    import asyncio

    # Test the moderation
    openai_model = OpenAIModel()

    # Test with a single string
    test_text = "I want to kill you bro : P"
    result = openai_model.detect_moderation(content=test_text)
    print(f"Synchronous moderation result for '{test_text}':")
    print(f"Results: {result.results[0]}")

    # Test with multiple strings
    test_texts = ["I want to love you bro : P!", "I want to kill you bro : P"]
    result_multiple = openai_model.detect_moderation(content=test_texts)
    print(f"Synchronous moderation results for multiple '{test_texts}':")
    print(f"Results: {result_multiple}")

    # Test asynchronous moderation
    async def test_async_moderation():
        async_result = await openai_model.detect_moderation_async(content=test_text)
        print(f"Asynchronous moderation result for '{test_text}':")
        print(f"Results: {async_result.results[0]}")

    # Run async test
    asyncio.run(test_async_moderation())
