from data_simulation import generate_dataset
from app import medassist

def evaluate():
    dataset = generate_dataset(100)
    correct = 0

    for symptoms, true_label in dataset:
        result = medassist(symptoms)

        if "HIGH" in result and true_label == "High Risk":
            correct += 1
        elif "MEDIUM" in result and true_label == "Medium Risk":
            correct += 1
        elif "LOW" in result and true_label == "Low Risk":
            correct += 1

    accuracy = correct / len(dataset)
    print(f"Model Accuracy: {accuracy*100:.2f}%")

if __name__ == "__main__":
    evaluate()