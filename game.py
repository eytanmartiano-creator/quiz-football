# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 15:45:08 2025

@author: Eytan Martiano
"""
import json
import random

joueur_actuel = None

def charger_joueurs():
    with open("joueurs.json", "r", encoding="utf-8") as f:
        return json.load(f)

def charger_clubs():
    with open("club.json", "r", encoding="utf-8") as f:
        return json.load(f)

def choisir_joueur():
    global joueur_actuel
    joueurs = charger_joueurs()
    joueur_actuel = random.choice(joueurs)
    return joueur_actuel["nom"], joueur_actuel["clubs"]

def verifier_reponse(reponse):
    global joueur_actuel
    if not joueur_actuel:
        return False
    return reponse.strip().lower() in [a.lower() for a in joueur_actuel["alias"]]

def get_joueur_actuel():
    global joueur_actuel
    return joueur_actuel["nom"] if joueur_actuel else ""

def get_clubs_data():
    return charger_clubs()
