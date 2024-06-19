n = int(input("Ingrese su numero de preferencia para aplicar la serie Fibbonaci"))
if n <= 0:
    print("El número ingresado debe ser mayor o igual a 1")
else:
    if n == 1:
        f = [0]
    elif n == 2:
        f = [0, 1]
    else:
        f = [0, 1] 
        for f in range(2, n):
            f.append([f-1], [f+2])
    print("La serie Fibbonaci = {n}:")
    print(f)