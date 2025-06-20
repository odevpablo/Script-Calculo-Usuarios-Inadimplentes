import csv
import pymsteams

# URLs das webhooks
webhooks = {
    "Gestor1": f"https://prod-10.brazilsouth.logic.azure.com:443/workflows/49d62273f0354e8e844d3ac81a43e7d6/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=7sPDGCXeSQp84gxuyjz3dOBg-ZZJ59mwKX1C0oGKA60",
    "Gestor2": f"https://prod-10.brazilsouth.logic.azure.com:443/workflows/49d62273f0354e8e844d3ac81a43e7d6/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=7sPDGCXeSQp84gxuyjz3dOBg-ZZJ59mwKX1C0oGKA60",
    "Gestor3": f"https://prod-10.brazilsouth.logic.azure.com:443/workflows/49d62273f0354e8e844d3ac81a43e7d6/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=7sPDGCXeSQp84gxuyjz3dOBg-ZZJ59mwKX1C0oGKA60",
    "Gestor4": f"https://prod-10.brazilsouth.logic.azure.com:443/workflows/49d62273f0354e8e844d3ac81a43e7d6/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=7sPDGCXeSQp84gxuyjz3dOBg-ZZJ59mwKX1C0oGKA60"
}

def carregar_dados_csv(caminho_csv):
    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_csv}' não encontrado.")
        return []

def contar_motos_por_filial(dados):
    motos_por_filial = {}

    for linha in dados:
        filial = linha.get('filial', '').strip()

        if not filial:
            continue

        motos_por_filial[filial] = motos_por_filial.get(filial, 0) + 1

    return motos_por_filial

def classificar_filial_por_gestor(filial):
    classificacoes = {
        "Gestor1": {
            "Mottu Anápolis", "Mottu Arapiraca", "Mottu Brasília", "Mottu Campina Grande", "Mottu Contagem", 
            "Mottu Feira de Santana", "Mottu Florianópolis", "Mottu Franca", "Mottu Imperatriz", "Mottu Joinville", 
            "Mottu Juazeiro do Norte", "Mottu Maceió", "Mottu Marabá", "Mottu Maringá", "Mottu Montes Claros", 
            "Mottu Mossoró", "Mottu Palmas", "Mottu Parauapebas", "Mottu Piracicaba", "Mottu Rio Branco", 
            "Mottu Santarém", "Mottu São José do Rio Preto", "Mottu Uberaba"
        },
        "Gestor2": {
            "Mottu Aracaju", "Mottu Belo Horizonte", "Mottu Boa Vista", "Mottu Campo Grande", "Mottu Caruaru", 
            "Mottu Juazeiro", "Mottu Macapá", "Mottu Porto Velho", "Mottu São José dos Campos", "Mottu Sorocaba", 
            "Mottu Uberlândia", "Mottu Vitória", "Mottu Vila Velha", "Mottu Porto Alegre"
        },
        "Gestor3": {
            "Mottu Belém", "Mottu Cuiabá", "Mottu Curitiba", "Mottu Fortaleza", "Mottu Goiânia", "Mottu João Pessoa", 
            "Mottu Manaus", "Mottu Natal", "Mottu Olinda", "Mottu Recife", "Mottu Ribeirão Preto", "Mottu Salvador", 
            "Mottu São Luís", "Mottu Teresina"
        },
        "Gestor4": {
            "Mottu Alagoinhas", "Mottu Ananindeua", "Mottu Aparecida de Goiânia", "Mottu Araçatuba", "Mottu Bauru", 
            "Mottu Camaçari", "Mottu Caxias do Sul", "Mottu Criciúma", "Mottu Divinópolis", "Mottu Fátima", 
            "Mottu Governador Valadares", "Mottu Ipatinga", "Mottu Itabuna", "Mottu Itajaí", "Mottu Juiz De Fora", 
            "Mottu Linhares", "Mottu Londrina", "Mottu Maracanaú", "Mottu Niterói", "Mottu Parnaíba", "Mottu Pelotas", 
            "Mottu Piçarreira", "Mottu Rio Verde", "Mottu Rondonópolis", "Mottu São Carlos", "Mottu Sobral", 
            "Mottu Vitória da Conquista", "Mottu Parnamirim"
        }
    }

    for gestor, filiais in classificacoes.items():
        if filial in filiais:
            return gestor

def disparar_webhook(gestor, mensagens):
    url = webhooks.get(gestor)
    if url:
        try:
            message = pymsteams.connectorcard(url)
            message.text(f"<b>Notificação de quantidade de motos por filial:</b><br>{mensagens.replace('\n', '<br>')}")
            message.send()
            print(f"Webhook disparada com sucesso para {gestor}.")
        except Exception as e:
            print(f"Erro ao enviar mensagem para {gestor}: {e}")
    else:
        print(f"Nenhuma webhook configurada para o gestor {gestor}.")

def processar_e_classificar(caminho_csv):
    dados = carregar_dados_csv(caminho_csv)

    if not dados:
        return

    motos_por_filial = contar_motos_por_filial(dados)

    mensagens_por_gestor = {}

    for filial, quantidade_motos in motos_por_filial.items():
        gestor = classificar_filial_por_gestor(filial)
        mensagem = f"- {filial} ({quantidade_motos} motos)"
        if gestor not in mensagens_por_gestor:
            mensagens_por_gestor[gestor] = mensagem
        else:
            mensagens_por_gestor[gestor] += "\n" + mensagem

    for gestor, mensagens in mensagens_por_gestor.items():
        mensagem_final = f"As seguintes filiais possuem motos:<br>{mensagens.replace('\n', '<br>')}"
        disparar_webhook(gestor, mensagem_final)

caminho_arquivo = "dados.csv"
processar_e_classificar(caminho_arquivo)
