frase = input("Escribi una frase: ")
palabras = len(frase.split(" "))
cuantoTarda = palabras / 2
print(f"Palabras dichas: {palabras}, cuanto tardaria en decirlas: {cuantoTarda}")
if(cuantoTarda > 60):
    print("Tardas mas de un minuto en decir la frase!")

print(f"Dalto tardaria: {cuantoTarda*0.7}")