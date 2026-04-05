class Client:
    def __init__(self):
        pass

    def act(self, observation):
        # simple baseline action
        return {"decision": "ask_history"}