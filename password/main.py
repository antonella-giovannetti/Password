import hashlib
import json
import os.path

def menu():
    while True:
        print(' ')
        print('MENU')
        print('1 - Créer un compte')
        print('2 - Afficher les utilisateurs')
        print('3 - Quitter')
        print(' ')
        number = input('Choissisez un chiffre > ')
        print(' ')
        if number.isdigit() == False:
            print(' ')
            print('Veuillez entrer un chiffre entre 1 et 3!')
            print(' ')
        elif number == "1":
            create_account()
        elif number == "2":
            if os.path.isfile("data.json"):
                with open('data.json', 'r') as file_json:
                    dict_json = json.load(file_json)
                    print('Voici les utilisateurs enregistrés : ')
                    for i in dict_json["infos"]:
                        print(i['user'] + ": " + i['password'])
                    print(' ')
            else:
                # This is a print function
                print('Il n\'y a pas encore de compte enregistré')
        elif number == "3":
            break
        else:
            print(' ')
            print('Veuillez entrer un chiffre valide !')
            print(' ')
            
# Fonction pour ajouter données dans un fichier json
def add_on_json(user, password):
    if os.path.isfile("data.json"):
        with open('data.json', 'r+') as file_json:
            dict_json = json.load(file_json)
            dict_json.setdefault("infos", []).append({"user": user, "password" : password})
            file_json.truncate(0)
            file_json.seek(0)
            json.dump((dict_json), file_json, indent=4)
            print(' ')
            print('Votre compte a bien été enregistré')
    else:
        with open('data.json', 'w') as file_json:
            json.dump({"infos": [{"user": user, "password" : password}]}, file_json, indent=4)
        print(' ')
        print('Votre compte a bien été enregistré')

# Fonction pour hasher le mdp
def hashed_password(password):
    # encodage du mdp 
    encode_password = password.encode()
    # hashing du mdp
    new_password = hashlib.sha256(encode_password).hexdigest()
    return new_password

# Fonction pour création de mdp et vérification
def create_account():
    while True:
        user = input('Veuillez entrer un nom d\'utilisateur : ')
        if os.path.isfile("data.json"):
            with open('data.json', 'r') as file_json:
                dict_json = json.load(file_json)
                # Vérifier si l'utilisateur existe déjà dans le dictionnaire
                if user in [info["user"] for info in dict_json["infos"]]:
                    print("L'utilisateur existe déjà.")
                else:
                    # L'utilisateur n'existe pas encore
                    break
        else:
            # Fichier JSON n'existe pas encore
            break

    while True:
        password = input('Veuillez entrer un mot de passe : ')
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
            hashed_pswd = hashed_password(password)
            if os.path.isfile("data.json"):
                with open('data.json', 'r') as file_json:
                    dict_json = json.load(file_json)
                    # Vérifier si l'utilisateur existe déjà dans le dictionnaire
                    if hashed_pswd in [info["password"] for info in dict_json["infos"]]:
                        print("Le mot de passe existe déjà.")
                    else:
                        add_on_json(user, hashed_pswd)
                        break
            else:
                # Fichier JSON n'existe pas encore
                add_on_json(user, hashed_pswd)
                break
            break
menu()