# Avaliação do modelo YOLOv8n fine-tuned - Objects in the Classroom

## Objetivo

Este documento registra a avaliação preliminar do modelo YOLOv8n ajustado ao dataset **Objects in the Classroom**, utilizado no projeto de iniciação científica sobre reconhecimento de objetos para auxílio a usuários cegos em contexto educacional.

O objetivo desta avaliação é documentar o treinamento, os resultados quantitativos e as limitações iniciais do modelo treinado para posterior uso no artigo, monografia e relatório final.

---

## Dataset

O dataset utilizado foi o **Objects in the Classroom**, composto por imagens de objetos comuns em ambientes educacionais.

### Classes

O dataset possui 20 classes:

| ID | Classe |
|---:|---|
| 0 | table |
| 1 | chair |
| 2 | whiteboard |
| 3 | bookshelf |
| 4 | clock |
| 5 | wall-magazine |
| 6 | trash-can |
| 7 | eraser |
| 8 | sharpener |
| 9 | pen |
| 10 | book |
| 11 | ruler |
| 12 | scissor |
| 13 | fan |
| 14 | laptop |
| 15 | remote-control |
| 16 | bag |
| 17 | pants |
| 18 | shoes |
| 19 | hat |

### Divisão dos dados

| Split | Quantidade de imagens |
|---|---:|
| Train | 3200 |
| Validation | 640 |
| Test | 160 |

No conjunto de teste foram avaliadas 160 imagens contendo 198 instâncias anotadas.

---

## Modelo avaliado

O modelo utilizado foi o **YOLOv8n**, partindo de pesos pré-treinados e ajustado ao dataset Objects in the Classroom.

### Configuração geral

| Item | Valor |
|---|---|
| Modelo base | YOLOv8n |
| Framework | Ultralytics |
| Arquivo base | yolov8n.pt |
| Arquivo final | classroom_yolov8n_e50_best.pt |
| Número de classes | 20 |
| Epochs | 50 |
| Batch size | 16 |
| Image size | 640 |
| Hardware | Google Colab com GPU Tesla T4 |
| Device | CUDA:0 |
| Early stopping | patience = 15 |
| Ambiente | Python 3.12.13, Torch 2.10.0+cu128, Ultralytics 8.4.45 |

---

## Comando geral de treinamento

O treinamento foi executado no Google Colab com GPU Tesla T4, salvando os resultados no Google Drive.

Comando equivalente:

    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")

    results = model.train(
        data="/content/dataset/objects-in-the-classroom/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        patience=15,
        project="/content/drive/MyDrive/ic_yolo_runs",
        name="classroom_yolov8n_gpu_e50"
    )

---

## Resultados no conjunto de validação

Após o treinamento, o melhor modelo salvo em `best.pt` foi validado no conjunto de validação.

| Métrica | Valor |
|---|---:|
| Precision | 0.876 |
| Recall | 0.880 |
| mAP50 | 0.914 |
| mAP50-95 | 0.741 |

Esses resultados indicam bom desempenho geral do modelo no conjunto de validação, especialmente considerando que o modelo utilizado foi a versão nano do YOLOv8.

---

## Resultados no conjunto de teste

O modelo também foi avaliado no conjunto de teste separado, composto por 160 imagens e 198 instâncias.

| Métrica | Valor |
|---|---:|
| Precision | 0.866 |
| Recall | 0.870 |
| mAP50 | 0.900 |
| mAP50-95 | 0.746 |

O resultado no conjunto de teste sugere que o modelo apresentou boa capacidade de generalização dentro do dataset utilizado, mantendo desempenho próximo ao observado na validação.

---

## Resultados por classe no conjunto de teste

| Classe | Imagens | Instâncias | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|---:|
| table | 8 | 8 | 0.938 | 1.000 | 0.995 | 0.913 |
| chair | 8 | 18 | 0.821 | 0.512 | 0.695 | 0.403 |
| whiteboard | 8 | 8 | 0.958 | 1.000 | 0.995 | 0.856 |
| bookshelf | 8 | 13 | 0.742 | 0.769 | 0.847 | 0.602 |
| clock | 8 | 8 | 0.803 | 0.875 | 0.766 | 0.609 |
| wall-magazine | 8 | 8 | 1.000 | 0.924 | 0.995 | 0.912 |
| trash-can | 8 | 10 | 0.683 | 0.649 | 0.741 | 0.686 |
| eraser | 8 | 8 | 0.845 | 0.685 | 0.893 | 0.836 |
| sharpener | 8 | 18 | 0.624 | 0.830 | 0.742 | 0.677 |
| pen | 8 | 8 | 0.939 | 1.000 | 0.995 | 0.704 |
| book | 8 | 11 | 0.854 | 1.000 | 0.965 | 0.760 |
| ruler | 8 | 9 | 1.000 | 0.955 | 0.995 | 0.883 |
| scissor | 8 | 8 | 0.968 | 1.000 | 0.995 | 0.884 |
| fan | 8 | 9 | 0.859 | 0.778 | 0.775 | 0.563 |
| laptop | 8 | 8 | 0.978 | 1.000 | 0.995 | 0.942 |
| remote-control | 8 | 8 | 0.826 | 1.000 | 0.982 | 0.915 |
| bag | 8 | 9 | 0.931 | 1.000 | 0.995 | 0.615 |
| pants | 8 | 8 | 0.851 | 0.875 | 0.864 | 0.753 |
| shoes | 8 | 13 | 0.780 | 0.545 | 0.783 | 0.606 |
| hat | 8 | 8 | 0.914 | 1.000 | 0.995 | 0.803 |

---

## Observações sobre desempenho por classe

O modelo apresentou desempenho elevado em diversas classes, como `table`, `whiteboard`, `wall-magazine`, `pen`, `ruler`, `scissor`, `laptop`, `remote-control`, `bag` e `hat`.

Algumas classes apresentaram desempenho mais baixo em determinadas métricas, especialmente:

- `chair`, com mAP50-95 de 0.403;
- `fan`, com mAP50-95 de 0.563;
- `shoes`, com recall de 0.545;
- `trash-can`, com precision e recall mais moderados;
- `sharpener`, com precision de 0.624.

Essas diferenças podem estar relacionadas à variação visual dos objetos, número de instâncias, semelhança com outras classes, oclusões, qualidade das imagens ou características específicas do dataset.

---

## Tempo de inferência

Na avaliação do conjunto de teste em GPU Tesla T4, o tempo médio reportado foi:

| Etapa | Tempo médio |
|---|---:|
| Preprocess | 6.2 ms |
| Inference | 5.2 ms |
| Postprocess | 1.9 ms |

Esses tempos se referem ao ambiente de avaliação em GPU no Google Colab. Eles não devem ser confundidos com o tempo total percebido pelo usuário no aplicativo Android, que depende também de envio da imagem, execução local do backend, rede local/emulador e processamento da resposta.

---

## Avaliação do YOLOv8n pré-treinado

Também foi executada uma avaliação direta do `yolov8n.pt` pré-treinado no conjunto de teste do dataset Objects in the Classroom.

O resultado global foi:

| Modelo | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| YOLOv8n pré-treinado | 0.0123 | 0.130 | 0.00783 | 0.00447 |
| YOLOv8n fine-tuned 50 epochs | 0.866 | 0.870 | 0.900 | 0.746 |

Entretanto, essa comparação quantitativa direta deve ser interpretada com cuidado. O modelo YOLOv8n pré-treinado utiliza o vocabulário de classes do dataset COCO, enquanto o Objects in the Classroom possui uma taxonomia própria com 20 classes específicas. Assim, os índices de classe não correspondem diretamente entre os dois conjuntos.

Por esse motivo, o YOLOv8n pré-treinado foi considerado principalmente como baseline funcional inicial para validação do fluxo de inferência, enquanto o modelo fine-tuned foi considerado o modelo principal para o domínio específico do projeto.

---

## Integração com o backend

O modelo `classroom_yolov8n_e50_best.pt` foi integrado ao backend FastAPI por meio da variável de ambiente `MODEL_PATH`.

Exemplo de execução local:

    $env:MODEL_PATH="models/classroom_yolov8n_e50_best.pt"
    uvicorn app.main:app --reload

O endpoint `/detect` passou a retornar também o nome do modelo ativo, facilitando a rastreabilidade dos testes.

Exemplo de resposta:

    {
      "model": "classroom_yolov8n_e50_best.pt",
      "filename": "laptop_194.jpg",
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

Esse teste confirmou que o backend estava utilizando o modelo treinado no dataset Objects in the Classroom e retornando classes compatíveis com a taxonomia do projeto.

---

## Integração com o aplicativo Android

Após a integração do modelo ao backend, o aplicativo Android também foi testado em emulador.

O fluxo testado foi:

1. selecionar imagem no aplicativo;
2. enviar a imagem para o backend local;
3. executar inferência no backend;
4. receber resposta JSON;
5. converter o resultado em texto amigável;
6. exibir objetos detectados;
7. ler o resultado com Text-to-Speech.

Esse teste confirmou a integração ponta-a-ponta entre aplicativo Android, backend FastAPI e modelo YOLOv8n fine-tuned.

---

## Limitações

Esta avaliação ainda possui algumas limitações:

- os testes foram conduzidos em ambiente local e emulador Android;
- o modelo foi avaliado no dataset utilizado no projeto, mas ainda não foi testado com imagens reais coletadas em ambiente escolar/faculdade;
- a execução atual é cliente-servidor, não on-device;
- o tempo de inferência em GPU no Colab não representa diretamente o tempo de resposta no app;
- a avaliação funcional com imagens selecionadas ainda precisa ser documentada em tabela separada;
- o desempenho pode variar em imagens com iluminação, ângulo, oclusão ou composição diferentes das imagens do dataset.

---

## Próximos passos

Os próximos passos relacionados ao modelo e avaliação são:

1. realizar uma avaliação funcional com 15 a 20 imagens selecionadas;
2. registrar objetos esperados, objetos detectados, confiança e tempo de resposta;
3. documentar os resultados em tabela;
4. gerar diagramas de arquitetura e fluxo da solução;
5. incorporar os resultados ao artigo e à monografia;
6. avaliar futuramente testes em dispositivo físico e possível execução on-device.

---

## Resumo

O fine-tuning do YOLOv8n por 50 epochs no dataset Objects in the Classroom resultou em bom desempenho no conjunto de teste, com mAP50 de 0.900 e mAP50-95 de 0.746. O modelo foi integrado ao backend FastAPI e testado com sucesso no fluxo ponta-a-ponta com o aplicativo Android, tornando-se a versão principal atual do modelo de detecção do projeto.