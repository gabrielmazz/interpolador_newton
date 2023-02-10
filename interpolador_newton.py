import sympy as sp
import numpy as np

"""
    Este trecho de código define a função "interp_newton" que recebe como entrada dois arrays, "x" e "y", que representam os pontos para interpolação. A função retorna uma outra função, "p(z)", 
    que é a interpolação dos pontos usando o Método de Newton. A função interp_newton começa armazenando o tamanho dos arrays "x" e "y" na variável "n". Em seguida, cria uma cópia dos valores de 
    "y" e armazena na variável "a". Depois, é realizado um loop de "j" que vai de 1 até n-1, e dentro deste loop, é realizado outro loop de "i" que vai de n-1 até j-1, decrementando de 1 em 1. 
    Durante o loop de "i", o valor da interpolação é calculado usando o Método de Newton. Por fim, a função "p(z)" é definida como o resultado da interpolação usando o Método de Newton, e é 
    retornada ao final da função "interp_newton".
"""

def interp_newton(x, y):
    # Guarda o tamanho dos arrays x e y na variável n
    n = len(x)
    
    # Cria uma cópia dos valores de y e guarda na variável a
    a = y.copy()
    
    # Loop de j que vai de 1 até n-1
    for j in range(1, n):
        
        # Loop de i que vai de n-1 até j-1, decrementando de 1 em 1
        for i in range(n-1, j-1, -1):
            
            # Calcula o valor da interpolação usando o método de Newton
            a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])

    # Define a função p(z) como o resultado da interpolação usando o método de Newton
    def p(z):
        val = a[n-1]
        for i in range(n-2, -1, -1):
            val = val * (z - x[i]) + a[i]
        return val

    # Retorna a função p(z)
    return p


# Pega os pontos x e y em uma array
x_str = input('Determine o array "x", adicionando os números separados por espaço: ').strip().split()
y_str = input('Determine o array "y", adicionando os números separados por espaço: ').strip().split()

# Estimativa que está sendo buscada
est = input('Determine qual a estimativa que deseja alcançar: ')

# Transforma os pontos de string para uma array de inteiros
x = np.array(x_str, dtype=int)
y = np.array(y_str, dtype=int)



# Recebe a interpolação vinda da função
P = interp_newton(x, y)

# Cria o polinomio
x_sym = sp.symbols('x')
polinomio = sp.poly(P(x_sym), x_sym)

# Imprime o polinômio interpolador
print(f"\nO polinômio interpolador de Newton é:")
print(sp.simplify(str(polinomio.as_expr())))

# Verifica a estimativa que foi pedida
x = sp.Symbol('x')

print(f"\nO resultado da estimativa para o valor de f({est}) é:")
print(sp.simplify(polinomio.subs(x, est)))