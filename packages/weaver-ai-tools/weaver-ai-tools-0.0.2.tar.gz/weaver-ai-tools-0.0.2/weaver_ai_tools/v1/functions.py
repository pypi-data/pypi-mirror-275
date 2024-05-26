from .config import configuration

def register():
    requests.post("http://web:8000/service/alive/", configuration).raise_for_status()
