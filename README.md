# Interpolação de Newton

Este código usa o método de Interpolação de Newton para gerar um polinômio que aproxime uma função dada pelos pontos `x` e `y`.

## Bibliotecas

O código importa duas bibliotecas principais: `sympy` e `numpy`. A biblioteca `sympy` é usada para trabalhar com expressões matemáticas simbólicas e `numpy` é usada para trabalhar com arrays numéricos.

## Função `interp_newton`

A função `interp_newton` é responsável por calcular a interpolação de Newton. Ela recebe dois argumentos, os arrays `x` e `y`, que representam os pontos de uma função.

1. Guarda o tamanho dos arrays `x` e `y` na variável `n`.
2. Cria uma cópia dos valores de `y` e guarda na variável `a`.
3. Loop de `j` que vai de 1 até `n-1`.
   1. Loop de `i` que vai de `n-1` até `j-1`, decrementando de 1 em 1.
      1. Calcula o valor da interpolação usando o método de Newton: `a[i] = (a[i] - a[i-1]) / (x[i] - x[i-j])`.
4. Define a função `p(z)` como o resultado da interpolação usando o método de Newton.
5. Retorna a função `p(z)`.

## Entrada de dados

O usuário é solicitado a informar os arrays `x` e `y` que representam os pontos de uma função. Eles são lidos como strings e convertidos para arrays de inteiros. Sua leitura deve ser feita todos em uma linha com espaçamentos

- Exemplo: `x: 1 2 3 4` e `y: 5 6 7 8`

## Cálculo do polinômio interpolador

Com os arrays `x` e `y` em mãos, a função `interp_newton` é chamada para obter a interpolação de Newton. A partir da interpolação, é gerado o polinômio interpolador usando a biblioteca `sympy`.

## Estimativa

O usuário também pode verificar uma estimativa para a função, inserindo a expressão. O valor da `estimativa` é informado pelo usuário. O resultado da estimativa é obtido substituindo o valor da expressão no polinômio interpolador.

## Saída

O polinômio interpolador é impresso na tela e, caso a estimativa seja solicitada, o resultado da estimativa também é exibido.
