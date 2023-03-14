import hashlib
import json
import os.path

# Fonction pour ajouter données dans un fichier json
def add_on_json(user, password):
    if os.path.isfile("data.json"):
        with open('data.json', 'r+') as file_json:
            dict_json = json.load(file_json)
            dict_json.setdefault("infos", []).append({"user": user, "password" : password})
            file_json.truncate(0)
            file_json.seek(0)
            json.dump((dict_json), file_json, indent=4)
    else:
        with open('data.json', 'w') as file_json:
            json.dump({"infos": [{"user": user, "password" : password}]}, file_json, indent=4)

# Fonction pour hasher le mdp
def hashed_password(password):
    # encodage du mdp 
    encode_password = password.encode()
    # hashing du mdp
    new_password = hashlib.sha256(encode_password).hexdigest()
    return new_password

# Fonction pour création de mdp et vérification
def create_user_with_password():
    hashed_pswd = ""
    while True:
        user = input('Créer un nom d\'utilisateur : ')
        if os.path.isfile("data.json"):
            with open('data.json', 'r') as file_json:
                dict_json = json.load(file_json)
                # Vérifier si l'utilisateur existe déjà dans le dictionnaire
                for info in dict_json["infos"]:
                    if info["user"] == user:
                        print("L'utilisateur existe déjà.")
                        break
                else:
                    # L'utilisateur n'existe pas encore
                    break
        else:
            # Fichier JSON n'existe pas encore
            break

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
            hashed_pswd = hashed_password(password)
            break
    add_on_json(user, hashed_pswd)

create_user_with_password()