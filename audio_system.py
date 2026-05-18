#----imports::
import winsound

#________________________
def startup_sound():
    # ------------------
    try:
        winsound.PlaySound(r"audio\Windows Notify Calendar.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            "THE Windows Notify Calendar.wav.wav file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
