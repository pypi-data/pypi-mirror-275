import json
import openai
from pydantic import BaseModel
from ._types import GPTMessageRole, GPTSchemaType, GPTModel
from ._validate import GPTSessionConstructorSchema


class GPTClient:
    def __init__(self, model: GPTModel, top_p: float, presence_penalty: float, frequency_penalty: float,
                 temperature: float, response_format: dict = None, max_tokens: int = None, max_retry: int = 3):
        GPTSessionConstructorSchema.model_validate({
            "model": model,
            "top_p": top_p,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "max_retry": max_retry
        })

        self._model = model
        self._top_p = top_p
        self._presence_penalty = presence_penalty
        self._frequency_penalty = frequency_penalty
        self._temperature = temperature
        self._response_format = response_format
        self.max_tokens = max_tokens
        self.max_retry = max_retry

        self._messages: dict = []
        self._ai_client: openai.OpenAI = openai.OpenAI()
        self.last_cost = 0

    def add_message(self, role: GPTMessageRole, data: str | dict | list):
        data_in_json = json.dumps(data)
        self._messages.append({
            "role": role,
            "content": data_in_json
        })

    def clear_messages(self):
        self._messages = []

    def set_schema(self, schema: BaseModel, schema_type: GPTSchemaType):
        json_schema = json.dumps(schema.model_json_schema())
        self._messages.append({
            "role": "system",
            "content": f"{schema_type} JSON schema: {json_schema}"
        })

    def get_messages_token_count(self) -> int:
        from ._tokens_count import num_token_from_message
        return sum([num_token_from_message(message, self._model) for message in self._messages])

    def get_messages(self) -> list:
        return self._messages

    def run(self):
        try:
            response = self._ai_client.with_options(max_retries=self.max_retry).chat.completions.create(
                messages=self._messages,
                model=self._model,
                temperature=self._temperature,
                top_p=self._top_p,
                presence_penalty=self._presence_penalty,
                frequency_penalty=self._frequency_penalty,
                response_format=self._response_format,
                max_tokens=self.max_tokens
            )
            self.last_cost = response.usage.total_tokens
            if response.choices:
                return response.choices[0].message.content
            else:
                return None
        except openai.OpenAIError as error:
            raise error
