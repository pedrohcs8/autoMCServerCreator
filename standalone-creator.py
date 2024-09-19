#!/usr/bin/env python
import contextlib as __stickytape_contextlib

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path

        def make_package(path):
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    with open(os.path.join(partial_path, "__init__.py"), "wb") as f:
                        f.write(b"\n")

        make_package(os.path.dirname(path))

        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "wb") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

    __stickytape_write_module('helpers/vanillaCreator.py', b'from simple_term_menu import TerminalMenu\nimport os\n\ndef createVanilla():\n    version = input("Version\\n")\n    folder = input("Folder\\n")\n\n    print("Use ONLINE_MODE?")\n    online_mode_options = ["Yes", "No"]\n    online_mode_menu = TerminalMenu(online_mode_options)\n    online_mode_raw = online_mode_menu.show()\n\n    online_mode = "FALSE"\n\n    if online_mode_raw == 0:\n        online_mode = "TRUE"\n    else:\n        online_mode = "FALSE"\n\n    print("Select Java Version:")\n    java_version_options = ["java8-multiarch", "java11", "java17", "java21"]\n    java_version_menu = TerminalMenu(java_version_options)\n    java_version_raw = java_version_menu.show()\n\n    java_version = "java8-multiarch"\n\n    if java_version_raw == 0:\n        java_version = "java8-multiarch"\n    elif java_version_raw == 1:\n        java_version = "java11"\n    elif java_version_raw == 2:\n        java_version = "java17"\n    elif java_version_raw == 3:\n        java_version = "java21"\n\n    memory = input("Allocated Ram in GB:\\n")\n    container_name = input("Container Name:\\n")\n    port = input("Port\\n")\n\n    os.system(f"docker run -t -i -d -v ~/{folder}:/data -e VERSION={version} -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")')
    __stickytape_write_module('helpers/snapshotCreator.py', b'from simple_term_menu import TerminalMenu\nimport os\n\ndef createSnapshot():\n    folder = input("Folder\\n")\n\n    print("Use ONLINE_MODE?")\n    online_mode_options = ["Yes", "No"]\n    online_mode_menu = TerminalMenu(online_mode_options)\n    online_mode_raw = online_mode_menu.show()\n\n    online_mode = "FALSE"\n\n    if online_mode_raw == 0:\n        online_mode = "TRUE"\n    else:\n        online_mode = "FALSE"\n\n    print("Select Java Version:")\n    java_version_options = ["java8-multiarch", "java11", "java17", "java21"]\n    java_version_menu = TerminalMenu(java_version_options)\n    java_version_raw = java_version_menu.show()\n\n    java_version = "java8-multiarch"\n\n    if java_version_raw == 0:\n        java_version = "java8-multiarch"\n    elif java_version_raw == 1:\n        java_version = "java11"\n    elif java_version_raw == 2:\n        java_version = "java17"\n    elif java_version_raw == 3:\n        java_version = "java21"\n\n    memory = input("Allocated Ram in GB:\\n")\n    container_name = input("Container Name:\\n")\n    port = input("Port\\n")\n\n    os.system(f"docker run -t -i -d -v ~/{folder}:/data -e VERSION=SNAPSHOT -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")')
    __stickytape_write_module('helpers/forgeCreator.py', b'from simple_term_menu import TerminalMenu\nimport os\n\n# TODO: ADD FORGE VERSION SUPPORT\n\ndef createForge():\n    version = input("Version\\n")\n    folder = input("Folder\\n")\n\n    print("Use ONLINE_MODE?")\n    online_mode_options = ["Yes", "No"]\n    online_mode_menu = TerminalMenu(online_mode_options)\n    online_mode_raw = online_mode_menu.show()\n\n    online_mode = "FALSE"\n\n    if online_mode_raw == 0:\n        online_mode = "TRUE"\n    else:\n        online_mode = "FALSE"\n\n    print("Select Java Version:")\n    java_version_options = ["java8-multiarch", "java11", "java17", "java21"]\n    java_version_menu = TerminalMenu(java_version_options)\n    java_version_raw = java_version_menu.show()\n\n    java_version = "java8-multiarch"\n\n    if java_version_raw == 0:\n        java_version = "java8-multiarch"\n    elif java_version_raw == 1:\n        java_version = "java11"\n    elif java_version_raw == 2:\n        java_version = "java17"\n    elif java_version_raw == 3:\n        java_version = "java21"\n\n    memory = input("Allocated Ram in GB:\\n")\n    container_name = input("Container Name:\\n")\n    port = input("Port\\n")\n\n    print("Use simplevoicechat (24454)?")\n    voip_options = ["Yes", "No"]\n    voip_menu = TerminalMenu(voip_options)\n    voip_raw = voip_menu.show()\n\n    voip = False\n\n    if voip_raw == 0:\n        voip = True\n    elif voip_raw == 1:\n        voip = False\n\n    if voip == True:\n        os.system(\n            f"docker run -t -i -d -v ~/{folder}:/data -e TYPE=FORGE -e VERSION={version} -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -p 24454:24454/udp -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")\n    else:\n        os.system(\n            f"docker run -t -i -d -v ~/{folder}:/data -e TYPE=FORGE -e VERSION={version} -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")')
    __stickytape_write_module('helpers/spigotCreator.py', b'from simple_term_menu import TerminalMenu\nimport os\n\n# TODO: ADD GEYSER SUPPORT\n\ndef createSpigot():\n    version = input("Version\\n")\n    folder = input("Folder\\n")\n\n    print("Use ONLINE_MODE?")\n    online_mode_options = ["Yes", "No"]\n    online_mode_menu = TerminalMenu(online_mode_options)\n    online_mode_raw = online_mode_menu.show()\n\n    online_mode = "FALSE"\n\n    if online_mode_raw == 0:\n        online_mode = "TRUE"\n    else:\n        online_mode = "FALSE"\n\n    print("Select Java Version:")\n    java_version_options = ["java8-multiarch", "java11", "java17", "java21"]\n    java_version_menu = TerminalMenu(java_version_options)\n    java_version_raw = java_version_menu.show()\n\n    java_version = "java8-multiarch"\n\n    if java_version_raw == 0:\n        java_version = "java8-multiarch"\n    elif java_version_raw == 1:\n        java_version = "java11"\n    elif java_version_raw == 2:\n        java_version = "java17"\n    elif java_version_raw == 3:\n        java_version = "java21"\n\n    memory = input("Allocated Ram in GB:\\n")\n    container_name = input("Container Name:\\n")\n    port = input("Port\\n")\n\n    print("Use simplevoicechat (24454)?")\n    voip_options = ["Yes", "No"]\n    voip_menu = TerminalMenu(voip_options)\n    voip_raw = voip_menu.show()\n\n    voip = False\n\n    if voip_raw == 0:\n        voip = True\n    elif voip_raw == 1:\n        voip = False\n\n    if voip == True:\n        os.system(\n            f"docker run -t -i -d -v ~/{folder}:/data -e TYPE=SPIGOT -e VERSION={version} -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -p 24454:24454/udp -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")\n    else:\n        os.system(\n            f"docker run -t -i -d -v ~/{folder}:/data -e TYPE=SPIGOT -e VERSION={version} -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p {port}:{port} -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")')
    __stickytape_write_module('helpers/autoCurseforgeCreator.py', b'from simple_term_menu import TerminalMenu\nimport os\n\ndef createCurseforge():\n    modpack_url = input("Modpack URL:\\n")\n    cf_key = input("Curseforge API Key:\\n")\n    folder = input("Folder\\n")\n\n    print("Use ONLINE_MODE?")\n    online_mode_options = ["Yes", "No"]\n    online_mode_menu = TerminalMenu(online_mode_options)\n    online_mode_raw = online_mode_menu.show()\n\n    online_mode = "FALSE"\n\n    if online_mode_raw == 0:\n        online_mode = "TRUE"\n    else:\n        online_mode = "FALSE"\n\n    print("Select Java Version:")\n    java_version_options = ["java8-multiarch", "java11", "java17", "java21"]\n    java_version_menu = TerminalMenu(java_version_options)\n    java_version_raw = java_version_menu.show()\n\n    java_version = "java8-multiarch"\n\n    if java_version_raw == 0:\n        java_version = "java8-multiarch"\n    elif java_version_raw == 1:\n        java_version = "java11"\n    elif java_version_raw == 2:\n        java_version = "java17"\n    elif java_version_raw == 3:\n        java_version = "java21"\n\n    memory = input("Allocated Ram in GB:\\n")\n    container_name = input("Container Name:\\n")\n    port = input("Port\\n")\n\n    print("Use simplevoicechat (24454)?")\n    voip_options = ["Yes", "No"]\n    voip_menu = TerminalMenu(voip_options)\n    voip_raw = voip_menu.show()\n\n    voip = False\n\n    if voip_raw == 0:\n        voip = True\n    elif voip_raw == 1:\n        voip = False\n\n    if voip == True:\n        os.system(\n            f"docker run -d -it -v ~/{folder}:/data -e TYPE=AUTO_CURSEFORGE -e CF_PAGE_URL={modpack_url} -e CF_API_KEY=\'{cf_key}\' -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p 25565:25565 -p 24454:24454/udp -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")\n    else:\n        os.system(\n            f"docker run -d -it -v ~/{folder}:/data -e TYPE=AUTO_CURSEFORGE -e CF_PAGE_URL={modpack_url} -e CF_API_KEY=\'{cf_key}\' -e ONLINE_MODE={online_mode} -e MEMORY={memory}G -p 25565:25565 -e EULA=TRUE --name {container_name} itzg/minecraft-server:{java_version}")')
    from simple_term_menu import TerminalMenu
    
    from helpers.vanillaCreator import createVanilla
    from helpers.snapshotCreator import createSnapshot
    from helpers.forgeCreator import createForge
    from helpers.spigotCreator import createSpigot
    from helpers.autoCurseforgeCreator import createCurseforge
    
    print("Created by pedrohcs8")
    print("AutoMcSrvCreator V1.1")
    
    options = ["Vanilla", "Snapshot", "Forge", "Spigot", "Auto_Curseforge"]
    term_menu = TerminalMenu(options)
    menu_index = term_menu.show()
    
    if menu_index == 0:
        createVanilla()
    elif menu_index == 1:
        createSnapshot()
    elif menu_index == 2:
        createForge()
    elif menu_index == 3:
        createSpigot()
    elif  menu_index == 4:
        createCurseforge()