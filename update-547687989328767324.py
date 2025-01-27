import importlib
import sys

# List of required packages
required_packages = [
    'keyboard', 'pyaudio', 'SpeechRecognition', 'opencv-python',
    'picamera', 'sensors', 'gpsd-py3', 'gpiozero', 'psutil'
]

# Function to check if a package is installed
def check_package(package):
    try:
        importlib.import_module(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is NOT installed.")

# Check each package in the list
for package in required_packages:
    check_package(package)

# Exit with status 0 (success)
sys.exit(0)
