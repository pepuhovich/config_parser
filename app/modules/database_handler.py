import os
import psycopg2
from dotenv import load_dotenv

# Load Postgres configuration from .env
load_dotenv(dotenv_path='database.env')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')
db_name = os.getenv('POSTGRES_DB')
db_username = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')


def send_to_db(interface_list):
    conn = None
    try:
        # Create connection from env values
        conn = psycopg2.connect(host = db_host,
                                port = db_port,
                                database = db_name, 
                                user = db_username,
                                password = db_password)
        # Create connection cursor
        cur = conn.cursor()
        # Insert data to table
        for interface in interface_list:
            cur.execute(
                "INSERT INTO interfaces_config(name, description, config, port_channel_id, max_frame_size) VALUES (%s, %s, %s, %s, %s)",
                (
                    interface.name,
                    interface.description,
                    interface.config,
                    interface.port_channel_id,
                    interface.max_frame_size,
                ),
            )
        print("Data sent to the database successfully")
        cur.close()

    except psycopg2.DatabaseError as error:
        print(f"Error while sending data to the database: {error}")
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
