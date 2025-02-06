# commands.py
class QueryLLMsCommand:
    def __init__(self, llms, prompt):
        self.llms = llms
        self.prompt = prompt

    def execute(self):
        responses = {}
        for name, llm in self.llms.items():
            responses[name] = llm.get_response(self.prompt)
        return responses
