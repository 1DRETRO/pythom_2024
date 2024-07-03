t = input("Ingrese una cadena de texto: ").lower()
c_a = 0
c_e = 0
c_i = 0
c_o = 0
c_u = 0

for l in t:
    if l == "a":
        c_a += 1
    elif l == "e":
        c_e += 1
    elif l == "i":
        c_i += 1
    elif l == "o":
        c_o += 1 
    elif l == "u":
        c_u += 1 
print(f"La letra a se repite {c_a} veces, la e {c_e} veces, la i {c_i} veces, la o {c_o} veces y la u {c_u} veces")

    