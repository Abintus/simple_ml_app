import joblib
from sklearn.datasets import load_iris


def load_model(filename):
    return joblib.load(filename)


def predict(model, input_data):
    iris = load_iris()
    predictions = model.predict(input_data)
    return [iris.target_names[pred] for pred in predictions]


if __name__ == "__main__":
    model = load_model("trained_model.joblib")
    sample_data = [[5.1, 3.5, 1.4, 0.2]]
    predictions = predict(model, sample_data)
    print(f"Predicted class: {predictions}")
