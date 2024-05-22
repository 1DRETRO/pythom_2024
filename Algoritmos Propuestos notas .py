Joel_notas = (5.64, 3.45, 4.56)
Alondra_notas = (4.56, 5.64, 6.91)
Paz_notas = (3.45, 4.01, 6.23)

Joel_promedio = round(sum(Joel_notas))/3
Joel_nota_minima = min(Joel_notas)
Alondra_promedio = round(sum(Alondra_notas))/3
Alondra_nota_minima = min(Alondra_notas)
Paz_promedio = round(sum(Paz_notas))/3
Paz_nota_minima = min(Paz_notas)

Total_notas = (Joel_promedio, Alondra_promedio, Paz_promedio)  

print("El promedio de Joel es", round(Joel_promedio,3)) 
print("Su nota minima es", (Joel_nota_minima))
print("El promedio de Alondra es", round(Alondra_promedio,3))
print("Su nota minima es", (Alondra_nota_minima))
print("El promedio de Paz es", round(Paz_promedio))
print("Su nota minima es", (Paz_nota_minima))

Promedio_curso = round(sum(Total_notas))/3

print("El promedio general del curso es", Promedio_curso)

