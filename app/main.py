from modules.json_parser import get_interfaces
from modules.database_handler import send_to_db

if __name__ == "__main__":
    interface_list = get_interfaces()
    send_to_db(interface_list)
