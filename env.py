class MedicalEnv:
    def __init__(self):
        self.done = False

    def reset(self, input_data=None):
        self.done = False

        # ✅ Robust handling (VERY IMPORTANT)
        if input_data is None:
            symptoms = []
        elif isinstance(input_data, dict):
            symptoms = input_data.get("symptoms", [])
        elif isinstance(input_data, list):
            symptoms = input_data
        else:
            symptoms = []

        return {
            "observation": {
                "symptoms": symptoms
            }
        }

    def step(self, action):
        # ✅ Safe extraction (IMPORTANT)
        if isinstance(action, dict):
            symptoms = action.get("symptoms", [])
        else:
            symptoms = []

        score = 0
        if "Chest Pain" in symptoms:
            score += 5
        if "Shortness of Breath" in symptoms:
            score += 4
        if "Fatigue" in symptoms:
            score += 2
        if "Fever" in symptoms:
            score += 1

        if score >= 7:
            diagnosis = "High Risk"
            reward = 1.0
        elif score >= 4:
            diagnosis = "Moderate Risk"
            reward = 0.6
        else:
            diagnosis = "Low Risk"
            reward = 0.3

        self.done = True

        return {
            "observation": {
                "diagnosis": diagnosis
            },
            "reward": reward,
            "done": True,
            "info": {}
        }