# Jungle Pathing
<br>
<div align="center" style="display: flex; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/f8964242-f77b-426e-a08b-d7e022d326c2" style="width: 15%;">
</div>
<br>

Este repositório consiste em acessar a **API da Riot Games** para selecionar e analisar um jogo de SoloQ, focando no mapeamento
do ”Jungle Pathing” de um jogador específico que atuou como jungler.

## Estrutura do Projeto

1. **Código Python
main.py**: Script principal responsável por:
Obter o PUUID do jogador utilizando o nome de invocador e tag line.
Coletar os IDs das partidas recentes jogadas pelo jogador.
Selecionar e extrair detalhes de uma partida específica.
Processar os dados da partida para extrair informações detalhadas do jungler.
Gerar uma visualização do jungle pathing (com limitações discutidas nos resultados).
2. **Dashboard Power BI**
O dashboard foi desenvolvido para visualizar as principais métricas de desempenho do jungler durante a partida. Os dados são apresentados de forma clara e visualmente atraente, utilizando gráficos de barras, KPIs, e outras visualizações.
3. **Dados
.csv/.xlsx**: Arquivo contendo os dados organizados e transformados para serem importados no Power BI.

## Para Executar

**Pré-requisitos**: <br>
Python 3.x

**Bibliotecas Python**:<br>
`requests`
`pandas`
`matplotlib`
`python-dotenv`

### Passos para execução
Passos para Execução
**Obtenha a chave da API da Riot Games**:

- Crie uma conta no Portal de Desenvolvedores da Riot Games.
- Insira a chave da API no arquivo `.env.`

**Executar o Script Python**:

- Rode o script `main.py` para extrair e processar os dados da partida.<br>
- Os resultados serão gerados em um arquivo de dados que poderá ser importado no Power BI.<br>

**Importar os Dados no Power BI:**

- Abra o Power BI Desktop.
- Importe o arquivo .csv/.xlsx com os dados gerados pelo script.
- Ajuste as visualizações conforme necessário para explorar os dados.
- Você também pode abrir o Dashboard pronto localizado na pasta 'dashboard'.

## Documentação

Você encontrará um **relatório detalhado** documentando todo o projeto na pasta 'relatory'.

### Resultados
O projeto foi concluído com sucesso, com exceção de uma limitação na visualização do jungle pathing. 
O gráfico gerado apresenta valores de coordenadas baixos, resultando em uma visualização inadequada do trajeto do jungler no mapa. 
Este problema pode estar relacionado à extração incorreta dos valores de posição a partir da API da Riot Games.
Uma oportunidade incrível de aprendizado e experiência.

![dashboard](https://github.com/user-attachments/assets/f8127073-5b18-4f01-9b69-59d8cf0de25a)

