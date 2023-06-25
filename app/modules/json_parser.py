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
        self.config = json.dumps(config)
        self.port_channel_id = port_channel_id


def look_for_interfaces():
    path_to_json = Path("configClear_v2.json")
    with open(path_to_json, "r") as f:
        json_file = json.load(f)
        # Path to all interfaces in json file
        all_interface_list = json_file["frinx-uniconfig-topology:configuration"][
            "Cisco-IOS-XE-native:native"
        ]["interface"]

    return all_interface_list


all_interfaces_list = look_for_interfaces()


def get_interfaces():
    interface_list = []
    for interface_group_name, interface_group_content in all_interfaces_list.items():
        # Skip BDI and Loopback interfaces
        # Remove if condition to include BDI and Loopack interfaces in list
        if interface_group_name == "BDI" or interface_group_name == "Loopback":
            pass
        else:
            for interface in interface_group_content:
                # Assign dict values to variables
                interface_name = interface_group_name + str(interface.get("name"))
                interface_description = interface.get("description")
                interface_max_frame_size = interface.get("mtu")
                interface_config = interface
                interface_port_channel_id = interface.get(
                    "Cisco-IOS-XE-ethernet:channel-group", {}
                ).get("number")

                # Create object from interface values
                interface_configuration = DeviceConfiguration(
                    interface_name,
                    interface_description,
                    interface_max_frame_size,
                    interface_config,
                    interface_port_channel_id,
                )
                interface_list.append(interface_configuration)

    return interface_list
