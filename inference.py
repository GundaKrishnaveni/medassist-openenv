import os
from env import MedicalEnv

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")


def run():
    env = MedicalEnv()

    obs = env.reset({"symptoms": ["Fever"]})

    print("[START]")

    done = False
    step = 0

    while not done:
        action = {"symptoms": obs["symptoms"]}

        result = env.step(action)

        print(f"[STEP] step={step} reward={result['reward']}")

        obs = result
        done = result["done"]
        step += 1

    print("[END]")


if __name__ == "__main__":
    run()