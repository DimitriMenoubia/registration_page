from tkinter import *
import os

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("S'inscrire")
    register_screen.geometry("300x250")


    global username
    global password
    global username_entry
    global password_entry
    
# definir les variables de text
    username = StringVar()
    password = StringVar()

#definir l'etiquette pour les instructions de l'utilisateur
    Label(register_screen, text="SVP entrez les details suivants", bg="blue").pack()
    Label(register_screen, text="").pack()

#definir l'etiquette du nom d'utilisateur
    username_lable = Label(register_screen, text="Nom d'utilisateur * ")
    username_lable.pack()


#definition des entree du champ noms d'utilisateur
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

#definition des etiquette du champ motdepasse
    password_lable = Label(register_screen, text="Motdepasse * ")
    password_lable.pack()

#definition de l'etiquette de motdepasse
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()


    Label(register_screen, text="").pack()

#definition du button Connexion
    Button(register_screen, text="S'inscrire", width=10, height=1, bg="blue", command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Se Connecter")
    login_screen.geometry("300x250")
    Label(login_screen, text="SVP entrez vos informations en bas").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="nom d'utilisateur * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Motdepasse * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Se Connecter", width=10, height=1, command = login_verify).pack()


def register_user():

#recuperer les noms d'utilisateur et motdepasse
    username_info = username.get()
    password_info = password.get()

#ouvrir le fichier en lecture seul
    file = open(username_info, "w")

#on ecris les noms d'utilisateurs et motdepasse dans le fichier
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

#definir une etiquette qui nous affiche un message de success quand on PARVIENS a se logger

    Label(register_screen, text="inscription reussi!!", fg="green", font=("Calibri", 11)).pack()



def login_verify():

#recuperation nom d'utilisateur et mot de passe

    username1 = username_verify.get()
    password1 = password_verify.get()
    


#ceci supprime les info d'identification une fois que le processus d'identification se termine

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    list_of_files = os.listdir()

#definir les condiitons de verification
    if username1 in list_of_files:
        file1 = open(username1, "r")   # ouvrir le fichier en lecture seule
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()



def login_sucess():
    
    global login_success_screen   #cree la fenetre login success
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Connexion reussi").pack()


    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="motdepasse incorrect !").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

#popup quand le nom d'utilisateur entree n'est pas reconnu

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Utilisateur inexistant").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


#fonction pour detruire les popup
def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


#conception de la premiere fenetre
def main_account_screen():

    global main_screen
    main_screen = Tk()     #cree une fenetre graphique
    main_screen.geometry("300x250")  #defini la config de cette fenetre graphique
    main_screen.title("Connexion au compte")  #defini le titre de la fenetre graphique

#cree une etiquette de formulaire

    Label(text="Choisissez Se Connecter Ou S'incrire", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()


#cree le button Connexion

    Button(text="Se Connecter", height="2", width="30", command=login).pack()
    Label(text="").pack()


#cree le button S'inscrire
   
    Button(text="S'inscrire", height="2", width="30", command=register).pack()

    main_screen.mainloop()   # demarre l'interface graphique
  
main_account_screen()# appel la fonction main_account_screen()



