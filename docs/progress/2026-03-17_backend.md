# Progresso (2026-03-17) — Backend mínimo (FastAPI)

## Objetivo
Implementar servidor mínimo que recebe uma imagem e retorna lista de objetos detectados (JSON), alinhado ao cronograma da IC.

## Como rodar
1) Ativar venv
venv\Scripts\activate

2) Subir servidor
uvicorn app.main:app --reload

## Endpoints
- GET /health
  - retorna {"status":"ok"}

- POST /detect (multipart/form-data)
  - campo: file (jpg/jpeg/png)
  - retorna: filename, num_detections, inference_ms, detections[]

## Testes
### Health
curl.exe http://127.0.0.1:8000/health

### Detect (PowerShell com curl real)
$img="datasets\objects-in-the-classroom\data\images\test\<arquivo>.jpg"
curl.exe -X POST "http://127.0.0.1:8000/detect" -F "file=@$img"

### Teste via Python
py vision/scripts/test_api_detect.py