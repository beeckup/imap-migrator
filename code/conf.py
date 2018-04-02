import os

SOURCE = {
    'HOST': str(os.environ['FROMHOST']),
    'USERNAME': str(os.environ['FROMMAIL']),
    'PASSWORD': str(os.environ['FROMPASSWORD']),
    'SSL': bool(os.environ['FROMSSL']),
    'IGNORE_FOLDERS': str(os.environ['FROMIGNORE_FOLDERS'])
}

TARGET = {
    'HOST': str(os.environ['TOHOST']),
    'USERNAME': str(os.environ['TOMAIL']),
    'PASSWORD': str(os.environ['TOPASSWORD']),
    'SSL': bool(os.environ['TOSSL']),
    'ROOT_FOLDER': str(os.environ['TOROOT_FOLDER'])
}