import os
import uuid
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.yolo_service import detect_objects

app = FastAPI(title="Object Recognition Server", version="0.1.0")

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    # salva arquivo temporário
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in [".jpg", ".jpeg", ".png"]:
        return JSONResponse(status_code=400, content={"error": "Formato inválido. Use jpg/jpeg/png."})

    temp_name = f"{uuid.uuid4().hex}{ext}"
    temp_path = os.path.join(UPLOAD_DIR, temp_name)

    data = await file.read()
    with open(temp_path, "wb") as f:
        f.write(data)

    # roda detecção
    import time
    t0 = time.time()
    detections = detect_objects(temp_path, conf=0.25)
    dt_ms = (time.time() - t0) * 1000
    
    # (opcional) apagar arquivo temporário
    try:
        os.remove(temp_path)
    except Exception:
        pass

    return {
        "filename": file.filename,
        "num_detections": len(detections),
        "inference_ms": round(dt_ms, 2),
        "detections": detections
    }