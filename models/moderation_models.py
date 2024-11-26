from enum import StrEnum


class OpenAIModerationModels(StrEnum):
    OMNI_LATEST = "omni-moderation-latest"
    OMNI_2024_09_26 = "omni-moderation-2024-09-26"
    TEXT_LATEST = "text-moderation-latest"
    TEXT_STABLE = "text-moderation-stable"
    TEXT_007 = "text-moderation-007"


# class AnthropicModerationModels(StrEnum):


class MistralModerationModels(StrEnum):
    TEXT_2411 = "mistral-moderation-2411"
    TEXT_LATEST = "mistral-moderation-latest"
