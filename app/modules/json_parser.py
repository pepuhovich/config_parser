import json
from pathlib import Path


class DeviceConfiguration:
    def __init__(self, id = None, name = None, description = None, max_frame_size = None, config = None, port_channel_id = None):
        self.id = id
        self.name = name
        self.description = description
        self.max_frame_size = max_frame_size
        self.config = config
        self.port_channel_id = port_channel_id


def get_interfaces():
    interface_list = []
    path_to_json = Path("./configClear_v2.json")
    with open(path_to_json, "r") as f:
        json_file = json.load(f)
        # Path to all interfaces in json file
        all_interface_list = json_file["frinx-uniconfig-topology:configuration"][
            "Cisco-IOS-XE-native:native"
        ]["interface"]

    for interface_group in (
        # Read specific interface types
        all_interface_list["Port-channel"],
        all_interface_list["TenGigabitEthernet"],
        all_interface_list["GigabitEthernet"],
    ):
        for interface in interface_group:
            record = {
                "name": None,
                "description": None,
                "max-frame-size": None,
                "config": None,
                "port-channel-id": None,
            }
            record["name"] = interface["name"]
            if 'description' in interface:
                record["description"] = interface["description"]
            if 'mtu' in interface:
                record["max-frame-size"] = interface["mtu"]
            record["config"] = interface
            if "Cisco-IOS-XE-ethernet:channel-group" in interface:
                record["port-channel-id"] = interface["Cisco-IOS-XE-ethernet:channel-group"]['number']
            interface_configuration = DeviceConfiguration(
                record["name"],
                record["description"],
                record["max-frame-size"],
                record["config"],
                record["port-channel-id"],
            )
            interface_list.append(interface_configuration)

    return interface_list
