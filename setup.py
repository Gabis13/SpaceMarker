import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]

cx_Freeze.setup (
    name = "SpaceMarker",
    options = {
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                "bg.jpg"
                "click.mp3"
                "loading.mp3"
                "Space_Machine_Power.mp3"
                "space.ico"
                "space.png"
                "README.md"
            ]
        }
    }, executables = executables
)