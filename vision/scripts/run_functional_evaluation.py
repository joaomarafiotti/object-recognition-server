import csv
import json
from datetime import datetime
from pathlib import Path

import requests

API_URL = "http://127.0.0.1:8000/detect"

TEST_DIR = Path("datasets/objects-in-the-classroom/data/images/test")
OUTPUT_DIR = Path("docs/evaluation")
OUTPUT_FILE = OUTPUT_DIR / "functional_test_results.csv"

EVALUATION_CASES = [
    {"expected": "table", "pattern": "table_*"},
    {"expected": "chair", "pattern": "chair_images-18-*"},
    {"expected": "whiteboard", "pattern": "whiteboard-test-1.*"},
    {"expected": "bookshelf", "pattern": "bookshelf-test-1.*"},
    {"expected": "clock", "pattern": "clock-test-7.*"},
    {"expected": "wall-magazine", "pattern": "walmegazine-test-1.*"},
    {"expected": "trash-can", "pattern": "trashcan-test1.*"},
    {"expected": "eraser", "pattern": "eraser193.*"},
    {"expected": "sharpener", "pattern": "sharpener193.*"},
    {"expected": "pen", "pattern": "pen193.*"},
    {"expected": "book", "pattern": "book_fd526e72cac26aa8_jpg*"},
    {"expected": "ruler", "pattern": "ruler193.*"},
    {"expected": "scissor", "pattern": "scissor193.*"},
    {"expected": "fan", "pattern": "fan_193.*"},
    {"expected": "laptop", "pattern": "laptop_194.*"},
    {"expected": "remote-control", "pattern": "remote-control_193.*"},
    {"expected": "bag", "pattern": "bag_12-c608116e-ae57-403c-b447-88afd14b2_jpg*"},
    {"expected": "pants", "pattern": "pants_image178_jpg*"},
    {"expected": "shoes", "pattern": "shoes_193.*"},
    {"expected": "hat", "pattern": "hat_image--209-*"},
]


def find_image(pattern: str) -> Path | None:
    matches = sorted(TEST_DIR.glob(pattern))
    return matches[0] if matches else None


def classify_result(expected: str, detected_objects: list[str]) -> str:
    if not detected_objects:
        return "nenhuma_detecção"

    if expected in detected_objects:
        return "correto"

    return "erro"


def run_detection(image_path: Path) -> dict:
    with image_path.open("rb") as image_file:
        files = {
            "file": (
                image_path.name,
                image_file,
                "image/jpeg",
            )
        }

        response = requests.post(API_URL, files=files, timeout=60)
        response.raise_for_status()
        return response.json()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rows = []

    for case in EVALUATION_CASES:
        expected = case["expected"]
        pattern = case["pattern"]
        image_path = find_image(pattern)

        if image_path is None:
            rows.append(
                {
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "expected_class": expected,
                    "pattern": pattern,
                    "image_file": "",
                    "model": "",
                    "num_detections": 0,
                    "detected_objects": "",
                    "top_confidence": "",
                    "inference_ms": "",
                    "status": "arquivo_não_encontrado",
                    "raw_response": "",
                }
            )
            continue

        try:
            result = run_detection(image_path)

            detections = result.get("detections", [])
            detected_objects = [
                detection.get("class_name", "")
                for detection in detections
                if detection.get("class_name")
            ]

            confidences = [
                float(detection.get("confidence", 0))
                for detection in detections
            ]

            top_confidence = max(confidences) if confidences else ""

            status = classify_result(expected, detected_objects)

            rows.append(
                {
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "expected_class": expected,
                    "pattern": pattern,
                    "image_file": image_path.name,
                    "model": result.get("model", ""),
                    "num_detections": result.get("num_detections", 0),
                    "detected_objects": ", ".join(detected_objects),
                    "top_confidence": round(top_confidence, 4) if top_confidence != "" else "",
                    "inference_ms": result.get("inference_ms", ""),
                    "status": status,
                    "raw_response": json.dumps(result, ensure_ascii=False),
                }
            )

            print(
                f"[{status}] esperado={expected} | "
                f"detectado={detected_objects} | "
                f"arquivo={image_path.name}"
            )

        except Exception as error:
            rows.append(
                {
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "expected_class": expected,
                    "pattern": pattern,
                    "image_file": image_path.name,
                    "model": "",
                    "num_detections": "",
                    "detected_objects": "",
                    "top_confidence": "",
                    "inference_ms": "",
                    "status": "erro_execução",
                    "raw_response": str(error),
                }
            )

            print(f"[erro_execução] esperado={expected} | arquivo={image_path.name} | erro={error}")

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csv_file:
        fieldnames = [
            "timestamp",
            "expected_class",
            "pattern",
            "image_file",
            "model",
            "num_detections",
            "detected_objects",
            "top_confidence",
            "inference_ms",
            "status",
            "raw_response",
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print()
    print(f"Resultados salvos em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()