from simple_term_menu import TerminalMenu
import os

def createSnapshot():
    folder = input("Folder\n")

    print("Use ONLINE_MODE?")
    online_mode_options = ["Yes", "No"]
    online_mode_menu = TerminalMenu(online_mode_options)
    online_mode_raw = online_mode_menu.show()

    online_mode = "FALSE"

    if online_mode_raw == 0:
        online_mode = "TRUE"
    else:
        online_mode = "FALSE"

    print("Select Java Version:")
    java_version_options = ["java8-multiarch", "java11", "java17", "java21"]
    java_version_menu = TerminalMenu(java_version_options)
    java_version_raw = java_version_menu.show()

    java_version = "java8-multiarch"

    if java_version_raw == 0:
        java_version = "java8-multiarch"
    elif java_version_raw == 1:
        java_version = "java11"
    elif java_version_raw == 2:
        java_version = "java17"
    elif java_version_raw == 3:
        java_version = "java21"

    memory = input("Allocated Ram in GB:\n")
    container_name = input("Container Name:\n")
    port = input("Port\n")

    os.system(f"docker run -t -i -d -v ~/{folder}:/data -e VERSION=SNAPSHOT -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")