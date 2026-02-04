# Ajuste de Curvas: Datação por Carbono-14 🧪📉

> Trabalho prático da disciplina de **Algoritmos Numéricos** (UFES).
> Implementação "from scratch" (do zero) de métodos de regressão e álgebra linear.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📄 Sobre o Projeto

Este projeto tem como objetivo estimar a idade de amostras fósseis ou arqueológicas baseando-se na concentração residual de **Carbono-14**. 

Para isso, foi desenvolvido um software que realiza o **Ajuste de Curvas (Regressão)** sobre um conjunto de dados históricos, encontrando a equação que melhor descreve o decaimento radioativo da amostra.

### 🎯 O Desafio Técnico
A principal restrição deste trabalho foi a **proibição do uso de bibliotecas de álgebra linear ou estatística** (como `numpy`, `pandas`, `scikit-learn` ou `scipy`). 

Toda a lógica matemática foi implementada puramente em Python, incluindo:
1.  **Linearização de Modelo Exponencial** (aplicação de logaritmos).
2.  **Método dos Mínimos Quadrados** (montagem das equações normais).
3.  **Eliminação de Gauss** (resolução do sistema linear $Ax = b$).

## 🧮 Modelagem Matemática

O decaimento do Carbono-14 segue um modelo exponencial da forma:

$$N = \beta_0 \cdot e^{\beta_1 t}$$

Onde:
* $N$: Quantidade de Carbono-14.
* $t$: Tempo (idade da amostra).
* $\beta_0, \beta_1$: Coeficientes a serem determinados.

Para aplicar o **Método dos Mínimos Quadrados Linear**, a equação foi linearizada:

$$\ln(N) = \ln(\beta_0) + \beta_1 t$$

Isso transforma o problema em uma reta $Y = A + Bx$, permitindo a resolução via sistema linear.

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.
* Arquivo `carbono14.txt` no mesmo diretório do script (contendo os dados das amostras).

### Passo a Passo
1.  Clone este repositório:
    ```bash
    git clone https://github.com/Layonj3000/curve-fitting-carbon14.git
    ```
2.  Acesse a pasta do projeto:
    ```bash
    cd curve-fitting-carbon14
    ```
3.  Execute o script:
    ```bash
    python curve-fitting-carbon14.py
    ```

## 📊 Exemplo de Saída

Ao executar o programa, o console exibirá os parâmetros calculados e a estimativa final:

```text
Dados carregados: 48 amostras.
------------------------------
RESULTADOS DO AJUSTE
------------------------------
Beta_0 (Coeficiente Linear): 60220002024.8289
Beta_1 (Coeficiente Exponencial): -0.00012000
Equação Final: N = 6.0220e+10 * e^(-1.200000e-04 * t)
------------------------------
Para N = 53307321157:
Idade estimada (t) = 1007.6929 anos
------------------------------
```

## 👨‍💻 Autores 
<div>
  <table style="margin: 0 auto;">
    <tr>
      <td><a href="https://github.com/DavidPotentini"><img loading="lazy" src="https://avatars.githubusercontent.com/u/106561154?v=4" width="115"><br><sub>David Potentini</sub></a></td>
      <td><a href="https://github.com/Layonj300"><img loading="lazy" src="https://avatars.githubusercontent.com/u/106559843?v=4" width="115"><br><sub>Layon Reis</sub></a></td>
    </tr>
  </table>
</div>