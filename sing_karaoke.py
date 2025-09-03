 # file: sing_karaoke.py
import time
import sys

# Config
BPM = 96                           # mude o BPM
BEAT = 60.0 / BPM                  # 1 tempo em segundos
TYPE_DELAY = 0.02                  # atraso entre caracteres

# Letra: (texto, duração_em_tempos)
lines = [
    ("I wanna da—", 2),
    ("I wanna dance in the lights", 4),
    ("I wanna ro—", 2),
    ("I wanna rock your body", 4),
    ("Come on, come on", 4),
    ("Rock that body", 4),
]

def type_line(text, char_delay=TYPE_DELAY):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(char_delay)
    print()

def sing():
    for text, beats in lines:
        type_line(text)
        time.sleep(beats * BEAT)

if __name__ == "__main__":
    sing()