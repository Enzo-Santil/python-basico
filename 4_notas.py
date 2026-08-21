notas = [10, 7, 9, 4, 5]

soma = 0


for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")

