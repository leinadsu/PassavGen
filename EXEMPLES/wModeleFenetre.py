# ======================================================
# PROJET TRANSVERSE L2S2
# Auteurs : Equipe
# ======================================================
# Bibliothèques et importations :
import os  # Sert pour simplifier l'écriture du chemin d'accès d'un fichier (voir os.getcwd()).
from tkinter import *
from PIL.ImageTk import PhotoImage  # Ces deux liens servent pour amener les fonctions fixant les images de fond.
from wFenetreLogin import FenetreLogin


class NomDeLaFenetre(Tk):  # Declaration de l'objet

    # Constructeur de l'objet
    def __init__(self):
        Tk.__init__(self)
        print("*** Fenetre ouverture ***")  # Pour controle en console.
        self.title("Ouverture")  # Le titre de la fenêtre.
        self.minsize(1200, 700)  # Initialisation de la taille de fenêtre.
        self.Largeur = 1200  # Paramètre représentant la largeur de la zone du Canevas.
        self.Hauteur = 700  # Hauteur de la zone du canevas.

        # Paramètres plein écran, réutilisés dans les autres fenêtres.
        self.fullScreenState = True
        self.attributes("-fullscreen", self.fullScreenState)  # la fonction crée un plein écran si self.FullscreenState
        # = "True", et en mode affichage simple si "False".
        self.bind("<F11>", self.toggleFullScreen)  # Fonction permet d'obtenir un plein écran avec la touche F11
        self.bind("<Escape>", self.quitFullScreen)  # Fonction permet d'enlever le plein écran avec la touche Echap

        # Une méthode séparée pour construire le contenu de la fenêtre : crée une sorte "d'algorithme principal" dans
        # l'objet
        self.createWidgets()

    # **************************************
    # Fonction/Méthode de création des widgets.
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des éléments de la fenêtre.

        # ELEMENT GRAPHIQUE : Affichage du fond d'écran  dans son Canevas
        self.photo = PhotoImage(file=os.getcwd() + "\IMAGES\ImageOuverture.jpg")

        # ELEMENT GRAPHIQUE CANEVAS
        self.canvas = Canvas(self, width=self.Largeur, height=self.Hauteur)
        self.canvas.create_image(self.Largeur//2, self.Hauteur//2, image=self.photo)
        self.canvas.pack()

        # ELEMENT GRAPHIQUE : Label dans le CANEVAS
        self.canvas.create_text(600, 50, text="PassavGen", font='Calibri 52', fill='Black')

        # ELEMENT GRAPHIQUE : Label dans le CANEVAS
        self.canvas.create_text(1100, 650, text="Version 1.0 © Touts droits réservés. ", font='Calibri 9', fill='Blue')

        # ELEMENT GRAPHIQUE : Bouton
        self.ouvreFenetreLogin = Button(self, text="Commencer", relief=GROOVE, font=("Calibri", 10), command=self.commandeOuvreFenetreLogin)
        self.ouvreFenetreLogin.pack(side=LEFT, padx=5, pady=5)

        # ELEMENT GRAPHIQUE : Bouton
        self.quitButton = Button(self,  text="Quitter", relief=GROOVE, font=("Calibri", 10), command=self.destroy)
        self.quitButton.pack(side=RIGHT, padx=5, pady=5)


    # ************************** Autres Fonctions de l'objet:

    # FONCTIONS réglant respectivement l'application du plein écran avec F11, et la fin du plein écran avec Echap.
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState  # Le paramètre prend True si False avant (ce qui est le cas
        # par défaut: la fenêtre ne s'affiche pas en plein écran)
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # COMMANDE : ouvre la fenetre de saisie du login/mdp
    def commandeOuvreFenetreLogin(self):

        self.destroy()
        # ferme Fenetre en cours, destroy supprime aussi toute les modifications qu'aura recue un objet :
        # ouvre Fenetre Login
        app = FenetreLogin(0)  # 0 représente un ID nul, sert pour que F01 puisse transmettre l'ID après
        app.focus_force()  # Force le focus sur la fenetre, pour ne pas avoir besoin de cliquer dessus et risquer
        # d'endommager le code.
        app.mainloop()  # Ouvre l'objet
        print("OK")

    def alert(self):
        print("**** ok vlaider")