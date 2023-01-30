import openai
import config


class OpenAIClient:
    def __init__(self):
        openai.api_key = config.get_api_key()

    def get_model_list(self):
        return openai.Model.list()

    def completion(self, prompt: str, model: str, max_tokens: int):
        return openai.Completion.create(
            model=model, prompt=prompt, max_tokens=max_tokens
        )
