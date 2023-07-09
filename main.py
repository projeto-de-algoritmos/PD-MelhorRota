import numpy as np

def calcular_custo(origem, destino):
    # Função para calcular o custo entre um ponto de origem e um destino
    # Pode ser baseado em fatores como distância, tempo, prioridade, etc.
    # Retorna o custo total

def encontrar_rota_otimizada(origens, destinos, capacidade_veiculo):
    n = len(origens)
    dp = np.zeros((n, capacidade_veiculo+1))

    for i in range(n):
        for j in range(capacidade_veiculo+1):
            if j >= destinos[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-destinos[i]] + calcular_custo(origens[i], destinos[i]))
            else:
                dp[i][j] = dp[i-1][j]
    
    # Recupera a rota ótima a partir da tabela dp
    rota_otimizada = []
    i, j = n-1, capacidade_veiculo
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            rota_otimizada.append((origens[i], destinos[i]))
            j -= destinos[i]
        i -= 1

    return rota_otimizada[::-1]

# Exemplo de uso do sistema de recomendação de rotas otimizadas
origens = [1, 2, 3, 4]  # Pontos de origem
destinos = [2, 4, 1, 3]  # Pontos de destino
capacidade_veiculo = 5

rota = encontrar_rota_otimizada(origens, destinos, capacidade_veiculo)
print("Rota otimizada:")
for origem, destino in rota:
    print(f"Origem: {origem}, Destino: {destino}")
