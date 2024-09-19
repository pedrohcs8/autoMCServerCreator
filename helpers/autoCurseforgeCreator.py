from simple_term_menu import TerminalMenu
import os

def createSpigot():
    modpack_url = input("Modpack URL:\n")
    cf_key = input("Curseforge API Key:\n")
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

    print("Use simplevoicechat (24454)?")
    voip_options = ["Yes", "No"]
    voip_menu = TerminalMenu(voip_options)
    voip_raw = voip_menu.show()

    voip = False

    if voip_raw == 0:
        voip = True
    elif voip_raw == 1:
        voip = False

    if voip == True:
        os.system(
            f"TYPE=AUTO_CURSEFORGE -e CF_PAGE_URL={modpack_url} -e CF_API_KEY='{cf_key}' -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p 25565:25565 -p 24454/24454/udp -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")
    else:
        os.system(
            f"TYPE=AUTO_CURSEFORGE -e CF_PAGE_URL={modpack_url} -e CF_API_KEY='{cf_key}' -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p 25565:25565 -p 24454/24454/udp -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")