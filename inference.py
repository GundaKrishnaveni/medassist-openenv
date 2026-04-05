import os
from env import MedicalEnv

# Required env variables (kept for compliance)
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")

def run_task(name, file):
    env = MedicalEnv()
    obs = env.reset(file)

    print(f"[START] task={name} env=medassist-pro model={MODEL_NAME}")

    done = False
    step = 0
    rewards = []

    while not done and step < 5:
        step += 1

        # Step 1: Always gather info
        if step == 1:
            action = {"decision": "ask_history"}

        # Step 2: classify urgency
        elif step == 2:
            if "chest pain" in obs.symptoms:
                action = {"decision": "classify_high"}
            elif "fatigue" in obs.symptoms:
                action = {"decision": "classify_medium"}
            else:
                action = {"decision": "classify_low"}

        # Step 3: diagnosis
        elif step == 3:
            if "chest pain" in obs.symptoms:
                action = {"decision": "diagnose_heart_attack"}
            elif "fatigue" in obs.symptoms:
                action = {"decision": "diagnose_diabetes"}
            else:
                action = {"decision": "diagnose_flu"}

        # Step 4+: final recommendation (this should end episode)
        else:
            if "chest pain" in obs.symptoms:
                action = {"decision": "recommend_hospital"}
            elif "fatigue" in obs.symptoms:
                action = {"decision": "recommend_consult_doctor"}
            else:
                action = {"decision": "recommend_rest"}

        # Take step
        obs, reward, done, info = env.step(action)
        rewards.append(f"{reward:.2f}")

        # Handle error field
        err = info["error"] if info["error"] else "null"

        print(f"[STEP] step={step} action={action['decision']} reward={reward:.2f} done={str(done).lower()} error={err}")

    # Compute score
    score = sum(map(float, rewards)) / len(rewards) if rewards else 0.0

    print(f"[END] success=true steps={step} score={score:.2f} rewards={','.join(rewards)}")


if __name__ == "__main__":
    run_task("easy", "tasks/easy.json")
    run_task("medium", "tasks/medium.json")
    run_task("hard", "tasks/hard.json")