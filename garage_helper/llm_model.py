from typing import Any

class OpenAIModel:
    def __init__(self, client: OpenAI, model_name: str) -> None:
        self.client = client
        self.model_name = model_name

    def generate(self, prompt: str, **kwargs: Any) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        return response.choices[0].message.content
    __call__ = generate

class LLMModel:
    def __init__(self, model_name, model_provider):
        self.model_name = model_name
        self.model_provider = model_provider
    
    def get_model(self):
        if self.model_provider == "openai":
            from openai import OpenAI
            client = OpenAI(
                base_url=endpoint,
                api_key=api_key
            )
            return OpenAIModel(client, self.model_name)
        elif self.model_provider == "anthropic":
            return AnthropicModel(self.model_name)
        elif self.model_provider == "google":
            return GoogleModel(self.model_name)
        else:
            raise ValueError("Invalid model provider")
    
    def generate(self, prompt: str, **kwargs: Any) -> str:
        model = self.get_model()
        return model.generate(prompt, **kwargs)