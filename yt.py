import os
from yt_dlp import YoutubeDL

# === CONFIGURACIÓN ===
CARPETA_YT = '/srv/nuc/ssd/YT/'
# CARPETA_YT = '/home/calleja/Descargas/'

ULTIMOS_N_VIDEOS = 2
CANAL_CONFIG = {
    "BaityLive": {"url": "https://www.youtube.com/@BaityLive/videos"},
    "BaityBait": {"url": "https://www.youtube.com/@SrBaityBait"},
    "LordDraugr": {"url": "https://www.youtube.com/@LordDraugr/videos"},
    "FacuPeralta": {"url": "https://www.youtube.com/@Facu_Peralta/videos"},
    "JuanRamonRallo": {"url": "https://www.youtube.com/@juanrallo/videos"},
    "Kurzgesagt": {"url": "https://www.youtube.com/@kurzgesagt/videos"},
    "PolBertran": {"url": "https://www.youtube.com/@PolBertran/videos"},
    "L&V": {"url": "https://www.youtube.com/@LeyendasyVideojuegos/videos"},
    "AlfredoVozmediano": {"url": "https://www.youtube.com/@avozmechef/videos"},
    "Diegodoal": {"url": "https://www.youtube.com/@diegodoal/videos"},
    "Ecomonos": {"url": "https://www.youtube.com/@ecomonos/videos"},
    "Fonseca": {"url": "https://www.youtube.com/@SoloFonseca/videos"},
    "HRom": {"url": "https://www.youtube.com/@HRom/videos"},
    "LaHiperactina": {"url": "https://www.youtube.com/@Lahiperactina/videos"},
    "EsquizofreniaNatural": {"url": "https://www.youtube.com/@EsquizofreniaNatural/videos"},
    "CorduraArtificial": {"url": "https://www.youtube.com/@CorduraArtificial/videos"},
    "VisualEconomik": {"url": "https://www.youtube.com/@VisualEconomik/videos"},
    "ArteDeInvertir_videos": {"url": "https://www.youtube.com/@Artedeinvertir/videos"},
    "ArteDeInvertir_directos": {"url": "https://www.youtube.com/@Artedeinvertir/streams"},
    "ArjanCodes": {"url": "https://www.youtube.com/@ArjanCodes/videos"},
    "Betto": {"url": "https://www.youtube.com/@SrtoBetto/videos"},
    "BettaTech": {"url": "https://www.youtube.com/@BettaTech/videos"},
    "Mafius": {"url": "https://www.youtube.com/@MAFIUSS/videos"},
    "LearnThatStack": {"url": "https://www.youtube.com/@LearnThatStack/videos"},
    "SotoIvars": {"url": "https://www.youtube.com/@JuanSotoIvarsYtb/videos"},
    "BaityPlus": {"url": "https://www.youtube.com/@BaityPluss/videos"},
    "DrLaRosa": {"url": "https://www.youtube.com/@DRLAROSA/videos"},
}

# === FUNCIONES ===

def descargar_videos(canal_url, carpeta_salida):
    os.makedirs(carpeta_salida, exist_ok=True)

    opciones = {
        'outtmpl': os.path.join(carpeta_salida, '%(title)s.%(ext)s'),
        'format': 'best',
        'quiet': False,
        'ignoreerrors': True,
        'playlistend': ULTIMOS_N_VIDEOS,
        'remote_components': ['ejs:github']
    }

    with YoutubeDL(opciones) as ydl:
        print(f"\nDescargando videos de: {canal_url}")
        ydl.download([canal_url])


def main():
    for nombre, config in CANAL_CONFIG.items():
        print(f"\nProcesando canal: {nombre}")
        descargar_videos(config["url"], os.path.join(CARPETA_YT,nombre))


if __name__ == "__main__":
    main()


