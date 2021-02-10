from cx_Freeze import setup, Executable
import sys

includes = [
    "background",
    "button",
    "constant",
    "leaderboard",
    "level",
    "players",
    "spridesheet",
    "levels"
]

packages = [
    "pygame",
    "json",
    "enum"
]

neededfiles = [
    ("./ressources/images/Dragon/Dragon_DOWN2.png", "./ressources/images/Dragon/Dragon_DOWN2.png"),
    ("./ressources/images/Dragon/Dragon_DOWN3.png", "./ressources/images/Dragon/Dragon_DOWN3.png"),
    ("./ressources/images/Dragon/Dragon_DOWN1.png", "./ressources/images/Dragon/Dragon_DOWN1.png"),
    ("./ressources/images/Dragon/Dragon_LEFT1.png", "./ressources/images/Dragon/Dragon_LEFT1.png"),
    ("./ressources/images/Dragon/Dragon_LEFT2.png", "./ressources/images/Dragon/Dragon_LEFT2.png"),
    ("./ressources/images/Dragon/Dragon_LEFT3.png", "./ressources/images/Dragon/Dragon_LEFT3.png"),
    ("./ressources/images/Dragon/Dragon_RIGHT1.png", "./ressources/images/Dragon/Dragon_RIGHT1.png"),
    ("./ressources/images/Dragon/Dragon_RIGHT2.png", "./ressources/images/Dragon/Dragon_RIGHT2.png"),
    ("./ressources/images/Dragon/Dragon_RIGHT3.png", "./ressources/images/Dragon/Dragon_RIGHT3.png"),
    ("./ressources/images/Dragon/Dragon_UP1.png", "./ressources/images/Dragon/Dragon_UP1.png"),
    ("./ressources/images/Dragon/Dragon_UP2.png", "./ressources/images/Dragon/Dragon_UP2.png"),
    ("./ressources/images/Dragon/Dragon_UP3.png", "./ressources/images/Dragon/Dragon_UP3.png"),
    ("./ressources/images/Dragon/flying_dragon-red-RGB.png", "./ressources/images/Dragon/flying_dragon-red-RGB.png"),
    ("./ressources/images/Dresseur/ballepokemon2.png", "./ressources/images/Dresseur/ballepokemon2.png"),
    ("./ressources/images/Dresseur/Dresseur.png", "./ressources/images/Dresseur/Dresseur.png"),
    ("./ressources/images/GameOver.png", "./ressources/images/GameOver.png"),
    ("./ressources/images/Game_background.png", "./ressources/images/Game_background.png"),
    ("./ressources/images/Heart.png", "./ressources/images/Heart.png"),
    ("./ressources/images/Leaderboard_background.png", "./ressources/images/Leaderboard_background.png"),
    ("./ressources/images/tiles_spritesheet.png", "./ressources/images/tiles_spritesheet.png"),
    ("./ressources/images/tiles_spritesheet2.png", "./ressources/images/tiles_spritesheet2.png"),
    ("./ressources/images/Title_background.png", "./ressources/images/Title_background.png"),
    ("./scores.json", "./scores.json")
]
base = None
if sys.platform == "win32":
    # base = 'Console'
    base = 'Win32GUI'
 

executables = [
    Executable("main.py",
            #    appendScriptToExe=True,
            #    appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

# Name of file to make ".exe" of
filename = "start_game.py"
setup(
    name = 'Dragonshotv0.1',
    version = '0.1',
    description = 'Cx test',
    options = {'build_exe': {'packages':packages,'includes':includes, "include_files":neededfiles}},
    executables = executables
    )