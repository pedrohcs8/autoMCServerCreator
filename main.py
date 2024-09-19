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