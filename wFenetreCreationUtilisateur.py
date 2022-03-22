from wFenetreListeProjets import FenetreListeProjet
import os  # Sert pour simplifier l'écriture du chemin d'accès d'un fichier (voir os.getcwd()).
from tkinter import *
from PIL.ImageTk import PhotoImage  # Ces deux liens servent pour amener les fonctions fixant les images de fond.


class FenetreCreationUtilisateur(Tk):  # Declaration de l'objet

    # Constructeur de l'objet
    def __init__(self):
        Tk.__init__(self)
        print("*** Fenetre ouverture ***")  # Pour controle en console.
        self.title("Ouverture")  # Le titre de la fenêtre.
        self.minsize(1200, 700)  # Initialisation de la taille de fenêtre.
        self.Largeur = 100  # Paramètre représentant la largeur de la zone du Canevas.
        self.Hauteur = 100  # Hauteur de la zone du canevas.
        self.LigneInitiale = 21
        self.ColonneInitiale =21

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

        self.frameInfoTop = Frame(self, bg="white", borderwidth=2, relief=GROOVE, height= 100, padx=3, pady=3)
        self.frameInfoTop.place(x=0,y=0)


        # ELEMENTS GRAPHIQUES : Label Frame
        self.labelFrameSaisie= LabelFrame(self, text="Saisir vos informations", padx=21, pady=21)
        self.labelFrameSaisie.pack(side=LEFT, fill=BOTH, expand="yes")

        self.frameColonneDroite = Frame(self,bg="white", borderwidth=2, relief=GROOVE, padx=3, pady=3)
        self.frameColonneDroite.pack(side=RIGHT, fill=Y, expand=TRUE)



        # ELEMENT GRAPHIQUE : Affichage du fond d'écran  dans son Canevas
        self.photo = PhotoImage(file=os.getcwd() + "\IMAGES\ImageOuverture.jpg")

        # ELEMENT GRAPHIQUE CANEVAS
        self.canvas = Canvas(self.frameColonneDroite,width=52,height=52)
        self.canvas.create_image(0, 0, image=self.photo)
        self.canvas.pack(side=TOP)


        # ELEMENTS GRAPHIQUES : Label login
        LabelNom = Label(self.labelFrameSaisie, text="Nom", font=('Calibri', 10), fg="Black")
        LabelNom.place(x=self.ColonneInitiale, y=self.LigneInitiale)

        # ELEMENTS GRAPHIQUES : Label login
        LabelPrenom = Label(self.labelFrameSaisie, text="Prenom", font=('Calibri', 10), fg="Black")
        LabelPrenom.place(x=self.ColonneInitiale, y=self.LigneInitiale +40)

        # ELEMENTS GRAPHIQUES : Label login
        LabelDateNaissance = Label(self.labelFrameSaisie, text="Date de naissance", font=('Calibri', 10), fg="Black")
        LabelDateNaissance.place(x=self.ColonneInitiale, y=self.LigneInitiale +80)

        # ELEMENTS GRAPHIQUES : Label login
        LabelAdresseMail = Label(self.labelFrameSaisie, text="Adresse e-mail", font=('Calibri', 10), fg="Black")
        LabelAdresseMail.place(x=self.ColonneInitiale, y=self.LigneInitiale +120)

        # ELEMENTS GRAPHIQUES : Label login
        LabelMotDePasse1 = Label(self.labelFrameSaisie, text="Saisir un mot de passe", font=('Calibri', 10), fg="Black")
        LabelMotDePasse1.place(x=self.ColonneInitiale, y=self.LigneInitiale +160)

        # ELEMENTS GRAPHIQUES : Label login
        LabelMotDePasse2 = Label(self.labelFrameSaisie, text="Re-Saisir le mot de passe", font=('Calibri', 10), fg="Black")
        LabelMotDePasse2.place(x=self.ColonneInitiale, y=self.LigneInitiale +200)

        # ELEMENT GRAPHIQUE : Bouton
        self.EnregistrerLaSaisie = Button(self.labelFrameSaisie, text=" Enregistrer la saisie ", relief=GROOVE, font=("Calibri", 10), command=self.commandeEnregistrerLaSaisie)
        self.EnregistrerLaSaisie.pack(side=LEFT, padx=5, pady=5)

        # ELEMENT GRAPHIQUE : Bouton
        self.quitButton = Button(self.labelFrameSaisie,  text="Quitter", relief=GROOVE, font=("Calibri", 10), command=self.destroy)
        self.quitButton.pack(side=RIGHT, padx=5, pady=5)

        # ELEMENTS GRAPHIQUES : Label login
        LabelTitre = Label(self.frameInfoTop, text="PAssavGen", font=('Calibri', 10), fg="Black")
        LabelTitre.place(x=self.ColonneInitiale, y=self.LigneInitiale)

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
    def commandeEnregistrerLaSaisie(self):

        self.destroy()
        # ferme Fenetre en cours, destroy supprime aussi toute les modifications qu'aura recue un objet :
        # ouvre Fenetre Login
        app = FenetreListeProjet(0)  # 0 représente un ID nul, sert pour que F01 puisse transmettre l'ID après
        app.focus_force()  # Force le focus sur la fenetre, pour ne pas avoir besoin de cliquer dessus et risquer
        # d'endommager le code.
        app.mainloop()  # Ouvre l'objet
        print("OK")

    def alert(self):
        print("**** ok vlaider")