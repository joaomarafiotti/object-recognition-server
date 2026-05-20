# object-recognition-server

Servidor para detecção de objetos usando YOLO, desenvolvido como parte da iniciação científica sobre reconhecimento de objetos para auxílio a usuários cegos em contexto educacional.

## Objetivo

Receber uma imagem, executar inferência com um modelo YOLO e retornar um JSON com os objetos detectados.

Este repositório representa o backend da arquitetura cliente-servidor do projeto. O cliente Android está no repositório `blind-assistance-app`.

## Stack

* Python
* FastAPI
* Uvicorn
* Ultralytics / YOLOv8
* PowerShell / curl.exe para testes locais

## Estrutura

* `app/`: backend e serviço de inferência
* `configs/`: configuração do dataset
* `datasets/`: instruções para dataset local
* `docs/progress/`: registros de progresso
* `vision/scripts/`: scripts de teste
* `models/`: pasta local sugerida para armazenar pesos `.pt` do modelo

## Modelo principal atual

O modelo principal atual do projeto é:

`classroom_yolov8n_e50_best.pt`

Esse modelo corresponde a um YOLOv8n ajustado ao dataset **Objects in the Classroom**.

Resumo do treinamento:

* modelo base: YOLOv8n
* dataset: Objects in the Classroom
* classes: 20
* epochs: 50
* image size: 640
* batch size: 16
* ambiente: Google Colab com GPU Tesla T4

Resultado no conjunto de teste:

| Métrica   | Valor |
| --------- | ----: |
| Precision | 0.866 |
| Recall    | 0.870 |
| mAP50     | 0.900 |
| mAP50-95  | 0.746 |

## Observação sobre o arquivo `.pt`

O arquivo do modelo **não é versionado no GitHub**.

Coloque localmente o arquivo:

`classroom_yolov8n_e50_best.pt`

dentro da pasta:

`models/`

Exemplo de estrutura local:

```text
object-recognition-server/
├── app/
├── configs/
├── datasets/
├── models/
│   └── classroom_yolov8n_e50_best.pt
├── vision/
├── README.md
└── requirements.txt
```

Arquivos `.pt` são ignorados pelo `.gitignore`.

## Como rodar

### 1. Ativar o ambiente virtual

No PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 2. Rodar com o modelo padrão

Se nenhum modelo for informado, o backend usa `yolov8n.pt`:

```powershell
uvicorn app.main:app --reload
```

### 3. Rodar com o modelo treinado da IC

Para usar o modelo treinado no dataset Objects in the Classroom:

```powershell
$env:MODEL_PATH="models/classroom_yolov8n_e50_best.pt"
uvicorn app.main:app --reload
```

## Endpoints

### `GET /health`

Verifica se o servidor está ativo e informa o modelo carregado.

Exemplo:

```json
{
  "status": "ok",
  "model": "classroom_yolov8n_e50_best.pt"
}
```

### `POST /detect`

Recebe uma imagem (`jpg`, `jpeg` ou `png`) via `multipart/form-data` e retorna as detecções.

Exemplo de resposta:

```json
{
  "model": "classroom_yolov8n_e50_best.pt",
  "filename": "example.jpg",
  "num_detections": 1,
  "inference_ms": 251.61,
  "detections": [
    {
      "class_id": 14,
      "class_name": "laptop",
      "confidence": 0.9592918157577515
    }
  ]
}
```

## Testes locais

### Testar `/health`

```powershell
curl.exe http://127.0.0.1:8000/health
```

### Testar `/detect`

Exemplo com uma imagem do dataset:

```powershell
$img="datasets\objects-in-the-classroom\data\images\test\laptop_194.jpg"
curl.exe -X POST "http://127.0.0.1:8000/detect" -F "file=@$img"
```

Também existe um script Python de teste em:

```text
vision/scripts/test_api_detect.py
```

## Integração com o app Android

O backend é consumido pelo aplicativo Android do projeto.

Durante testes com emulador Android, o app acessa o backend local usando:

```text
http://10.0.2.2:8000
```

Esse endereço permite que o emulador acesse o servidor rodando na máquina host.

Fluxo atual da integração:

1. usuário seleciona uma imagem no app Android
2. app envia a imagem para o endpoint `/detect`
3. backend executa inferência com YOLO
4. backend retorna JSON com as detecções
5. app exibe o resultado
6. app lê o resultado em voz alta com Text-to-Speech

## Dataset

Dataset utilizado:

* nome: Objects in the Classroom
* número de classes: 20
* formato: YOLO
* splits:

  * train: 3200 imagens
  * val: 640 imagens
  * test: 160 imagens

Classes:

```text
table, chair, whiteboard, bookshelf, clock, wall-magazine, trash-can,
eraser, sharpener, pen, book, ruler, scissor, fan, laptop,
remote-control, bag, pants, shoes, hat
```

O dataset não é versionado no GitHub. As instruções locais ficam em:

```text
datasets/README.md
```

## Status atual

* Dataset classroom definido
* Modelo YOLOv8n treinado por 50 epochs
* Avaliação realizada no conjunto de teste
* Backend FastAPI funcional
* Endpoint `/detect` retornando detecções em JSON
* Backend integrado ao app Android
* App Android já envia imagem, recebe resposta e fala o resultado

## Próximos passos

* comparar o modelo YOLOv8n atual com modelos leves mais recentes, como YOLO26n
* avaliar métricas, tamanho do modelo, tempo de inferência e viabilidade de exportação para mobile
* exportar o modelo selecionado para formato mobile, como TFLite/LiteRT
* iniciar integração on-device no aplicativo Android
* comparar a arquitetura cliente-servidor atual com a futura arquitetura on-device
* gerar diagramas finais de arquitetura, fluxo de execução e pipeline de treinamento/inferência

## Autor

João Pedro Piccino Marafiotti