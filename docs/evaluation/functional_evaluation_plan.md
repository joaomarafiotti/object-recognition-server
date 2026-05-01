# Avaliação funcional preliminar do protótipo

## Objetivo

Este documento descreve a avaliação funcional preliminar do protótipo desenvolvido na iniciação científica. A avaliação tem como objetivo verificar se a solução cliente-servidor é capaz de receber imagens, executar detecção de objetos no backend e retornar resultados interpretáveis pelo aplicativo Android.

Esta avaliação complementa a avaliação quantitativa do modelo YOLOv8n fine-tuned, documentada em `model_evaluation_yolov8n_e50.md`.

---

## Protótipo avaliado

A solução avaliada é composta por:

- backend em Python/FastAPI;
- modelo YOLOv8n fine-tuned no dataset Objects in the Classroom;
- aplicativo Android em Kotlin/Jetpack Compose;
- comunicação via requisição HTTP multipart;
- resposta em JSON;
- exibição textual e leitura por voz no app Android.

Fluxo geral:

1. o usuário seleciona uma imagem;
2. o app envia a imagem ao backend;
3. o backend executa inferência com YOLO;
4. o backend retorna um JSON com as detecções;
5. o app interpreta e apresenta o resultado.

---

## Modelo utilizado

Modelo utilizado nos testes funcionais:

`classroom_yolov8n_e50_best.pt`

Esse modelo foi treinado por 50 epochs no dataset Objects in the Classroom.

Principais métricas no conjunto de teste:

| Métrica | Valor |
|---|---:|
| Precision | 0.866 |
| Recall | 0.870 |
| mAP50 | 0.900 |
| mAP50-95 | 0.746 |

---

## Ambiente de teste

| Item | Valor |
|---|---|
| Backend | FastAPI local |
| Endpoint | `POST /detect` |
| Modelo | `classroom_yolov8n_e50_best.pt` |
| Dataset | Objects in the Classroom |
| Split usado | test |
| Quantidade de imagens selecionadas | 20 |
| Critério de seleção | 1 imagem por classe |
| App Android | Testado em emulador |
| Backend local | `http://127.0.0.1:8000` |
| Emulador Android | usa `http://10.0.2.2:8000` para acessar o host |

---

## Imagens selecionadas

A avaliação funcional usa uma imagem de teste para cada uma das 20 classes do dataset.

| Classe esperada | Padrão de arquivo usado |
|---|---|
| table | `table_*` |
| chair | `chair_images-18-*` |
| whiteboard | `whiteboard-test-1.*` |
| bookshelf | `bookshelf-test-1.*` |
| clock | `clock-test-7.*` |
| wall-magazine | `walmegazine-test-1.*` |
| trash-can | `trashcan-test1.*` |
| eraser | `eraser193.*` |
| sharpener | `sharpener193.*` |
| pen | `pen193.*` |
| book | `book_fd526e72cac26aa8_jpg*` |
| ruler | `ruler193.*` |
| scissor | `scissor193.*` |
| fan | `fan_193.*` |
| laptop | `laptop_194.*` |
| remote-control | `remote-control_193.*` |
| bag | `bag_12-c608116e-ae57-403c-b447-88afd14b2_jpg*` |
| pants | `pants_image178_jpg*` |
| shoes | `shoes_193.*` |
| hat | `hat_image--209-*` |

---

## Critério de classificação funcional

Cada imagem é classificada automaticamente da seguinte forma:

| Status | Significado |
|---|---|
| correto | a classe esperada apareceu entre as detecções |
| erro | houve detecção, mas a classe esperada não apareceu |
| nenhuma_detecção | o modelo não retornou objetos |
| arquivo_não_encontrado | o arquivo de teste não foi encontrado no diretório local |

---

## Como executar

Antes de rodar a avaliação, iniciar o backend com o modelo treinado:

```powershell
$env:MODEL_PATH="models/classroom_yolov8n_e50_best.pt"
uvicorn app.main:app --reload
````

Em outro terminal, executar:

```powershell
py vision/scripts/run_functional_evaluation.py
```

O script gera o arquivo:

```text
docs/evaluation/functional_test_results.csv
```

---

## Resultado esperado

O arquivo CSV gerado deve conter, para cada imagem:

* classe esperada;
* arquivo usado;
* modelo ativo;
* quantidade de detecções;
* objetos detectados;
* maior confiança;
* tempo de inferência;
* status funcional.

---

## Observações

Esta avaliação é funcional e preliminar. Ela não substitui as métricas quantitativas obtidas no conjunto de teste, como precision, recall, mAP50 e mAP50-95. Seu objetivo é registrar evidências práticas de funcionamento do protótipo integrado.

Os resultados podem variar dependendo do limiar de confiança, da imagem selecionada e do ambiente de execução do backend.