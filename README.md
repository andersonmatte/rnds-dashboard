# Dashboard RNDS - Rede Nacional de Dados em Saúde

Este projeto cria um dashboard interativo utilizando Dash para visualização de dados da Rede Nacional de Dados em Saúde (RNDS).

## Descrição

O dashboard consome dados em formato JSON da RNDS e apresenta visualizações interativas através de gráficos e tabelas, facilitando a análise e compreensão dos dados de saúde.

## Tecnologias Utilizadas

- **Dash**: Framework Python para criação de aplicações web analíticas
- **Pandas**: Biblioteca para manipulação e análise de dados
- **Plotly**: Biblioteca para criação de gráficos interativos

## Instalação

Pré-requisitos:
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalar Dependências

Execute os seguintes comandos para instalar as bibliotecas necessárias:

```bash
pip install dash
pip install pandas
pip install plotly
```

Ou instale todas as dependências de uma vez:

```bash
pip install dash pandas plotly
```

## Estrutura do Projeto

```
rnds-dashboard/
├── README.md              # Este arquivo
├── app.py                 # Aplicação principal do dashboard
├── data/                  # Diretório para arquivos JSON da RNDS
│   └── sample_data.json   # Exemplo de dados
├── assets/                # Arquivos estáticos (CSS, imagens)
└── requirements.txt       # Lista de dependências
```

## Como Executar

1. Clone ou baixe este repositório
2. Instale as dependências conforme descrito acima
3. Coloque seu arquivo JSON da RNDS no diretório `data/`
4. Execute a aplicação:

```bash
python app.py
```

5. Abra seu navegador e acesse `http://127.0.0.1:8050`

## Funcionalidades

- Carregamento de dados JSON da RNDS
- Visualizações interativas com gráficos dinâmicos
- Filtros e seleções para análise exploratória
- Interface responsiva e intuitiva
- Atualização em tempo real dos dados

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está sob licença MIT.

## Contato

Para dúvidas ou sugestões, entre em contato através do repositório.
