import onnxruntime as rt
import numpy as np
import json
import os

def init():
    global session, input_name, label_names

    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "iris_rf_model.onnx")
    session = rt.InferenceSession(model_path)
    input_name = session.get_inputs()[0].name
    label_names = ["setosa", "versicolor", "virginica"]

def run(raw_data):
    try:
        data = json.loads(raw_data)["data"]
        inputs = np.array(data, dtype=np.float32)
        outputs = session.run(None, {input_name: inputs})
        preds = outputs[0].tolist()
        return [label_names[int(p)] for p in preds]
    except Exception as e:
        return {"error": str(e)}