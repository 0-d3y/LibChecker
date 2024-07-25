import subprocess
import sys
import pyfiglet


class Colors:
    BLACK = '\033[30m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    RESET = '\033[0m'


tool_name = "LibChecker"
logo = pyfiglet.figlet_format(tool_name, font="slant")
print(Colors.WHITE + logo + Colors.RESET + "                 insta: cyber_77k\n")


libraries = [
    'requests', 'numpy', 'pandas', 'matplotlib', 'scipy', 'beautifulsoup4', 'lxml', 'pytest', 'flask', 'django',
    'sqlalchemy', 'pillow', 'scrapy', 'tensorflow', 'torch', 'keras', 'pyyaml', 'jupyter', 'notebook', 'seaborn',
    'statsmodels', 'pyautogui', 'pytesseract', 'pynput', 'pygame', 'plotly', 'dash', 'requests-html', 'tweepy',
    'chardet', 'paramiko', 'cryptography', 'cffi', 'pycrypto', 'asyncio', 'aiohttp', 'nltk', 'spacy', 'textblob',
    'opencv-python', 'pyqt5', 'wxPython', 'twilio', 'pymongo', 'redis', 'tornado', 'gunicorn', 'celery', 'pika',
    'schedule', 'pyodbc', 'pydantic', 'marshmallow', 'watchdog', 'gitpython', 'hypothesis', 'websockets', 'fastapi',
    'flask-restful', 'connexion', 'pytest-django', 'pytest-cov', 'pytest-mock', 'pytest-xdist', 'pytest-flask',
    'pytest-factoryboy', 'faker', 'moto', 'pytest-socket', 'sqlalchemy-utils', 'django-rest-framework', 'httpx',
    'fabric', 'yarl', 'aiofiles', 'pydub', 'pygments', 'paramiko', 'dataclasses', 'jsonschema', 'pyexcel',
    'beautifulsoup4', 'twisted', 'pyramid', 'boto3', 'sphinx', 'coverage', 'nose', 'scikit-learn', 'pytorch-lightning'
]

def run_command(command, check=True):
    try:
        subprocess.check_call(command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(Colors.RED + f"[ - ] Command failed: {e}" + Colors.RESET)
        if check:
            sys.exit(1)

def update_and_upgrade():
    print(Colors.WHITE + "[ + ] Updating and upgrading system packages..." + Colors.RESET)
    run_command('pkg update -y')
    run_command('pkg upgrade -y')

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(Colors.WHITE + f"[ + ] {package_name} installed successfully." + Colors.RESET)
    except subprocess.CalledProcessError as e:
        print(Colors.RED + f"[ - ] Failed to install {package_name}: {e}" + Colors.RESET)

def clean_pip_cache():
    print(Colors.WHITE + "[ ! ] Cleaning pip cache..." + Colors.RESET)
    run_command('pip cache purge', check=False)

def check_and_install_libraries():
    for lib in libraries:
        try:
            __import__(lib)
            print(Colors.WHITE + f"[ + ] {lib} : [already installed]" + Colors.RESET)
        except ImportError:
            print(Colors.RED + f"[ - ] {lib} [not installed] Installing..." + Colors.RESET)
            install_package(lib)

def ensure_pyfiglet_installed():
    try:
        import pyfiglet
    except ImportError:
        print(Colors.WHITE + "[ + ] pyfiglet not found. Installing..." + Colors.RESET)
        install_package('pyfiglet')

if __name__ == "__main__":
    update_and_upgrade()
    ensure_pyfiglet_installed()
    clean_pip_cache()
    check_and_install_libraries()
