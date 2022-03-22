# ======================================================
# PROJET TRANSVERSE L2S2
# Auteurs : Equipe
# ======================================================
# Bibliothèques et importations :
import os
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

from wFenetreCreationUtilisateur import FenetreCreationUtilisateur
from wFenetreListeProjets import FenetreListeProjet


class FenetreLogin(Tk):  # declaration de l'objet

    def __init__(self, ID_PersonneConnectee):
        Tk.__init__(self)
        print("*** FenetreLogin ***")  # Pour controle en console
        self.title("Fenetre Login")  # Le titre de la fenêtre
        self.maxsize  # Initialisation de la taille de fenêtre.

        # Les variables utiles
        self.Largeur = 1200  # Paramètre représentant la largeur de la zone du Canevas
        self.Hauteur = 700  # Hauteur de la zone du Canevas.
        self.leftPadding = 21
        self.paddingtop =100
        self.messageUtilisateurNom = StringVar()  # Variable de message d'erreur de saisie type stringvar()
        self.messageUtilisateurNom.set("...")  # maj Label pertinent.

        # Paramètres plein écran
        self.fullScreenState = True
        self.attributes("-fullscreen", self.fullScreenState)
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)
        self.createWidgets()  # Une méthode séparée pour construire le contenu de la fenêtre

    # Fonction/Méthode de création des widgets ****************************************.
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement


        # ELEMENT GRAPHIQUE : CANEVAS
        self.canvas = Canvas(self, width=self.Largeur, height=self.Hauteur)

        # ELEMENT GRAPHIQUE : Label dans le CANEVAS
        self.canvas.create_text(600, 50, text="PassavGen", font='Calibri 52', fill='Black')

        # ELEMENT GRAPHIQUE : Label dans le CANEVAS
        self.canvas.create_text(1100, 650, text="Version 1.0 © Touts droits réservés. ", font='Calibri 9', fill='Blue')

        # ELEMENT GRAPHIQUE : Image dans le canevas
        self.Photofond = Image.open(os.getcwd() + "\IMAGES\ImageOuverture.jpg")
        self.ImageCentrale = PhotoImage(self.Photofond)
        self.canvas.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.ImageCentrale)
        self.canvas.pack()

        # ELEMENTS GRAPHIQUES : Label login
        LabelLogin = Label(self, text="Identifiant", font=('Calibri', 10), fg="Black")
        LabelLogin.place(x=self.leftPadding, y=39)

        # ELEMENTS GRAPHIQUES : Label mot de passe
        LabelMdPasse = Label(self, text="Mot de passe", font=('Calibri', 10), fg="Black")
        LabelMdPasse.place(x=self.leftPadding, y=80)

        # ELEMENT GRAPHIQUE : champ de saisie
        EntreeLogin = Entry(self, bg='White', fg='Black', font=("Calibri", 10))
        EntreeLogin.focus_set()
        EntreeLogin.place(x=self.leftPadding + 90, y=39)

        # ELEMENT GRAPHIQUE : champ de saisie
        EntreeMdPasse = Entry(self, show="*", bg='White', fg='Black', font=("Calibri", 10))
        EntreeMdPasse.place(x=self.leftPadding + 90, y=80)

        # ELEMENT GRAPHIQUE : Label
        # Declaration et Placement du label avec le message du nom.
        self.LblMessage = Label(self, textvariable=self.messageUtilisateurNom, font=("Calibri", 10))
        self.LblMessage.pack(side="top")

        # ELEMENT GRAPHIQUE : <Button>
        self.BoutonQuitter = Button(self, text="Quitter", relief=GROOVE, font=("Calibri", 10), command=self.destroy)
        self.BoutonQuitter.place(x=self.leftPadding + 180, y=self.paddingtop + 21)

        # ELEMENT GRAPHIQUE : <Button>
        self.BoutonValideAuthentification = Button(self, text="Valider", relief=GROOVE, font=("Calibri", 10), command=self.CommandeVerifieAuthentification)
        self.BoutonValideAuthentification.place(x=self.leftPadding + 90, y=self.paddingtop + 21)

        # ELEMENT GRAPHIQUE : <Button>
        self.BoutonNouvelUtilisateur = Button(self, text="Nouvel utilisateur", relief=GROOVE, font=("Calibri", 10),
                                                   command=self.CommandeNouvelUtilisateur)
        self.BoutonNouvelUtilisateur.place(x=self.leftPadding + 90, y=self.paddingtop + 70)


    # FONCTIONS OUTILS réglant le plein écran
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    def CommandeVerifieAuthentification(self):  # Fonction doit être mise avant sinon erreur
        self.destroy()
        # ferme Fenetre ouverture, destroy supprime aussi toute les modifications qu'aura recue un objet :
        app = FenetreListeProjet(0)
        app.focus_force()  # Force le focus sur la fenetre, pour ne pas avoir besoin de cliquer dessus et risquer
        # d'endommager le code.
        app.mainloop()  # Ouvre l'objet
        # ========================

    def CommandeNouvelUtilisateur(self):  # Fonction doit être mise avant sinon erreur
        self.destroy()
        # ferme Fenetre ouverture, destroy supprime aussi toute les modifications qu'aura recue un objet :
        app = FenetreCreationUtilisateur()
        app.focus_force()  # Force le focus sur la fenetre, pour ne pas avoir besoin de cliquer dessus et risquer
        # d'endommager le code.
        app.mainloop()  # Ouvre l'objet
        # ========================
    def alert(self):
        print("****   valider")
