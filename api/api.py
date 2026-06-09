from fastapi import FastAPI, UploadFile
from ultralytics import YOLO
import numpy as np, cv2

app = FastAPI(title="Garbage Detection API")
model = None

def get_model():
    global model
    if model is None:
        model = YOLO("models/weights/best.pt")
    return model

@app.get("/")
def root():
    return {"message": "Garbage Detection API is running ✅"}

@app.post("/predict")
async def predict(file: UploadFile):
    m = get_model()
    img = np.frombuffer(await file.read(), np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    results = m(img, conf=0.5)[0]
    detections = []
    for box in results.boxes:
        detections.append({
            "class": m.names[int(box.cls)],
            "confidence": round(float(box.conf), 4),
            "bbox": box.xyxy[0].tolist()
        })
    return {"detections": detections, "count": len(detections)}