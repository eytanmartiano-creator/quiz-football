# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 15:45:37 2025

@author: Eytan Martiano
"""
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import game

images_logos = []

import requests

url = "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/250px-Real_Madrid_CF.svg.png"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
with open("real_madrid.png", "wb") as f:
    f.write(response.content)

def charger_logo(url, size=(50, 50)):
    """Télécharge et redimensionne un logo depuis une URL"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erreur chargement logo {url} : {e}")
        return None



def afficher_joueur():
    """Affiche clubs + logos"""
    global images_logos
    joueur, clubs = game.choisir_joueur()
    clubs_data = game.get_clubs_data()

    for widget in frame_clubs.winfo_children():
        widget.destroy()
    images_logos.clear()

    for club in clubs:
        frame = tk.Frame(frame_clubs)
        frame.pack(anchor="w")
        logo_url = clubs_data.get(club)
        if logo_url:
            img = charger_logo(logo_url)
            if img:
                images_logos.append(img)
                tk.Label(frame, image=img).pack(side="left", padx=5)
        tk.Label(frame, text=club, font=("Arial", 12)).pack(side="left")

    entry_reponse.delete(0, tk.END)
    label_resultat.config(text="")

def verifier():
    """Vérifie la réponse entrée"""
    reponse = entry_reponse.get()
    if game.verifier_reponse(reponse):
        label_resultat.config(text="✅ Bravo !", fg="green")
    else:
        label_resultat.config(
            text=f"❌ Mauvaise réponse.\nC’était {game.get_joueur_actuel()}.", fg="red"
        )

# Tkinter UI
root = tk.Tk()
root.title("Quiz Football - Devine le joueur")

frame_clubs = tk.Frame(root)
frame_clubs.pack(pady=10)

entry_reponse = tk.Entry(root, font=("Arial", 12))
entry_reponse.pack(pady=5)

btn_verifier = tk.Button(root, text="Vérifier", command=verifier, font=("Arial", 12))
btn_verifier.pack(pady=5)

label_resultat = tk.Label(root, text="", font=("Arial", 12))
label_resultat.pack(pady=10)

btn_nouveau = tk.Button(root, text="Nouveau joueur", command=afficher_joueur, font=("Arial", 12))
btn_nouveau.pack(pady=5)

afficher_joueur()
root.mainloop()
