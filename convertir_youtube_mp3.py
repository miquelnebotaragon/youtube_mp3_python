#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import youtube_dl

# Definició de la funció:
def youtube_a_mp3():
    # Variables de la funció:
    youtube_url = input("Introdueix la URL del vídeo a descarregar: ") # Sol·licita a l'usuari que introdueixi URL del vídeo.
    info_video = youtube_dl.YoutubeDL().extract_info(url = youtube_url,download=False) # Extracció informació del vídeo des de YouTube.
    nom_arxiu = f"{info_video['title']}.mp3" # Agafarà directament el nom del vídeo des de l'extracció anterior.
    youtube_dl_opcions = {
        'format': 'bestaudio/best',
        'keepvideo':False,
        'outtmpl':nom_arxiu,
    } # Personalitzam les opcions de descàrrega, per exemple, amb màxima qualitat.

    # Instruccions d'execució: 
    with youtube_dl.YoutubeDL(youtube_dl_opcions) as ydl:
        ydl.download([info_video['webpage_url']])

# Execució de la funció:
youtube_a_mp3()
