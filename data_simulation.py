import random

symptoms = ["Chest Pain", "Shortness of Breath", "Fatigue", "Fever"]

def generate_sample():
    selected = random.sample(symptoms, random.randint(1, 4))

    if "Chest Pain" in selected and "Shortness of Breath" in selected:
        label = "High Risk"
    elif len(selected) >= 2:
        label = "Medium Risk"
    else:
        label = "Low Risk"

    return selected, label


def generate_dataset(n=100):
    data = []
    for _ in range(n):
        x, y = generate_sample()
        data.append((x, y))
    return data