import random
import string

def generator_parola(min_length, numere=True, caractere_speciale=True):
    litere = string.ascii_letters
    cifre = string.digits
    special = string.punctuation

    caractere = litere
    if numere:
        caractere += cifre
    if caractere_speciale:
        caractere += special
    
    parola = ""
    indeplineste_cerinta = False
    contine_numere = False
    contine_speciale = False

    while not indeplineste_cerinta or len(parola) < min_length:
        caracter_nou = random.choice(caractere)
        parola += caracter_nou

        if caracter_nou in cifre:
            contine_numere = True
        elif caracter_nou in special:
            contine_speciale = True

        indeplineste_cerinta = True
        if numere:
            indeplineste_cerinta = contine_numere
        if caractere_speciale:
            indeplineste_cerinta = indeplineste_cerinta and contine_speciale
        
    return parola


min_length = int(input("Enter the minimum length of your password: "))
contine_numere = input("Do you want any numbers in your password? y/n ").lower() == "y"
contine_speciale = input("Do you want any special caractere in your password? y/n ").lower() == "y"
parola = generator_parola(min_length, contine_numere, contine_speciale)
print('Your password is: ', parola)

