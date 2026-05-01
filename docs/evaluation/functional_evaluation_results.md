# Resultados da avaliação funcional preliminar

## Objetivo

Este documento registra os resultados da avaliação funcional preliminar do protótipo integrado, composto pelo aplicativo Android, backend FastAPI e modelo YOLOv8n fine-tuned no dataset Objects in the Classroom.

A avaliação teve como objetivo verificar se o backend, ao receber imagens pelo endpoint `/detect`, retorna a classe esperada para imagens representativas do conjunto de teste.

---

## Configuração da avaliação

| Item | Valor |
|---|---|
| Modelo utilizado | `classroom_yolov8n_e50_best.pt` |
| Backend | FastAPI local |
| Endpoint | `POST /detect` |
| Dataset | Objects in the Classroom |
| Split utilizado | test |
| Número de imagens | 20 |
| Critério de seleção | 1 imagem por classe |
| Critério de acerto | a classe esperada aparece entre as detecções |
| Arquivo bruto de resultados | `functional_test_results.csv` |

---

## Resumo dos resultados

Foram avaliadas 20 imagens do conjunto de teste, sendo uma imagem para cada classe do dataset. O modelo retornou corretamente a classe esperada em 18 das 20 imagens avaliadas.

| Métrica funcional | Valor |
|---|---:|
| Total de imagens avaliadas | 20 |
| Casos corretos | 18 |
| Casos com erro | 2 |
| Arquivos não encontrados | 0 |
| Taxa de acerto funcional preliminar | 90% |

---

## Tabela de resultados

| Classe esperada | Objetos detectados | Status |
|---|---|---|
| table | table | correto |
| chair | chair, chair | correto |
| whiteboard | whiteboard | correto |
| bookshelf | bookshelf, bookshelf | correto |
| clock | clock | correto |
| wall-magazine | wall-magazine | correto |
| trash-can | sharpener, remote-control | erro |
| eraser | sharpener | erro |
| sharpener | sharpener, sharpener, sharpener, sharpener, sharpener, sharpener, sharpener | correto |
| pen | pen | correto |
| book | book | correto |
| ruler | ruler | correto |
| scissor | scissor | correto |
| fan | fan | correto |
| laptop | laptop | correto |
| remote-control | remote-control | correto |
| bag | bag | correto |
| pants | shoes, pants | correto |
| shoes | shoes | correto |
| hat | hat | correto |

---

## Análise preliminar

A avaliação funcional mostrou que o protótipo integrado foi capaz de detectar corretamente a classe esperada em 18 das 20 imagens avaliadas, resultando em uma taxa de acerto funcional preliminar de 90%.

Os dois erros ocorreram nas classes:

- `trash-can`, detectada como `sharpener` e `remote-control`;
- `eraser`, detectada como `sharpener`.

Esses erros indicam possíveis confusões visuais entre objetos pequenos ou com características semelhantes dentro do dataset. Mesmo assim, o resultado geral sugere que o modelo fine-tuned apresenta desempenho funcional adequado para uma primeira versão do protótipo.

---

## Relação com o aplicativo Android

Além da avaliação via script, o modelo também foi testado no fluxo ponta-a-ponta com o aplicativo Android em emulador. Nesse fluxo, o app seleciona uma imagem, envia para o backend, recebe o JSON com as detecções, apresenta os objetos detectados na interface e lê o resultado em voz alta usando Text-to-Speech.

Assim, esta avaliação complementa os testes do aplicativo ao registrar de forma sistemática o comportamento do backend com 20 imagens do conjunto de teste.

---

## Limitações

Esta avaliação é preliminar e possui algumas limitações:

- foi utilizada apenas uma imagem por classe;
- as imagens vieram do conjunto de teste do próprio dataset;
- os testes foram realizados com backend local;
- a avaliação funcional não substitui métricas quantitativas como precision, recall, mAP50 e mAP50-95;
- os resultados podem variar com imagens reais capturadas em ambientes educacionais diferentes.

---

## Conclusão

A avaliação funcional preliminar indica que o protótipo integrado é capaz de executar o fluxo principal de detecção de objetos com bom desempenho inicial. O sistema retornou a classe esperada em 90% dos casos avaliados, reforçando a viabilidade da arquitetura cliente-servidor implementada para reconhecimento de objetos em contexto educacional.