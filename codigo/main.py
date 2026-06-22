def par_impar(n):
    if n.isdigit():
        n = int(n)
    else:
        print("Error: Debe ingresar un numero entero.")
        return
    if n == 0:
        print(f"El numero {n} es nulo.")
        return
    
    if n % 2 == 0:
        print(f"El numero {n} es par.")
    else:
        print(f"El numero {n} es impar.")
    
par_impar(input("Ingrese un numero entero: "))
    