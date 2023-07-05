from db.database import Database
import logging

def find_games_to_start():
    try:
        mongodb_connection = Database()
        data = mongodb_connection.find_all_games_to_start()
        mongodb_connection.close_connection()
        print("- ", data)
    except Exception as e:
        logging.error(exc_info=True, msg=str(e))
