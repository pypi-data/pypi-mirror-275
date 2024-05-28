#  disai_jazz/arch.py
class SequentialFlow:
    def __init__(self, agent, model):
        self.agent = agent
        self.model = model

    def generate_prompt(self, user_prompt):
        return f"{self.agent} {user_prompt}"

    def gen_image(self, user_prompt):
        full_prompt = self.generate_prompt(user_prompt)
        return self.model.generate_image(full_prompt)
    
    def web_agent(self,user_prompt):
        full_prompt = self.generate_prompt(user_prompt)
        return self.model.webagent(full_prompt)
