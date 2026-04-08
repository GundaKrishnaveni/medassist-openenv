import os
from env import MedicalEnv

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")

def run_task(name, file):
    env = MedicalEnv()

    obs = env.reset({"symptoms": ["Fever"]})

    print(f"[START] task={name} env=medassist model={MODEL_NAME}")

    done = False
    step = 0

    while not done:
        action = {
            "symptoms": obs["observation"]["symptoms"]
        }

        result = env.step(action)

        print(f"[STEP] step={step} reward={result['reward']}")

        obs = result
        done = result["done"]
        step += 1

    print(f"[END] total_steps={step}")


# ✅ THIS WAS MISSING (CRITICAL)
if __name__ == "__main__":
    run_task("test", None)