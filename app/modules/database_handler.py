import psycopg2
from modules.config_parser import config


def send_to_db(configuration_data):
    conn = None
    try:
        # Load database configuration
        database_access = config()
        conn = psycopg2.connect(**database_access)
        # Create connection cursor
        cur = conn.cursor()
        # Insert data to table
        for data in configuration_data:
            cur.execute(
                "INSERT INTO interfaces_config(name, description, config, port_channel_id, max_frame_size) VALUES (%s, %s, %s, %s, %s)",
                (
                    data.name,
                    data.description,
                    data.config,
                    data.port_channel_id,
                    data.max_frame_size,
                ),
            )
        cur.close()
    except (LookupError, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
