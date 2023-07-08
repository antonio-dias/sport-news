from dotenv import load_dotenv
from service import job_service

if __name__ == '__main__':
    load_dotenv()

    job_service.extract_game_info()
