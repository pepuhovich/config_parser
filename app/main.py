from modules.json_parser import get_interfaces

if __name__ == "__main__":
    list = get_interfaces()
    for i in list:
        print( i.name, i.description, i.max_frame_size, i.config, i.port_channel_id)