import time
# Config
BPM = 90                           # BPM típico de sertanejo
BEAT = 60.0 / BPM                  # 1 tempo em segundos
TYPE_DELAY = 0.03                  # atraso entre caracteres (um pouco mais lento)
# Letra sertaneja: (texto, duração_em_tempos)
lines = [
    ("Eu sei que você me quer", 4),
    ("Mas tem medo de se entregar", 4),
    ("Vem comigo, não tenha pressa", 4),
    ("Que eu vou te mostrar o amor", 4),
    ("No sertão, sob o luar", 4),
    ("A gente vai se encontrar", 4),
]
def type_line(text, char_delay=TYPE_DELAY):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(char_delay)
    print()
def karaoke():
    for text, duration in lines:
        type_line(text)
        time.sleep(duration * BEAT)
if __name__ == "__main__":
    karaoke()