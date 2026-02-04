import math

# Leitura inicial do arquivo
t_values = []
N_values = []

# Vamos assumir que o arquivo existe por enquanto
with open('carbono14.txt', 'r') as arquivo:
    for linha in arquivo:
        parts = linha.split()
        if len(parts) >= 2:
            try:
                t = float(parts[-2])
                N = float(parts[-1])
                t_values.append(t)
                N_values.append(N)
            except ValueError:
                continue

print(f"Dados carregados: {len(t_values)} amostras.")