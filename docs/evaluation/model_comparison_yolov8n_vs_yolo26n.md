# Comparação YOLOv8n vs YOLO26n

## Objetivo

Esta comparação foi realizada para justificar a escolha do modelo principal do projeto de iniciação científica, considerando a evolução planejada de uma arquitetura cliente-servidor para uma solução mobile/on-device.

A comparação também responde à questão metodológica sobre o uso do YOLOv8n em vez de outras versões mais recentes ou mais robustas da família YOLO.

Foram comparados dois modelos leves:

- YOLOv8n, usado como baseline atual do projeto;
- YOLO26n, avaliado como alternativa mais recente com foco em cenários edge/mobile.

## Dataset

Dataset: Objects in the Classroom

Formato: YOLO

Número de classes: 20

Splits:

- train: 3200 imagens
- validation: 640 imagens
- test: 160 imagens

Classes:

```text
table, chair, whiteboard, bookshelf, clock, wall-magazine, trash-can,
eraser, sharpener, pen, book, ruler, scissor, fan, laptop,
remote-control, bag, pants, shoes, hat
````

## Protocolo experimental

Os dois modelos foram treinados e avaliados com o mesmo dataset e o mesmo protocolo geral.

Configuração geral:

* framework: Ultralytics
* ambiente: Google Colab
* GPU: Tesla T4
* image size: 640
* batch size: 16
* treinamento com pesos pré-treinados
* avaliação no mesmo conjunto de teste

O YOLOv8n foi treinado por 50 épocas. O YOLO26n foi configurado para 50 épocas, mas parou antecipadamente por early stopping após 48 épocas, com melhor resultado observado na época 33.

## YOLOv8n

Run de treinamento:

```text
ic_yolo_runs/classroom_yolov8n_gpu_e50
```

Modelo final:

```text
classroom_yolov8n_e50_best.pt
```

Configuração:

* modelo base: yolov8n.pt
* epochs: 50
* tempo aproximado de treino: 0.838 horas
* melhor modelo salvo como: best.pt

Resultado no test set:

| Métrica   | Valor |
| --------- | ----: |
| Precision | 0.866 |
| Recall    | 0.870 |
| mAP50     | 0.900 |
| mAP50-95  | 0.746 |

Tempos reportados no test set:

| Etapa       |  Tempo |
| ----------- | -----: |
| Preprocess  | 6.2 ms |
| Inference   | 5.2 ms |
| Postprocess | 1.9 ms |

Características do modelo:

| Item               |                  Valor |
| ------------------ | ---------------------: |
| Parâmetros         |  aproximadamente 3.01M |
| GFLOPs             |    aproximadamente 8.1 |
| Tamanho do best.pt | aproximadamente 6.3 MB |

## YOLO26n

Run de treinamento:

```text
ic_yolo_runs/classroom_yolo26n_gpu_e50
```

Modelo final:

```text
classroom_yolo26n_e50_best.pt
```

Configuração:

* modelo base: yolo26n.pt
* epochs solicitadas: 50
* parada antecipada: epoch 48
* melhor época: epoch 33
* tempo aproximado de treino: 0.967 horas
* melhor modelo salvo como: best.pt

Resultado no validation set após treinamento:

| Métrica   | Valor |
| --------- | ----: |
| Precision | 0.890 |
| Recall    | 0.826 |
| mAP50     | 0.911 |
| mAP50-95  | 0.745 |

Resultado no test set:

| Métrica   | Valor |
| --------- | ----: |
| Precision | 0.889 |
| Recall    | 0.831 |
| mAP50     | 0.899 |
| mAP50-95  | 0.734 |

Tempos reportados no test set:

| Etapa       |  Tempo |
| ----------- | -----: |
| Preprocess  | 6.9 ms |
| Inference   | 8.6 ms |
| Postprocess | 0.4 ms |

Características do modelo:

| Item               |                  Valor |
| ------------------ | ---------------------: |
| Parâmetros         |                  2.38M |
| GFLOPs             |                    5.2 |
| Tamanho do best.pt | aproximadamente 5.4 MB |

## Tabela comparativa no test set

| Modelo      | Precision | Recall | mAP50 | mAP50-95 | Parâmetros | GFLOPs | best.pt | Inference |
| ----------- | --------: | -----: | ----: | -------: | ---------: | -----: | ------: | --------: |
| YOLOv8n e50 |     0.866 |  0.870 | 0.900 |    0.746 |     ~3.01M |   ~8.1 |  6.3 MB |    5.2 ms |
| YOLO26n e50 |     0.889 |  0.831 | 0.899 |    0.734 |     ~2.38M |   ~5.2 |  5.4 MB |    8.6 ms |

## Análise

O YOLO26n apresentou maior precision, menor número de parâmetros, menor custo computacional em GFLOPs e menor tamanho de arquivo. Esses fatores tornam o modelo interessante para cenários mobile, edge e futuras etapas on-device.

Por outro lado, o YOLOv8n apresentou maior recall, mAP50 ligeiramente superior, mAP50-95 superior e menor tempo de inferência no test set executado em GPU Tesla T4.

Como o projeto tem finalidade assistiva, o recall é uma métrica especialmente relevante. Em um sistema de apoio a usuários cegos, deixar de detectar objetos presentes pode comprometer a utilidade prática da aplicação. Por isso, o melhor desempenho do YOLOv8n em recall e mAP50-95 é um ponto importante a favor de sua manutenção como modelo principal no baseline atual.

## Conclusão provisória

A comparação indica que a escolha inicial do YOLOv8n foi tecnicamente justificável. Embora o YOLO26n seja mais leve e tenha apresentado maior precision, ele não superou o YOLOv8n nas métricas de recall, mAP50-95 e tempo de inferência neste experimento.

Assim, o YOLOv8n permanece como candidato principal para a versão atual do projeto, enquanto o YOLO26n permanece como alternativa relevante para investigação de exportação e execução mobile/on-device.

A próxima etapa será testar a viabilidade de exportação dos modelos para formato mobile, como TFLite/LiteRT, e avaliar o comportamento em execução local no Android.