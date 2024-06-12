meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "XD":  "un repuesta graciosa utilizada en internet"
            }

palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in meme_dict.keys():
     print(meme_dict[palabra])   
else:
    print("perdon no pudimos identificar la palabra vuelve a escribirlo con mayusculas")
    # ¿Qué hacer si no se encuentra la palabra?
