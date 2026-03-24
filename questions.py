import random
categories = {
    "tipos" : ["cadena","entero","lista"],
    "codigo" : ["python","programa"],
    "control" : ["variable","funcion","bucle"]
}
used_words = []
total_score = 0
while True:
    print("Categorias disponibles:")
    for category in categories:
        print (category)
    chosen_category = input ("Elija una categoria").lower().strip()
    available_words = [word for word in categories[chosen_category] if word not in used_words]
    if not available_words:
        print("No quedan palabras disponibles. Elija otra categoria")
        continue
    word = random.sample(available_words,1)[0]
    used_words.append(word)
    guessed = []
    attempts = 6
    score = 0
    print("¡Bienvenido al Ahorcado!")
    print()
    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            score += 6
            print(f"¡Ganaste!, tu puntaje es {score}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower().strip()
    
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no valida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        score = 0
        print(f"¡Perdiste! La palabra era: {word}, tu puntaje es {score}")
    total_score += score
    play_again = input ("¿Volver a jugar? ingrese si o no: ").lower ()
    if play_again != "si":
        break
print(f"juego terminado!. Puntaje total: {total_score}")

