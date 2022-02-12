<img src="./data/icons/icon_main.png" height=128>

# Monokai Pro - Keygen

- [Monokai Pro - Keygen](#monokai-pro---keygen)
  - [About](#about)
  - [Usage](#usage)
    - [Binary](#binary)
    - [Source](#source)
  - [Build](#build)


## About

Monokai Pro theme keygen for VSCode and Sublime Text


## Usage
### Binary
1. Download the [latest release](https://github.com/maximilionus/monokai_pro_keygen/releases/latest/) binary for your platform
2. Start the `monokai_pro_keygen` executable
3. Follow the instructions to generate the key
4. Copy the key and use it in your editor

### Source
- Since this application does not require third-party packages you can easily run it from source code. Just ensure that you have `python 3` interpreter installed with version higher than `3.6` and move on to the next step

- Executing the command below in your command shell will launch a local python interpreter, load the main script *(`./monokai_pro_keygen/main.py`)* from this repository and execute it
    ```bash
    $ python -c 'import urllib.request;exec(urllib.request.urlopen("https://github.com/maximilionus/monokai_pro_keygen/raw/master/monokai_pro_keygen/main.py").read())'
    ```


## Build
1. Clone this repository
2. Install the `pipenv` package
   ```bash
   $ python -m pip install pipenv
   ```
3. Install the project dependencies with `pipenv`
   ```bash
   $ pipenv install
   ```
4. Run the build script
   ```bash
   $ pipenv run python build.py
   ```
5. After a successful build, the executable file can be found in the `./dist/exec` directory
