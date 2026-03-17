from pathlib import Path
from ultralytics import YOLO

# 1) Modelo pré-treinado
model = YOLO("yolov8n.pt")

# 2) Pega só N imagens do teste (não roda no diretório inteiro)
TEST_DIR = Path("datasets/objects-in-the-classroom/data/images/test")
imgs = sorted(TEST_DIR.glob("*.jpg"))[:5]  # roda só 5 imagens
if len(imgs) == 0:
    imgs = sorted(TEST_DIR.glob("*.jpeg"))[:5]
if len(imgs) == 0:
    imgs = sorted(TEST_DIR.glob("*.png"))[:5]

# 3) Roda inferência e SALVA (não abre janela)
# os resultados vão para runs/detect/predict/
results = model.predict(
    source=[str(p) for p in imgs],
    save=True,
    conf=0.25,
    imgsz=640,
    verbose=False
)

print(f"Processed {len(imgs)} images. Results saved in runs/detect/predict/")