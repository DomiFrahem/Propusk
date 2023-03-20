import os
import os
import appdirs
from dotenv import load_dotenv
from window.DialogCustomVariables import DialogCustomVariables


__VERSION = "ver 0.2"
DEFAULT_PATH = os.path.join(appdirs.user_data_dir(), "propusk")
DEFAULT_PATH_PHOTO = os.path.join(DEFAULT_PATH, "photo")

os.environ['VERSION'] = __VERSION
# os.environ['DEFAULT_PATH'] = DEFAULT_PATH
# os.environ['PHOTO_DIR'] = DEFAULT_PATH_PHOTO
os.environ['ABSOLUTE_PATH'] = os.path.dirname(os.path.abspath(__file__))
os.environ['NO_MEDIA_IMAGE'] = os.path.join(os.environ.get('ABSOLUTE_PATH'),
                                            'image', 'no_media_main.jpg')
os.environ['INDEX_PHOTO'] = '0'
os.environ['INDEX_CAMERA'] = '1'

def load_variables():
    # Load variable from .env
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    if not os.path.exists(dotenv_path):
        DialogCustomVariables(dotenv_path).exec_()
    
    load_dotenv(dotenv_path=dotenv_path)
