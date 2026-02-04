import math

# Leitura inicial do arquivo
t_values = []
N_values = []

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

if len(t_values) > 0:
    # Linearização: Y = ln(N)
    Y_values = [math.log(n) for n in N_values]
    X_values = t_values
    n = len(X_values)

    # Cálculo dos somatórios
    sum_x = sum(X_values)
    sum_x2 = sum(x**2 for x in X_values)
    sum_y = sum(Y_values)
    sum_xy = sum(x*y for x, y in zip(X_values, Y_values))

    # Matriz A e vetor b
    A = [[n, sum_x], [sum_x, sum_x2]]
    b = [sum_y, sum_xy]

    # Função Solver (Gauss)
    def solve_linear_system_2x2(matrix_A, vector_b):
        aug = [
            [matrix_A[0][0], matrix_A[0][1], vector_b[0]],
            [matrix_A[1][0], matrix_A[1][1], vector_b[1]]
        ]
        # Eliminação Forward
        pivot = aug[0][0]
        factor = aug[1][0] / pivot
        for j in range(3):
            aug[1][j] = aug[1][j] - factor * aug[0][j]
            
        # Substituição Backward
        x1 = aug[1][2] / aug[1][1]
        x0 = (aug[0][2] - aug[0][1] * x1) / aug[0][0]
        return x0, x1

    alpha_0, alpha_1 = solve_linear_system_2x2(A, b)

    # Recuperação dos parâmetros
    beta_0 = math.exp(alpha_0)
    beta_1 = alpha_1

    print("-" * 30)
    print("RESULTADOS DO AJUSTE")
    print("-" * 30)
    print(f"Beta_0 (Coeficiente Linear): {beta_0:.4f}")
    print(f"Beta_1 (Coeficiente Exponencial): {beta_1:.8f}")
    print(f"Equação Final: N = {beta_0:.4e} * e^({beta_1:.6e} * t)")
    print("-" * 30)

    # Estimativa solicitada
    N_target = 53307321157
    t_estimado = (math.log(N_target) - math.log(beta_0)) / beta_1

    print(f"Para N = {N_target}:")
    print(f"Idade estimada (t) = {t_estimado:.4f} anos")
    print("-" * 30)