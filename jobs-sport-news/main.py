from dotenv import load_dotenv
import schedule
from service import job_service

if __name__ == '__main__':
    load_dotenv()

    schedule.every(10).seconds.do(job_service.find_games_to_start)

    while True:
        schedule.run_pending()
