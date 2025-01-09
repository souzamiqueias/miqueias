# ChatBot com Inteligência Artificial para WhatsApp

Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.10 ou superior)
- Docker e docker compose
- Outras dependências listadas no arquivo `requirements.txt`

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt

## Baixar Arquivos Grandes

Para baixar e mover os arquivos grandes, siga os passos abaixo:

1. Obtenha os links diretos para os arquivos `torch_cpu.dll` e `dnnl.lib` no Google Drive.
2. Baixe manualmente os arquivos.
3. Mova os arquivos para o diretório `venv/Lib/site-packages/torch/lib`.
