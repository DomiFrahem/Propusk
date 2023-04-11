import os
import os
import appdirs
from dotenv import load_dotenv
from window.DialogCustomVariables import DialogCustomVariables


DEFAULT_PATH = os.path.join(appdirs.user_data_dir(), "propusk")
DEFAULT_PATH_PHOTO = os.path.join(DEFAULT_PATH, "photo")

no_media = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image', 'no_media_main.jpg')

os.environ.update({
    'VERSION': "ver 0.5 beta",
    'ABSOLUTE_PATH': os.path.dirname(os.path.abspath(__file__)),
    'NO_MEDIA_IMAGE': no_media,
    'INDEX_PHOTO': '0',
    'INDEX_CAMERA': '1',
    'DEFAULT_PATH': '/home/asidorov/Документы/propusk_db'
})

def load_variables():
    # Load variable from .env
    dotenv_path = os.path.join(appdirs.user_config_dir(), 'propusk.env')

    if not os.path.exists(dotenv_path):
        DialogCustomVariables(dotenv_path).exec_()
    
    load_dotenv(dotenv_path=dotenv_path)
