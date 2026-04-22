# Treino mínimo YOLOv8n (1 epoch)

## Ambiente
- Máquina: Windows 11, Intel i5-1135G7, 32GB RAM
- Execução: CPU
- Dataset: Objects in the Classroom (formato YOLO)
- Nº classes (nc): 20

## Dataset (estrutura confirmada)
datasets/objects-in-the-classroom/data/
- images/{train,val,test}
- labels/{train,val,test}
- data.yaml (original do dataset)

## Configuração usada
Arquivo: `configs/classroom_data.yaml`
- path: `datasets/objects-in-the-classroom/data`
- train/val/test: `images/train`, `images/val`, `images/test`
- nc = 20 (classes do classroom)

## Comando executado (treino mínimo)
yolo detect train model=yolov8n.pt data=configs/classroom_data.yaml epochs=1 imgsz=640 batch=4 device=cpu workers=2 project=runs/train name=classroom_yolov8n_e1

## Principais resultados (epoch 1)
Métricas globais ("all"):
- precision: 0.399
- recall: 0.435
- mAP50: 0.391
- mAP50-95: 0.255

Tempo por imagem (log):
- preprocess: 1.5ms
- inference: 82.6ms
- postprocess: 2.8ms

> Observação: este foi um treino mínimo (apenas 1 epoch) para validação do pipeline. As métricas ainda não representam desempenho final do modelo.

## Artefatos gerados localmente
Diretório de saída (YOLO):
- runs/.../classroom_yolov8n_e1/

Arquivos importantes:
- `weights/best.pt`
- `weights/last.pt`
- `results.csv`
- `args.yaml`
- gráficos e matrizes:
  - `confusion_matrix.png`, `confusion_matrix_normalized.png`
  - `results.png` e curvas (BoxF1, PR, P, R)
  - `val_batch*_pred.jpg` (exemplos de predição no val)

## Próximos passos imediatos
1) Rodar `predict` com `best.pt` em poucas imagens e salvar exemplos (sem abrir janelas).
2) Repetir treino com mais epochs (ex.: 5–20) para medir ganho real.
3) Iniciar API mínima (FastAPI) carregando `best.pt` e retornando lista de objetos.

### Trecho do log (val)
all 640 796 0.399 0.435 0.391 0.255
Speed: 1.5ms preprocess, 82.6ms inference, 2.8ms postprocess per image
Results saved to ...\classroom_yolov8n_e1

## Evidência visual (predict com best.pt)
Após o treino mínimo (1 epoch), rodei inferência em 5 imagens do conjunto de teste para validar o pipeline ponta-a-ponta.

Comando:
yolo detect predict model=runs/.../weights/best.pt source=temp_predict/images save=True conf=0.25 imgsz=640 project=runs/predict name=classroom_best_e1

Saída local:
runs/predict/classroom_best_e1/ (imagens com bounding boxes)

Observação (qualitativa):
- Como o treino foi mínimo (apenas 1 epoch), as predições ainda apresentam baixa qualidade e confusões entre classes.
- Esse resultado é esperado nesta etapa e serve como evidência de funcionamento do pipeline e como diagnóstico inicial.
- Próximo passo: aumentar epochs (ex.: 5–20) e repetir a avaliação visual + métricas para observar melhora real.