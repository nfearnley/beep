from importlib.resources import path as rpath
import winsound

import beep.sounds

def main():
    with rpath(beep.sounds, "beep.wav") as p:
        winsound.PlaySound(str(p), winsound.SND_FILENAME)

if __name__ == "__main__":
    main()
