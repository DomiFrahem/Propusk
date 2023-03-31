import os
import os
import appdirs
from dotenv import load_dotenv
from window.DialogCustomVariables import DialogCustomVariables


__VERSION = "ver 0.3 beta"
DEFAULT_PATH = os.path.join(appdirs.user_data_dir(), "propusk")
DEFAULT_PATH_PHOTO = os.path.join(DEFAULT_PATH, "photo")

no_media = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image', 'no_media_main.jpg')
os.environ.update({
    'VERSION': __VERSION,
    'ABSOLUTE_PATH': os.path.dirname(os.path.abspath(__file__)),
    'NO_MEDIA_IMAGE': no_media,
    'INDEX_PHOTO': '0',
    'INDEX_CAMERA': '1'
})
# os.environ['DEFAULT_PATH'] = DEFAULT_PATH
# os.environ['PHOTO_DIR'] = DEFAULT_PATH_PHOTO

def load_variables():
    # Load variable from .env
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    if not os.path.exists(dotenv_path):
        DialogCustomVariables(dotenv_path).exec_()
    
    load_dotenv(dotenv_path=dotenv_path)
