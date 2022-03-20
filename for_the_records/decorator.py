from distutils.text_file import TextFile
from wsgiref import validate


def literally_decorator(function):
    def text_frame(val):
        print('╔══════════════╗\n      '
        + val +'      \n╚══════════════╝')
        return function(val)
    return text_frame

@literally_decorator
def show_text(text):
    return text

show_text('jiyeon')
