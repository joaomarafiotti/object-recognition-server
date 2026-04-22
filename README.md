# object-recognition-server

Servidor mínimo para detecção de objetos usando YOLO, desenvolvido como parte da iniciação científica sobre reconhecimento de objetos para usuários cegos em contexto educacional.

## Objetivo

Receber uma imagem, executar inferência com um modelo YOLO e retornar um JSON com os objetos detectados.

## Stack

* Python
* FastAPI
* Uvicorn
* Ultralytics / YOLOv8

## Estrutura

* `app/`: backend e serviço de inferência
* `configs/`: configuração do dataset
* `datasets/`: instruções para dataset local
* `docs/progress/`: registros de progresso
* `vision/scripts/`: scripts de teste

## Como rodar

1. Ativar o ambiente virtual: `venv\Scripts\activate`
2. Subir o servidor: `uvicorn app.main:app --reload`

## Endpoints

### `GET /health`

Retorna:

```json
{"status":"ok"}
```

### `POST /detect`

Recebe uma imagem (`jpg`, `jpeg`, `png`) e retorna algo como:

```json
{
  "filename": "example.jpg",
  "num_detections": 1,
  "inference_ms": 82.6,
  "detections": [
    {
      "class_id": 0,
      "class_name": "person",
      "confidence": 0.62
    }
  ]
}
```

## Status atual

* Dataset classroom definido
* Treino mínimo inicial realizado
* Backend mínimo funcional implementado
* Próximo passo: cliente Android mínimo