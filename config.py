from dotenv import load_dotenv
import os

load_dotenv()

def create_config():
    config = {
        "BOT_TOKEN": os.getenv("BOT_TOKEN")
    }
    return config

if __name__ == "__main__":
    print("Config file was loaded")