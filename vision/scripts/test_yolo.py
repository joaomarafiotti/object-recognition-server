from ultralytics import YOLO

# carrega modelo pré-treinado
model = YOLO("yolov8n.pt")

# roda em uma imagem do dataset
results = model("datasets/objects-in-the-classroom/data/images/test")

# mostra resultados
for r in results:
    r.show()