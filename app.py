from fastapi import FastAPI
import joblib
from api.models.iris import PredictRequest, PredictResponse

app = FastAPI()


model = None


def load_model():
    global model
    model = joblib.load("trained_model.joblib")


@app.on_event("startup")
def startup_event():
    load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    # Extract feature values as a 2D list
    features = [
        [
            request.sepal_length,
            request.sepal_width,
            request.petal_length,
            request.petal_width,
        ]
    ]

    # Make prediction
    prediction = model.predict(features)

    # Return the prediction as a response
    return PredictResponse(prediction=str(prediction[0]))
