# Dashboard RNDS - Rede Nacional de Dados em Saúde

Este projeto cria um dashboard interativo utilizando Dash para visualização de dados da Rede Nacional de Dados em
Saúde (RNDS).

## Descrição

O dashboard consome dados em formato JSON da RNDS e apresenta visualizações interativas através de gráficos e mapas,
facilitando a análise e compreensão dos dados de saúde em diferentes níveis geográficos e temporais.

## Tecnologias Utilizadas

- **Dash**: Framework Python para criação de aplicações web analíticas
- **Pandas**: Biblioteca para manipulação e análise de dados
- **Plotly**: Biblioteca para criação de gráficos interativos e mapas

## Instalação

Pré-requisitos:

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalar Dependências

Execute os seguintes comandos para instalar as bibliotecas necessárias:

```bash
pip install dash pandas plotly
```

Ou utilize o arquivo requirements:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
rnds-dashboard/
├── README.md                    # Este arquivo
├── app.py                       # Aplicação principal do dashboard
├── requirements.txt             # Lista de dependências
├── components/                  # Componentes de visualização
│   ├── grafico_bar_uf.py        # Gráfico de barras por UF
│   ├── grafico_pie_uf.py        # Gráfico de pizza por UF
│   ├── grafico_regiao.py        # Gráfico por região
│   └── grafico_mapa_brasil.py   # Mapa interativo do Brasil
├── layouts/                     # Layouts das abas do dashboard
│   ├── aba_uf.py                # Layout da aba por UF
│   ├── aba_regiao.py            # Layout da aba por região
│   └── aba_brasil.py            # Layout da aba do Brasil
├── services/                    # Serviços de dados
│   └── data_loader.py           # Carregamento e processamento de dados
└── data/                        # Diretório para arquivos de dados
    ├── rnds.json                # Dados da RNDS
    └── brasil_estados.geojson   # Dados geográficos do Brasil
```

## Como Executar

1. Clone ou baixe este repositório
2. Instale as dependências conforme descrito acima
3. Certifique-se de que os arquivos de dados estão no diretório `data/`:
    - `rnds.json` (dados da RNDS)
    - `brasil_estados.geojson` (dados geográficos)
4. Execute a aplicação:

```bash
python app.py
```

5. Abra seu navegador e acesse `http://127.0.0.1:8050`

## Funcionalidades

### Abas do Dashboard

- **Por UF**:
    - Gráfico de barras mostrando o total de registros por Unidade Federativa
    - Gráfico de pizza com a distribuição percentual por UF

- **Por Região**:
    - Gráfico de barras colorido agrupado por regiões do Brasil
    - Visualização consolidada por Norte, Nordeste, Centro-Oeste, Sudeste e Sul

- **Brasil**:
    - Mapa interativo do Brasil com visualização por regiões
    - Cores diferenciadas para cada região
    - Informações detalhadas em hover

### Características Técnicas

- **Carregamento de dados**: Processamento automático de JSON da RNDS
- **Transformação de dados**: Formatação de datas e conversão de tipos
- **Visualizações interativas**: Gráficos dinâmicos com Plotly
- **Mapas geográficos**: Visualização espacial dos dados
- **Interface responsiva**: Layout adaptável a diferentes telas
- **Organização modular**: Código estruturado em componentes reutilizáveis

## Formato dos Dados

O dashboard espera um arquivo JSON (`data/rnds.json`) com a seguinte estrutura:

```json
[
  {
    "co_anomes": "202401",
    "sg_uf": "SP",
    "no_uf": "São Paulo",
    "no_regiao_brasil": "Sudeste",
    "vl_indicador_calculado_uf": 1000000,
    "vl_indicador_calculado_reg": 5000000,
    "vl_indicador_calculado_br": 10000000,
    "dt_atualizacao": "2024-01-15T10:30:00"
  }
]
```

## Desenvolvimento

### Arquitetura

- **app.py**: Ponto de entrada da aplicação Dash
- **components/**: Componentes reutilizáveis de visualização
- **layouts/**: Estrutura das diferentes abas do dashboard
- **services/**: Lógica de negócio e processamento de dados

### Personalização

- Cores dos gráficos podem ser ajustadas nos arquivos de componentes
- Novas visualizações podem ser adicionadas criando novos componentes
- Layouts podem ser modificados para incluir diferentes elementos

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar issues e bugs
- Sugerir melhorias e novas funcionalidades
- Enviar pull requests com código

## Licença

Este projeto está sob licença MIT.

## Contato

Para dúvidas ou sugestões, entre em contato através do repositório.
