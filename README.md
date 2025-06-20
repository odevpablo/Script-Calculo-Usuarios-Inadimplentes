# Notificador de Quantidade de Motos por Filial

## Descrição
Este script processa dados de uma planilha CSV com informações de filiais e classifica as filiais de acordo com os gestores responsáveis. Em seguida, dispara notificações para webhooks configurados no Microsoft Teams, informando a quantidade de motos em cada filial sob responsabilidade de cada gestor.

---

## Funcionalidades
1. **Carregamento de dados CSV**: Lê informações de um arquivo CSV contendo dados das filiais e suas respectivas quantidades de motos.
2. **Classificação por gestor**: Determina o gestor responsável por cada filial com base em uma tabela predefinida.
3. **Notificações automatizadas**: Envia notificações personalizadas para cada gestor via webhooks do Microsoft Teams.
4. **Agrupamento de informações por gestor**: Consolida os dados de todas as filiais de um gestor em uma única mensagem.

---

## Pré-requisitos
- Python 3.7 ou superior
- Bibliotecas necessárias:
  - `csv` (nativa do Python)
  - `pymsteams` (instale via `pip install pymsteams`)

---

## Estrutura do CSV
O arquivo CSV deve conter pelo menos uma coluna chamada `filial`, onde cada linha representa o nome da filial.

**Exemplo de estrutura:**
```csv
filial,quantidade_motos
Mottu São Paulo,100
Mottu Rio de Janeiro,80
Mottu Belo Horizonte,120
```

---

## Configuração

1. **URLs dos Webhooks**  
   Certifique-se de configurar as URLs corretas dos webhooks do Microsoft Teams no dicionário `webhooks` dentro do código.

2. **Arquivo CSV**  
   Substitua o valor da variável `caminho_arquivo` com o caminho para o seu arquivo CSV.

---

## Como usar
1. Clone este repositório ou copie o script para o seu ambiente local.
2. Instale as dependências necessárias com:
   ```bash
   pip install pymsteams
   ```
3. Prepare o arquivo CSV seguindo a estrutura descrita.
4. Execute o script:
   ```bash
   python script.py
   ```

---

## Fluxo do Script
1. O script carrega os dados do CSV usando a função `carregar_dados_csv`.
2. Conta a quantidade de motos por filial através de `contar_motos_por_filial`.
3. Classifica cada filial em um grupo de gestão com base na função `classificar_filial_por_gestor`.
4. Agrupa mensagens de cada gestor e dispara notificações utilizando `disparar_webhook`.

---

## Exemplo de Notificação no Microsoft Teams
**Título:** Notificação de quantidade de motos por filial  
**Mensagem:**
```
As seguintes filiais possuem motos:
- Mottu São Paulo (100 motos)
- Mottu Rio de Janeiro (80 motos)
```

---

## Observações
- Certifique-se de que as filiais no CSV correspondem aos nomes usados na classificação de gestores.
- Se uma filial não for atribuída a nenhum gestor, ela será ignorada.

---

## Possíveis Erros e Soluções
1. **Erro: Arquivo CSV não encontrado**
   - Certifique-se de que o caminho do arquivo esteja correto.
2. **Erro ao enviar webhook**
   - Verifique a URL do webhook correspondente no dicionário `webhooks`.
   - Confirme que o Microsoft Teams permite conexões externas para o webhook configurado.

---

## Contato
Em caso de dúvidas ou sugestões, entre em contato com o desenvolvedor.
