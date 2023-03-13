import hashlib
import json
def hashed_password(password):
    encode_password = password.encode()
    new_password = hashlib.sha256(encode_password).hexdigest()
    data = {"mdp": new_password}
    with open ("password/doc.json", "a") as file:
        json.dump(data, file)
    return new_password

def create_password():
    while True:
        password = input('Créer votre mot de passe : ')
        nbr_maj = 0
        nbr_min = 0
        nbr_chiffre = 0
        nbr_character = 0
        special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]
        for i in password:
            if i.lower() != i:
                nbr_maj += 1
            if i.upper() != i:
                nbr_min += 1
            if i.isdigit():
                nbr_chiffre +=1
            for j in special_characters:
                if i == j:
                    nbr_character += 1
        if len(password) < 8 or nbr_maj < 1 or nbr_min < 1 or nbr_chiffre < 1 or nbr_character < 1:
            print('Votre mot de passe doit contenir au moins 8 caractères,une lettre en majuscule et minuscule, un chiffre et un caractère spécial(!, @, #, $, %, ^, &, *).')
        else:
            print('ok')
            hashed_password(password)
            break



create_password()