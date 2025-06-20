# Script-Calculo-de-Percentual

## Visão Geral
Este notebook automatiza a análise de produtividade no tratamento de casos de inadimplência nas filiais, enviando relatórios via Microsoft Teams para os gestores regionais. O processo identifica filiais com baixo desempenho (menos de 15% de casos finalizados) e notifica os responsáveis.

## Pré-requisitos
- Acesso ao Google Cloud Platform (BigQuery)
- Python 3.7+
- Pacotes instalados:
  ```bash
  pip install google-cloud-bigquery pymsteams
  ```

## Estrutura do Código

### 1. Configurações Iniciais
- Instalação de dependências
- Definição dos webhooks para envio ao Microsoft Teams
- Conexão com o BigQuery

### 2. Funções Principais

**buscar_dados_bq()**
- Consulta os dados de serviços no BigQuery
- Filtra por:
  - Serviços de inadimplência
  - Eventos dos últimos 2 dias
  - Casos abertos pelo "Mottu Monitor" ou finalizados

**processar_dados(rows)**
- Contabiliza eventos por filial
- Classifica em categorias: "Aberto", "Finalizado" ou "Outro"

**regionais**
- Dicionário que mapeia filiais para seus respectivos gestores regionais

**classificar_filial(filial)**
- Identifica o gestor responsável por cada filial

**enviar_relatorio_teams(gestor, filiais_data)**
- Formata e envia mensagem via webhook
- Inclui:
  - Nome da filial
  - Percentual de finalização
  - Total de casos abertos
  - Quantidade finalizada

### 3. Fluxo Principal (main())
1. Executa a consulta no BigQuery
2. Processa os resultados
3. Filtra filiais com menos de 15% de casos finalizados
4. Agrupa por gestor regional
5. Envia relatórios individuais

## Critérios de Filtro
O relatório considera apenas filiais que:
- Possuem percentual de finalização abaixo de 15%
- Tiveram atividade no período analisado

## Frequência de Execução
O notebook é projetado para execução diária, analisando os dados do dia anterior.

## Personalização
Para adaptar o código:
1. Atualize o dicionário `webhooks` com novos gestores
2. Ajuste o dicionário `regionais` conforme mudanças na estrutura
3. Modifique a query SQL para alterar os critérios de filtro
4. Altere o limiar de 15% conforme necessidades operacionais

## Saída Esperada
Relatórios enviados via Microsoft Teams contendo:
- Lista de filiais com baixo desempenho
- Métricas de produtividade
- Agrupamento por gestor regional
