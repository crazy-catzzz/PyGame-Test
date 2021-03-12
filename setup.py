import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Test Game",
    options={"build_exe": {"packages":["pygame"]}},
    executables = executables

    )