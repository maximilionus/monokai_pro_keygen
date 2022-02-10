.PHONY: onefile, onedir


onefile:
	@echo "Starting the project build in single executable mode"
	@python -m PyInstaller ./keygen.py --clean -y --name monokai_pro_keygen --icon ./data/icons/icon_main.ico --onefile --runtime-tmpdir ./

onedir:
	@echo "Starting the default project build"
	@python -m PyInstaller ./keygen.py --clean -y --name monokai_pro_keygen --icon ./data/icons/icon_main.ico --onedir
