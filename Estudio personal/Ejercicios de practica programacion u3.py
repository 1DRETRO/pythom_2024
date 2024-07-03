pm = (55, 17, 93, 75, 88, 55)
pq = (10, 85, 75, 88, 91, 75)
pp = (68, 78, 85, 68, 82, 10)

cm = {}
for i in pm:
    if i in cm:
        cm[i] += 1 
    else: 
        cm[i] = 1
dm = [i for i, c in cm.items() if c > 1]

print("El valor duplicado del puntaje de matematicas es: ", dm)

cq = {}
for i in pq:
    if i in cq:
        cq[i] += 1
    else:
        cq[i] = 1
dq = [i for i, c in cq.items() if c > 1]
print("El valor duplicado del puntaje de quimica es ", dq)

mp = {}
for i in pp:
    if i in mp:
        mp[i] += 1
    else: 
        mp[i] = 1
mp = [i for i, c in mp.items() if c > 1 ]
print("El valor duplicado del puntaje de programacion es: ", mp)

ldm = list(pm)
ldq = list(pq)
ldp = list(pp)
ldm.sort(reverse=True)
ldq.sort(reverse=True)
ldp.sort(reverse=True)

print(ldm, ldq, ldp)

lm = (pm)
lsm = (set(lm))
print("Se muestran las siguientes listas sin duplicados: ", lsm)

lq = (pq)
lsq = (set(lq))
print(lsq)

lp = (pp)
lsp = (set(lp))
print(lsp)

lista = ldm + ldq + ldp
lista_set = set(lista)
lista = list(lista_set)
print("nueva lista", lista)

pmi = min(lista)
pmm = max(lista)
print(f"El puntaje minimo es {pmi} y el maximo es {pmm}")