# Exportação e avaliação TFLite dos modelos YOLO

## Objetivo

Este documento registra a exportação dos modelos YOLOv8n e YOLO26n para TensorFlow Lite, com foco na futura integração on-device no aplicativo Android.

A etapa foi realizada após a comparação dos modelos em formato PyTorch (`.pt`), considerando que o objetivo da iniciação científica é evoluir de uma arquitetura cliente-servidor para uma solução executada localmente no dispositivo móvel.

## Modelos exportados

Foram exportados dois modelos:

- YOLOv8n fine-tuned por 50 épocas;
- YOLO26n fine-tuned com configuração de 50 épocas e early stopping.

## Arquivos TFLite gerados

Os arquivos TFLite não são versionados no GitHub. Eles foram armazenados no Google Drive, dentro da pasta organizada da IC.

YOLOv8n:

```text
IC_Object_Recognition/06_exports_mobile/yolov8n_e50_float32_nms/classroom_yolov8n_e50_best_float32.tflite
````

YOLO26n:

```text
IC_Object_Recognition/06_exports_mobile/yolo26n_e50_float32_end2end/classroom_yolo26n_e50_best_float32.tflite
```

## Observação sobre NMS

Na exportação do YOLOv8n foi usado `nms=True`.

Na exportação do YOLO26n, o Ultralytics exibiu o aviso:

```text
'nms=True' is not available for end2end models. Forcing 'nms=False'.
```

Portanto, o YOLO26n foi exportado como modelo end-to-end, sem a mesma configuração explícita de NMS usada no YOLOv8n.

## Tamanho dos arquivos

| Modelo      | Formato        |  Tamanho |
| ----------- | -------------- | -------: |
| YOLOv8n e50 | TFLite Float32 | 11.78 MB |
| YOLO26n e50 | TFLite Float32 |  9.47 MB |

## Avaliação no test set com TFLite

Dataset: Objects in the Classroom

Test set:

* 160 imagens
* 198 instâncias

Configuração:

* image size: 640
* formato: TFLite Float32
* ambiente de avaliação: Google Colab
* framework: Ultralytics

| Modelo      | Formato        | Precision | Recall | mAP50 | mAP50-95 | Preprocess | Inference | Postprocess |
| ----------- | -------------- | --------: | -----: | ----: | -------: | ---------: | --------: | ----------: |
| YOLOv8n e50 | TFLite Float32 |     0.897 |  0.850 | 0.874 |    0.715 |     2.1 ms |  137.2 ms |      0.2 ms |
| YOLO26n e50 | TFLite Float32 |     0.869 |  0.837 | 0.894 |    0.727 |     1.8 ms |  114.1 ms |      0.2 ms |

## Comparação com modelos PyTorch

| Modelo      | Formato        | Precision | Recall | mAP50 | mAP50-95 |  Tamanho | Inferência |
| ----------- | -------------- | --------: | -----: | ----: | -------: | -------: | ---------: |
| YOLOv8n e50 | PyTorch `.pt`  |     0.866 |  0.870 | 0.900 |    0.746 |   6.3 MB |     5.2 ms |
| YOLO26n e50 | PyTorch `.pt`  |     0.889 |  0.831 | 0.899 |    0.734 |   5.4 MB |     8.6 ms |
| YOLOv8n e50 | TFLite Float32 |     0.897 |  0.850 | 0.874 |    0.715 | 11.78 MB |   137.2 ms |
| YOLO26n e50 | TFLite Float32 |     0.869 |  0.837 | 0.894 |    0.727 |  9.47 MB |   114.1 ms |

## Resultados por modelo

### YOLOv8n TFLite

Resultado no test set:

| Métrica   |  Valor |
| --------- | -----: |
| Precision | 0.8968 |
| Recall    | 0.8498 |
| mAP50     | 0.8736 |
| mAP50-95  | 0.7151 |

Tempo reportado:

| Etapa       |    Tempo |
| ----------- | -------: |
| Preprocess  |   2.1 ms |
| Inference   | 137.2 ms |
| Postprocess |   0.2 ms |

Resultado salvo em:

```text
ic_yolo_runs/classroom_yolov8n_e50_tflite_test_eval
```

### YOLO26n TFLite

Resultado no test set:

| Métrica   |  Valor |
| --------- | -----: |
| Precision | 0.8693 |
| Recall    | 0.8374 |
| mAP50     | 0.8944 |
| mAP50-95  | 0.7266 |

Tempo reportado:

| Etapa       |    Tempo |
| ----------- | -------: |
| Preprocess  |   1.8 ms |
| Inference   | 114.1 ms |
| Postprocess |   0.2 ms |

Resultado salvo em:

```text
ic_yolo_runs/classroom_yolo26n_e50_tflite_test_eval
```

## Análise preliminar

No formato PyTorch, o YOLOv8n apresentou maior recall, mAP50-95 e menor tempo de inferência no test set em GPU.

No formato TFLite Float32, o YOLO26n apresentou vantagens importantes para mobile:

* menor tamanho de arquivo;
* menor tempo de inferência no teste TFLite em Colab;
* maior mAP50;
* maior mAP50-95.

O YOLOv8n TFLite manteve maior precision e recall, mas sofreu maior queda em mAP50 e mAP50-95 em comparação com sua versão PyTorch.

## Conclusão provisória

Para a arquitetura cliente-servidor com modelo PyTorch, o YOLOv8n permanece como baseline forte.

Para a futura etapa on-device em Android, o YOLO26n TFLite se tornou um candidato forte, pois apresentou melhor relação entre tamanho, tempo de inferência TFLite e métricas mAP.

A decisão final ainda depende de testes reais no aplicativo Android, pois os tempos de inferência reportados aqui foram obtidos no ambiente Colab/TFLite e não em dispositivo móvel.