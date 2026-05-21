#----imports::
import winsound

#________________________________________________STARTUP:
def startup_sound():
    # ------------------Windows Notify Calendar.wav
    sound = "Windows Notify Calendar.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def save_file_sound():
    # ------------------tada.mp3
    sound = "tada.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def open_notebook_sound():
    # ------------------tada.mp3
    sound = "openbook_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def light_candle_sound():
    # ------------------tada.mp3
    sound = "lighting_candle.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def erase_input_sound():
    # ------------------tada.mp3
    sound = "erasing_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def delete_button_clicked_sound():
    # ------------------tada.mp3
    sound = "delete_button_hover.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
                           )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def flip_page_sound():
    # ------------------tada.mp3
    sound = "flip_page_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")