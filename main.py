import os
import uvicorn
import warnings
from mangum import Mangum
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

warnings.filterwarnings(action = "ignore")

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TranslatorProject.settings')

application = get_asgi_application()

handler = Mangum(application, lifespan="off")

if __name__ == "__main__":
    uvicorn.run("main:application", host = "0.0.0.0", port = 7000, lifespan = "off")