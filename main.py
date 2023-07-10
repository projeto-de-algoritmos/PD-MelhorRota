import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


def calcular_custo(origem, destino, peso):
    # Função para calcular o custo entre um ponto de origem e um destino
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

def exibir_rota():
    origens = [int(x) for x in entry_origens.get().split(",")]
    destinos = [int(x) for x in entry_destinos.get().split(",")]
    pesos = [int(x) for x in entry_pesos.get().split(",")]
    capacidade_veiculo = int(entry_capacidade.get())

    rota = encontrar_rota_otimizada(origens, destinos, pesos, capacidade_veiculo)

    messagebox.showinfo("Rota otimizada", formatar_rota(rota))

def formatar_rota(rota):
    rota_formatada = ""
    for origem, destino in rota:
        rota_formatada += f"Origem: {origem}, Destino: {destino}\n"
    return rota_formatada

# Criar a janela da interface
window = tk.Tk()
window.title("Sistema de Recomendação de Rotas Otimizadas")

# Carregar a imagem
imagem = ImageTk.PhotoImage(Image.open("carro.png"))

# Exibir a imagem na janela
label_imagem = tk.Label(window, image=imagem)
label_imagem.pack()


# Criar os rótulos e campos de entrada
label_capacidade = tk.Label(window, text="Capacidade do Veículo: (Digite um número inteiro)")
entry_capacidade = tk.Entry(window)

label_origens = tk.Label(window, text="Origens:(separe os números com vírgula)")
entry_origens = tk.Entry(window)

label_destinos = tk.Label(window, text="Destinos:(separe os números com vírgula)")
entry_destinos = tk.Entry(window)

label_pesos = tk.Label(window, text="Pesos:(separe os números com vírgula)")
entry_pesos = tk.Entry(window)


# Criar o botão para exibir a rota
button_exibir_rota = tk.Button(window, text="Exibir Rota Otimizada", command=exibir_rota)

# Posicionar os elementos na janela

label_capacidade.pack()
entry_capacidade.pack()

label_origens.pack()
entry_origens.pack()

label_destinos.pack()
entry_destinos.pack()

label_pesos.pack()
entry_pesos.pack()



button_exibir_rota.pack()

# Iniciar o loop da interface
window.mainloop()
