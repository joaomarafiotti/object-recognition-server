# datasets

Este diretório é usado para armazenar datasets locais utilizados no projeto.

## Dataset atual
- **Nome:** Objects in the Classroom
- **Fonte:** Kaggle
- **Link:** https://www.kaggle.com/datasets/aryakrisnaputra/objects-in-the-classroom

## Observação
Os arquivos do dataset **não são versionados no GitHub**.

Para usar o dataset neste projeto:
1. baixe o arquivo manualmente no Kaggle
2. extraia o conteúdo em:

`datasets/objects-in-the-classroom/`

## Estrutura esperada
O projeto espera uma estrutura semelhante a esta:

```text
datasets/
  objects-in-the-classroom/
    data/
      images/
        train/
        val/
        test/
      labels/
        train/
        val/
        test/
    data.yaml
````

## Arquivo de configuração usado pelo projeto

A configuração local do dataset utilizada pelo treinamento está em:

`configs/classroom_data.yaml`