import os
from env import MedicalEnv

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")

def run_task(name, file):
    env = MedicalEnv()
    obs = env.reset(["Fever"])   # sample input

    print(f"[START] task={name} model={MODEL_NAME}")

    done = False
    step = 0

    while not done:
        action = {"symptoms": obs["symptoms"]}

        result = env.step(action)

        print(f"[STEP] step={step} action={action} reward={result['reward']}")

        done = result["done"]
        step += 1

    print(f"[END] total_steps={step}")