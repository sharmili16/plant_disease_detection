from tensorflow.keras.models import load_model
def load_prediction_model():
  model = load_model("prediction_model")
  return model