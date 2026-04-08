import os
from env import MedicalEnv

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")


def run_task(name, file):
    env = MedicalEnv()

    # IMPORTANT: must pass input to reset
    obs = env.reset(["Fever"])

    print(f"[START] task={name} env=medassist model={MODEL_NAME}")

    done = False
    step = 0

    while not done:
        # IMPORTANT: use obs["observation"]
        symptoms = obs["observation"]["symptoms"]

        action = {
            "symptoms": symptoms
        }

        result = env.step(action)

        print(f"[STEP] step={step} reward={result['reward']}")

        obs = result
        done = result["done"]
        step += 1

    print(f"[END] total_steps={step}")