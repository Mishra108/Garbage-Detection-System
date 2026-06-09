# api.py
from fastapi import FastAPI, UploadFile
from ultralytics import YOLO
import numpy as np, cv2

app = FastAPI(title="Garbage Detection API")
model = YOLO("models/weights/best.pt")

@app.get("/")
def root():
    return {"message": "Garbage Detection API is running ✅"}

@app.post("/predict")
async def predict(file: UploadFile):
    img = np.frombuffer(await file.read(), np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    
    # conf=0.5 added — human false detections kam honge
    results = model(img, conf=0.5)[0]
    
    detections = []
    for box in results.boxes:
        detections.append({
            "class": model.names[int(box.cls)],
            "confidence": round(float(box.conf), 4),
            "bbox": box.xyxy[0].tolist()
        })
    return {"detections": detections, "count": len(detections)}