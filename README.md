# Python 3rd home assignment
Purpose of this app is to load interfaces configuration info from provided JSON, store them as objects in a list and then send them to the PostgresQL database. Both app and database are dockerised.
## How to run the app
Starting the app and the database is handled in docker-compose, so there is no need to run anything separately.
1. Make sure you don't have anything running on localhost port 5432
2. Open terminal in project's root directory
3. Run this command:
    ```
    docker-compose up
    ```
4. Wait a few second for Postgres initialisation and Python app to complete the task
5. If you see "Data sent to the database successfully, proceed to database check

## Check the database
**A Postgres management tool is recommended for this step for proper output from table**<br>
1. Login to the database at localhost:5432 with these credentials:
- database: database
- username: username
- password: password
2. Use query tool to get output from table:
    ```
    select * from interfaces_config;
    ```

## Adjust interface groups in JSON parser
The app is default set to skip BDI and Loopback interfaces in JSON. Find *get_interfaces* in *app/modules/jsonparser* to modify this setting.
- If you'd like to change parsed interface group, add/remove them to/from if condition. Example:
    ```
    if interface_group_name == "TenGigabitEthernet" or interface_group_name == "GigabitEthernet":
        pass
    ```
- If you'd like to parse all interfaces, remove whole condition, so the code will look like:
    ```
    for interface_group_name, interface_group_content in all_interfaces_list.items():
        for interface in interface_group_content:
            interface_name = interface_group_name + str(interface.get("name"))
        ...
    ```
