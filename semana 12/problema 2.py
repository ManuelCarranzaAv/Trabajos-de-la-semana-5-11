
palabra_secreta = "python"
counter = 0

while True:
    palabra = input("Ingresa la palabra secreta: ").lower()
    counter = counter + 1
    if palabra == palabra_secreta:
        print("Puerta abierta")
        break
    if palabra != palabra_secreta and counter > 3: 
        break