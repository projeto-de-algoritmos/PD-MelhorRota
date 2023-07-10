import numpy as np

def calcular_custo(origem, destino, peso):
    # Função para calcular o custo entre um ponto de origem e um destino
    # Neste exemplo, o custo será baseado na distância multiplicada pelo peso do pacote
    distancia = abs(destino - origem)
    return distancia * peso

def encontrar_rota_otimizada(origens, destinos, pesos, capacidade_veiculo):
    n = len(origens)
    dp = np.zeros((n, capacidade_veiculo+1))

    for i in range(n):
        for j in range(capacidade_veiculo+1):
            if j >= pesos[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-pesos[i]] + calcular_custo(origens[i], destinos[i], pesos[i]))
            else:
                dp[i][j] = dp[i-1][j]
    
    # Recupera a rota ótima a partir da tabela dp
    rota_otimizada = []
    i, j = n-1, capacidade_veiculo
    while i >= 0 and j >= 0:
        if i == 0 and dp[i][j] != 0:
            rota_otimizada.append((origens[i], destinos[i]))
            break
        elif dp[i][j] != dp[i-1][j]:
            rota_otimizada.append((origens[i], destinos[i]))
            j -= pesos[i]
        i -= 1

    return rota_otimizada[::-1]

# Exemplo de uso do sistema de recomendação de rotas otimizadas
origens = [1, 2, 3, 4]  # Pontos de origem
destinos = [2, 4, 1, 3]  # Pontos de destino
pesos = [2, 1, 3, 2]  # Pesos dos pacotes
capacidade_veiculo = 5

rota = encontrar_rota_otimizada(origens, destinos, pesos, capacidade_veiculo)
print("Rota otimizada:")
for origem, destino in rota:
    print(f"Origem: {origem}, Destino: {destino}")
