import os
from ultralytics import YOLO

# Carrega o modelo uma única vez quando o servidor inicia
MODEL_PATH = os.getenv("MODEL_PATH", "yolov8n.pt")
model = YOLO(MODEL_PATH)

def detect_objects(image_path: str, conf: float = 0.25):
    """
    Roda detecção de objetos em uma imagem e retorna lista de detecções.
    Retorno: [{"class_id": int, "class_name": str, "confidence": float}, ...]
    """
    results = model.predict(source=image_path, conf=conf, verbose=False)

    detections = []
    for r in results:
        names = r.names  # dict id->name
        if r.boxes is None:
            continue
        for b in r.boxes:
            cls_id = int(b.cls[0].item())
            conf_score = float(b.conf[0].item())
            detections.append({
                "class_id": cls_id,
                "class_name": names.get(cls_id, str(cls_id)),
                "confidence": conf_score
            })

    return detections