def programa():
    pregunta_inicial = input("Escriba que operación matematica que usted quiera utilizar: ")

    if pregunta_inicial == "+":
        sum1 = int(input("Escribe el primer numero que quieras sumar: "))
        sum2 = int(input("Ahora escribe el otro numero que quieras sumar: "))
        print("La suma de los dos numeros es: ", sum1 + sum2)
        
        final1 = input("Quieres hacer otra operación? ")
        
        if final1 == "Si" or final1 == "si":
            programa()
        else:
            print("Gracias por utilizar mi programa. Adios.")


    if pregunta_inicial == "-":
        rest1 = int(input("Escribe el primer numero que quieras restar: "))
        rest2 = int(input("Ahora escribe el numero por el cual el anterior sera restado: "))
        print("La suma de los dos numeros es: ", rest1 - rest2)
        
        final2 = input("Quieres hacer otra operación? ")
        
        if final2 == "Si" or final2 == "si":
            programa()
        else:
            print("Gracias por utilizar mi programa. Adios.")


    if pregunta_inicial == "*":
        multi1 = int(input("Escribe el primer numero que quieras multiplicar: "))
        multi2 = int(input("Ahora escribe el otro numero que quieras multiplicar: "))
        print("La suma de los dos numeros es: ", multi1 * multi2)
        
        final3 = input("Quieres hacer otra operación? ")
        
        if final3 == "Si" or final3 == "si":
            programa()
        else:
            print("Gracias por utilizar este programa. Adios.")

    if pregunta_inicial == "/":
        div1 = int(input("Escribe el numero que quieras dividir: "))
        div2 = int(input("Ahora escribe el numero por el cual lo quieres dividir: "))
        print("La suma de los dos numeros es: ", div1 / div2)
        
        final4 = input("Quieres hacer otra operación? ")

        if final4 == "Si" or final4 == "si":
            programa()
        else:
            print("Gracias por utilizar este programa. Adios.")
