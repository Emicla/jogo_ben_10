import cx_Freeze

executables = [cx_Freeze.Executable(
    script="jogo.py", icon="Imagens/controle.ico")]

cx_Freeze.setup(
    name="Fly Heroes",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Imagens"]
                           }},
    executables = executables
)