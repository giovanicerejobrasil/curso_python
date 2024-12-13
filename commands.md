#PyInstaller
## Direto no terminal
pyinstaller --name="Nome_do_Projeto" --noconfirm --onefile --add-data='pasta_dos_arquivos_necessários/:pasta_de_destino' --icon='pasta_do_ícone' --noconsole --clean --log-level=WARN --distpath="pasta_do_dist" --workpath="pasta_do_build" --specpath="pasta_do_.spec" arquivo_principal;

## Com .spec
pyinstaller --distpath="pasta_do_dist" --workpath="pasta_do_build" arquivo_principal;

#Recompilação do requirements.txt
pip freeze > requirements.txt