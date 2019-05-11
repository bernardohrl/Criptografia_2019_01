import os


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Digite o primeiro número: ")
    n1 = input()

    print("Digite o segundo número: ")
    n2 = input()

    print()
    print()
    print()
    r1, r2, r3 = extented_euclides_algorithm(int(n1), int(n2))
    print()
    print()
    print()


    n1, n2, r1, r2, r3 = str(n1), str(n2), str(r1), str(r2), str(r3)
    print("MDC(" + n1 + "," + n2 + ") = (" + r1 + ")(" + n1 + ") + (" + r2 + ")(" + n2 + ") = " +  r3)




def extented_euclides_algorithm(first, second):
    if second == 0:
        # Retorna MDC, o qual não será alterado.
        return 1, 0, first
   
    else:

        rest = first % second

        x , y, mdc = extented_euclides_algorithm(second, rest)

        # Retorna resultado inteiro da divisão
        quociente = first//second

        # Retonr y como first
        # Retonra resultado como second
        # Retorna MDC intocadoR
        return y, x-(quociente)*y, mdc




main()