from pathlib import Path
import requests

API_URL = "http://127.0.0.1:8000/detect"
IMG_PATH = Path(
    "datasets/objects-in-the-classroom/data/images/test/"
    "bag_02a48ac894ff090bcc47688b2ded534a_jpg.rf.06180c4c69d84529aad234049b477168.jpg"
)

with open(IMG_PATH, "rb") as f:
    files = {"file": (IMG_PATH.name, f, "image/jpeg")}
    response = requests.post(API_URL, files=files)

print(response.status_code)
print(response.json())