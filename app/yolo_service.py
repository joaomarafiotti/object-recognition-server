import os
from typing import Any
from ultralytics import YOLO

MODEL_PATH = os.getenv("MODEL_PATH", "yolov8n.pt")
model = YOLO(MODEL_PATH)


def get_model_name() -> str:
    """
    Retorna apenas o nome do arquivo/modelo carregado pelo backend.
    Exemplo: classroom_yolov8n_e50_best.pt
    """
    return os.path.basename(MODEL_PATH)


def detect_objects(image_path: str, conf: float = 0.25) -> list[dict[str, Any]]:
    """
    Roda detecção de objetos em uma imagem e retorna uma lista de detecções.

    Cada detecção tem o formato:
    {
        "class_id": int,
        "class_name": str,
        "confidence": float
    }
    """
    results = model.predict(source=image_path, conf=conf, verbose=False)

    detections: list[dict[str, Any]] = []

    for result in results:
        names = result.names
        if result.boxes is None:
            continue

        for box in result.boxes:
            class_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())

            detections.append(
                {
                    "class_id": class_id,
                    "class_name": names.get(class_id, str(class_id)),
                    "confidence": confidence,
                }
            )

    return detections