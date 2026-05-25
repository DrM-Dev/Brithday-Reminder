#----imports::
import winsound

#________________________________________________STARTUP:
def startup_sound():
    # ------------------
    sound = "birthday_reminder_startup.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def save_file_sound():
    # ------------------
    sound = "tada.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def open_notebook_sound():
    # ------------------
    sound = "openbook_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def light_candle_sound():
    # ------------------
    sound = "lighting_candle.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def erase_input_sound():
    # ------------------
    sound = "erasing_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def delete_button_clicked_sound():
    # ------------------
    sound = "delete_button_hover.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
                           )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#--------
def deleting_data_slot_sound():
    # ------------------
    sound = "crumble_paper_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
                           )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def flip_page_sound():
    # ------------------
    sound = "flip_page_sound.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
    )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
#________________________________________________
def closing_dates_book():
    # ------------------
    sound = "closing_dates_book.wav"
    try:
        winsound.PlaySound(fr"audio\{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC
                           )
    except FileNotFoundError:
        print(
            f"{sound} audio-file was NOT FOUND in [C:\Windows\Media\cding.wav] ")
