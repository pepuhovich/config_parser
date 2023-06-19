import json


def get_interfaces():
    interface_list = []
    with open("modules/demo_data.json", "r") as f:
        json_file = json.load(f)
        all_interface_list = json_file["frinx-uniconfig-topology:configuration"][
            "Cisco-IOS-XE-native:native"
        ]["interface"]

    for interface in (
        all_interface_list["Port-channel"],
        all_interface_list["TenGigabitEthernet"],
        all_interface_list["GigabitEthernet"],
    ):
        if_id = interface["type"]
        if_name = interface["name"]
        if_description[""]
        if_max_frame_size
        if_config
        if_port_channel_id
        policy_content = Single_Policy(policy_type, policy_name, True)
        policies_list.append(policy_content)

    return policies_list
