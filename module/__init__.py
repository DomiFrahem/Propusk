from datetime import datetime
import os
import platform
import subprocess



def create_filename(prefix: str = "propusk") -> str:
    return os.path.join(os.environ.get('PHOTO_DIR'), F"{prefix}_{datetime.now().timestamp()}.jpg")

def get_path_wkhtmltopdf() -> str:
    match platform.system():
        case 'Linux':
            result = subprocess.Popen(['whereis wkhtmltopdf'], shell=True, stdout=subprocess.PIPE).stdout.read()
            return str(result).split(' ')[1]
        case 'Windows':
            pass
        case _: ...
    
    
def main():
    print(get_path_wkhtmltopdf())


if __name__ == "__main__":
    main()