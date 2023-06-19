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
    description = None
    max_frame_size = None
    port_channel_id = None

    interface_list = []
    path_to_json = Path("../configClear_v2.json")
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
            name = interface["name"]
            try:
                if "description" in interface:
                    description = interface["description"]
            except KeyError:
                return None
            try:
                if "mtu" in interface:
                    max_frame_size = interface["mtu"]
            except KeyError:
                return None
            config = interface
            try:
                if "Cisco-IOS-XE-ethernet:channel-group" in interface:
                    port_channel_id = interface["Cisco-IOS-XE-ethernet:channel-group"][
                        "number"
                    ]
            except KeyError:
                return None
            interface_configuration = DeviceConfiguration(
                name, description, max_frame_size, config, port_channel_id
            )
            interface_list.append(interface_configuration)

    return interface_list
