# ======================================================
# PROJET TRANSVERSE L2S2
# Auteurs : Equipe
# ======================================================
# Bibliothèques et importations :
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class FenetreListeProjet(Tk):  # Declaration de l'objet
    # *****************************************
    # Constructeur de l'objet  : ne pas supprimer, sert pour mettre les paramètres et fonctions propres à l'objet.
    def __init__(self, ID_PersonneConnectee):  # Importation d'un message de test, ici "début" affiché en console
        # (pour vérifier l'importation de paramètres).
        Tk.__init__(self)
        print("*** Fenetre Liste Projet ***")  # Pour controle en console.
        self.title("Liste Projet")  # Le titre de la fenêtre.
        self.maxsize # Initialisation de la taille de fenêtre.
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

    # ******************************************************
    # Fonction/Méthode de création des widgets.
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des éléments de la fenêtre.

        # ELEMENT GRAPHIQUE : BARRE DE MENU ................
        menubar = Menu(self)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Créer", command=self.alert)
        menu1.add_command(label="Editer", command=self.alert)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Couper", command=self.alert)
        menu2.add_command(label="Copier", command=self.alert)
        menu2.add_command(label="Coller", command=self.alert)
        menubar.add_cascade(label="Editer", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=self.alert)
        menubar.add_cascade(label="Aide", menu=menu3)

        self.config(menu=menubar)
        # frame 1
        Frame1 = Frame(self, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=TOP,expand=Y, fill=BOTH, padx=5, pady=5)


        # ELEMENT GRAPHIQUE : BARRE D'ONGLETS ................
        tabControl = ttk.Notebook(Frame1)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='LISTE DES PROJETS')
        tabControl.add(tab2, text='INFORMATIONS')
        tabControl.pack(expand=1, fill="both")

        ttk.Label(tab1, text="Welcome to GeeksForGeeks").grid(column=0, row=0, padx=30,pady=30)
        ttk.Label(tab2, text="Lets dive into the world of computers").grid(column=0,row=0,padx=30,pady=30)


        # ELEMENT GRAPHIQUE : BOUTONS
        #>> Quitter l'application
        self.quitButton = Button(self,  text="Quitter", relief=GROOVE, font=("Calibri", 10), command=self.destroy)
        self.quitButton.pack(side=RIGHT, padx=5, pady=5)



    # **************************************
    # Autres Fonctions de l'objet:
    # FONCTIONS réglant respectivement l'application du plein écran avec F11, et la fin du plein écran avec Echap.
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState  # Le paramètre prend True si False avant (ce qui est le cas
        # par défaut: la fenêtre ne s'affiche pas en plein écran)
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    def alert(self):
        showinfo("alerte", "Bravo!")