# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

for X in (True, False):
    for Y in (True, False):
        for Z in (True, False):
            print(not (X or Y or Z) == (not X and not Y and not Z))


