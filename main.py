import requests
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Carregar a chave da API do arquivo .env
load_dotenv()
RIOT_API_KEY = os.getenv('RIOT_API_KEY')

BASE_URL = "https://americas.api.riotgames.com"

# Função para acessar a API da Riot Games
def get_data_from_riot_api(endpoint, params=None):
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }
    response = requests.get(BASE_URL + endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar API: {response.status_code}")
        return None

# 1. Obter o puuid a partir do gameName e tagLine
def get_puuid(game_name, tag_line):
    endpoint = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    data = get_data_from_riot_api(endpoint)
    if data:
        return data['puuid']
    return None

# 2. Obter os matchs recentes
def get_recent_match_ids(puuid):
    endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
    data = get_data_from_riot_api(endpoint)
    return data

# 3. Obter os detalhes de um jogo específico
def get_match_details(match_id):
    endpoint = f"/lol/match/v5/matches/{match_id}"
    data = get_data_from_riot_api(endpoint)
    return data

# 4. Obter a linha do tempo de um jogo específico
def get_match_timeline(match_id):
    endpoint = f"/lol/match/v5/matches/{match_id}/timeline"
    data = get_data_from_riot_api(endpoint)
    if data and 'frames' in data['info']:
        return data
    else:
        print("Erro: 'frames' não encontrado na linha do tempo")
        return None

# 5. Processar os dados do jogo e extrair informações do jungler
def process_match_info(match_data, puuid):
    participant_data = None
    for participant in match_data['info']['participants']:
        if participant['puuid'] == puuid:
            participant_data = participant
            break

    if participant_data:
        match_info = {
            'championName': participant_data['championName'],
            'teamPosition': participant_data['teamPosition'],
            'individualPosition': participant_data['individualPosition'],
            'firstBloodKill': participant_data['firstBloodKill'],
            'kills': participant_data['kills'],
            'deaths': participant_data['deaths'],
            'assists': participant_data['assists'],
            'items': [participant_data[f'item{i}'] for i in range(7)],
            'neutralMinionsKilled': participant_data['neutralMinionsKilled'],
            'totalMinionsKilled': participant_data['totalMinionsKilled'],
            'dragonKills': participant_data['dragonKills'],
            'baronKills': participant_data['baronKills'],
            'wardsPlaced': participant_data['wardsPlaced'],
            'wardKilled': participant_data['wardsKilled'],
            'visionScore': participant_data['visionScore'],
            'inhibitorKills': participant_data['inhibitorKills'],
            'inhibitorsLost': participant_data['inhibitorsLost'],
            'goldEarned': participant_data['goldEarned'],
            'win': participant_data['win']
        }
        return match_info
    return None

# 6. Processar a linha do tempo e extrair o caminho do jogador
def extract_jungle_pathing(timeline_data, participant_id):
    pathing = []

    if not timeline_data:
        print("Erro: Linha do tempo vazia ou inválida.")
        return pathing

    for frame in timeline_data['info']['frames']:
        # Verificar eventos associados ao jungler
        for event in frame['events']:
            if event.get('participantId') == participant_id and 'position' in event:
                if event['type'] in ['ITEM_PURCHASED', 'CHAMPION_KILL']:
                    position = {
                        'timestamp': event['timestamp'],
                        'x': event['position']['x'],
                        'y': event['position']['y'],
                        'type': event['type']
                    }
                    pathing.append(position)

    # Ordenar as posições pelo timestamp
    pathing.sort(key=lambda x: x['timestamp'])
    return pathing

# 7. Visualizar o caminho do jogador
def plot_jungle_pathing(pathing):
    x_positions = [pos['x'] for pos in pathing]
    y_positions = [pos['y'] for pos in pathing]
    event_types = [pos['type'] for pos in pathing]
    
    plt.figure(figsize=(10, 10))
    plt.plot(x_positions, y_positions, marker='o', linestyle='-', color='blue')
    
    for i, event_type in enumerate(event_types):
        plt.text(x_positions[i], y_positions[i], event_type, fontsize=8, color='red')
    
    plt.title('Jungle Pathing')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.show()

# Main Function
def main():
    game_name = "FUR Wiz"
    tag_line = "CBLOL"

    # 1. Obter puuid
    puuid = get_puuid(game_name, tag_line)
    if not puuid:
        print("Erro ao obter puuid")
        return

    # 2. Obter o ID do jogo selecionado manualmente
    match_id = "BR1_2984065900"

    # 3. Obter detalhes do jogo
    match_data = get_match_details(match_id)
    if not match_data:
        print("Erro ao obter detalhes do jogo")
        return

    # 4. Processar as informações do jogo para o jungler
    match_info = process_match_info(match_data, puuid)
    if match_info:
        print("Informações do Jungler:", match_info)
    else:
        print("Jungler não encontrado")
        return

    # 5. Obter a linha do tempo do jogo
    timeline_data = get_match_timeline(match_id)
    if not timeline_data:
        print("Erro ao obter linha do tempo do jogo")
        return

    # 6. Extrair o caminho do jungler
    jungle_pathing = extract_jungle_pathing(timeline_data, puuid)

    # 7. Visualizar o caminho do jungler
    plot_jungle_pathing(jungle_pathing)

if __name__ == "__main__":
    main()