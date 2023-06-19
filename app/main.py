class DeviceConfiguration:
    def __init__(self, id, name, description, max_frame_size, config, port_channel_id):
        self.id = id
        self.name = name
        self.description =  description
        self.max_frame_size = max_frame_size
        self.config = config
        self.port_channel_id = port_channel_id