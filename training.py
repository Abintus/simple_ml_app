from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    data = load_iris()
    X, y = data.data, data.target
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def save_model(model, filename):
    joblib.dump(model, filename)


X_train, X_test, y_train, y_test = load_data()
model = train_model(X_train, y_train)
save_model(model, "trained_model.joblib")
