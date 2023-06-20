import json
from pathlib import Path


class DeviceConfiguration:
    def __init__(
        self,
        name,
        description,
        max_frame_size,
        config,
        port_channel_id,
    ):
        self.name = name
        self.description = description
        self.max_frame_size = max_frame_size
        self.config = config
        self.port_channel_id = port_channel_id


def get_interfaces():
    path_to_json = Path("../configClear_v2.json")
    interface_list = []
    with open(path_to_json, "r") as f:
        json_file = json.load(f)
        # Path to all interfaces in json file
        all_interface_list = json_file["frinx-uniconfig-topology:configuration"][
            "Cisco-IOS-XE-native:native"
        ]["interface"]
    for k, v in all_interface_list.items():
        group_name = k
        if k == "BDI" or k == "Loopback":
            pass
        else:
            for interface in v:
                if_name = group_name + str(interface["name"])
                # Description
                if 'description' in interface:
                    if_description = interface["description"]
                else:
                    if_description = None
                
                 # Max frame size
                if 'mtu' in interface:
                    if_max_frame_size = interface["mtu"]
                else:
                    if_description = None
                # Config
                if_config = interface
                # Port channel ID
                if "Cisco-IOS-XE-ethernet:channel-group" in interface:
                    if_port_channel_id = interface["Cisco-IOS-XE-ethernet:channel-group"]["number"]
                else:
                    if_port_channel_id = None

                # Create object
                interface_configuration = DeviceConfiguration(
                    if_name,
                    if_description,
                    if_max_frame_size,
                    if_config,
                    if_port_channel_id,
                )
                interface_list.append(interface_configuration)

    return interface_list


get_interfaces()
