import json
from models import Observation

class MedicalEnv:
    def __init__(self):
        self.step_count = 0
        self.done = False
        self.task = None
        self.collected_info = []

    def reset(self, task_file):
        with open(task_file) as f:
            self.task = json.load(f)

        self.step_count = 0
        self.done = False
        self.collected_info = []

        return Observation(
            symptoms=self.task["symptoms"],
            patient_info="limited"
        )

    def step(self, action):
        self.step_count += 1
        reward = 0.0
        error = None

        act = action["decision"]

        if act == "ask_history":
            self.collected_info.append(self.task.get("hidden_info", "none"))
            reward += 0.2

        elif act == f"classify_{self.task['urgency']}":
            reward += 0.3

        elif act == f"diagnose_{self.task['diagnosis']}":
            reward += 0.4

        elif act == f"recommend_{self.task['action']}":
            reward += 0.8
            self.done = True

        else:
            reward -= 0.2
            error = "incorrect_action"

        return Observation(
            symptoms=self.task["symptoms"],
            patient_info="updated"
        ), max(0.0, min(1.0, reward)), self.done, {"error": error}

    def state(self):
        return {
            "steps": self.step_count
        }
