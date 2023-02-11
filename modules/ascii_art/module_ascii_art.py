import pyfiglet


def convert_text_to_ascii_art(text):
    result = pyfiglet.figlet_format(text, font='5lineoblique')
    return result
