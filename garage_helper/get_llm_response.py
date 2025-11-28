
from garage_helper.llm_model import LLMModel

MODEL_LOOKUP = {
    'openai': ['gpt-5','o3','o3-mini','gpt-5-mini'],
    'google': ['gemini-3-pro','gemini-2.0-flash']
}

class LLMResponse:
    def __init__(self, input, model_name):
        self.response = self.get_response(input, model_name)
    
    def get_response(self, input, model_name):
        model = LLMModel(model_name, 'openai')
        return model.generate(input)