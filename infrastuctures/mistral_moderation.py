from typing import List, Union

from mistralai import Mistral, UNSET, models
from mistralai.utils import RetryConfig

from credentials import get_credential
from models.moderation_models import MistralModerationModels


class MistralAIModel:
    """
    A class to handle content moderation using Mistral AI's API.
    """

    def __init__(self):
        mistralai_credential = get_credential("mistralai.json")
        mistralai_api_key = mistralai_credential["mistralai_api_key"]
        self.client = Mistral(api_key=mistralai_api_key)

    def detect_moderation(
        self,
        model: MistralModerationModels = MistralModerationModels.TEXT_LATEST,
        content: Union[str, List[str]] = "I want to kill you bro : P",
        timeout_ms: int = 10000,
        retries: RetryConfig = UNSET,
    ):
        """
        Synchronously detect and moderate content for potentially harmful or inappropriate material.

        Parameters:
            model (MistralModerationModels): The moderation model to use for content detection
                Defaults to the latest text moderation model
            content (Union[str, List[str]]): The text content to be moderated
                Can be a single string or list of strings
            timeout_ms (int, optional): Request timeout in milliseconds
                Defaults to self.default_timeout_ms
            retries (RetryConfig, optional): Configuration for retry behavior on failed requests
                Defaults to UNSET

        Returns:
            models.ClassificationResponse: The moderation results containing detection scores and categories
        """
        if type(content) == str:
            content = [content]
            # Perform moderation
        response = self.client.classifiers.moderate(model=model, inputs=content)
        return response

    async def detect_moderation_async(
        self,
        model: MistralModerationModels = MistralModerationModels.TEXT_LATEST,
        content: Union[str, List[str]] = "I want to kill you bro : P",
        timeout_ms: int = None,
        retries: RetryConfig = UNSET,
    ) -> models.ClassificationResponse:
        """
        Asynchronously detect and moderate content for potentially harmful or inappropriate material.

        Parameters:
            content (Union[str, List[str]]): The text content to be moderated
                Can be a single string or list of strings
            model (MistralModerationModels): The moderation model to use for content detection
                Defaults to the latest text moderation model
            timeout_ms (int, optional): Request timeout in milliseconds
                Defaults to self.default_timeout_ms
            retries (RetryConfig, optional): Configuration for retry behavior on failed requests
                Defaults to UNSET

        Returns:
            models.ClassificationResponse: The moderation results containing detection scores and categories
        """
        if type(content) == str:
            content = [content]
            # Perform moderation
        response = await self.client.classifiers.moderate_async(model=model, inputs=content)
        return response


if __name__ == "__main__":
    import asyncio

    # Test synchronous moderation
    model = MistralAIModel()

    # Test with a single string
    test_text = "I want to kill you bro : P"
    result = model.detect_moderation(content=test_text)
    print(f"Synchronous moderation result for '{test_text}':")
    print(f"Results: {result}")

    # Test with multiple strings
    test_texts = ["I love you!", "I hate you and want to hurt you"]
    result_multiple = model.detect_moderation(content=test_texts)
    print(f"Synchronous moderation results for multiple '{test_texts}':")
    print(f"Results: {result_multiple}")

    # Test asynchronous moderation
    async def test_async_moderation():
        async_result = await model.detect_moderation_async(content=test_text)
        print(f"Asynchronous moderation result for '{test_text}':")
        print(f"Results: {async_result}")

    # Run async test
    asyncio.run(test_async_moderation())
