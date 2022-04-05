<img src="./data/icons/icon_main.png" height=128>

# Monokai Pro - Keygen

- [Monokai Pro - Keygen](#monokai-pro---keygen)
  - [Note](#note)
  - [About](#about)
  - [Usage](#usage)
  - [CLI](#cli)
  - [Build](#build)


## Note
New web version of serial key generator, which doesn't require any executables to be downloaded, was developed and and delpoyed to Github Pages, available [on this link](https://maximilionus.github.io/monokai_pro_keygen).

> Source code is also available on branch `page` of this repository


## About

Monokai Pro theme keygen tool for **Visual Studio Code** and **Sublime Text**


## Usage
### Binary
1. Download the [latest release](https://github.com/maximilionus/monokai_pro_keygen/releases/latest/) binary for your platform
2. Start the `monokai_pro_keygen` executable
3. Follow the instructions to generate the key
4. Copy the key and use it in your editor

### Execute from web
- Since this tool does not require third-party packages you can easily run it from source code. Just ensure that you have `python 3` interpreter installed with version higher than `3.6` and move on to the next step

- Executing the command below in your command shell will launch a local python interpreter, load the main script *(`./monokai_pro_keygen/main.py`)* from this repository and execute it
    ```bash
    python3 -c "import urllib.request;exec(urllib.request.urlopen('https://github.com/maximilionus/monokai_pro_keygen/raw/master/monokai_pro_keygen/main.py').read())"
    ```
    > On Windows platform replace `python3` with `python`


## CLI
### About
Since version `1.1.0`, this tool now supports `cli` *(command line interface)* interactions, meaning that all required data for serial key generation *(email, editor)* can be provided with just one command.

This feature is available for all variants of this tool *(python version)* - [built executable](#binary), [web execution](#execute-from-web), source code run.

### Arguments
| argument         | description                                                |
| :--------------- | :--------------------------------------------------------- |
| `--email`, `-E`  | valid email address, defaults to 'maximilionuss@gmail.com' |
| `--editor`, `-M` | select editor ('code' - VS Code, 'sublime' - Sublime Text) |
| `--simple`       | print generated serial key without any decorations         |

### Example
```bash
$ ./monokai_pro_keygen -h
usage: monokai_pro_keygen [-h] [--email EMAIL] [--editor {code,sublime}] [--simple]

Monokai Pro theme license key generator for Visual Studio Code and Sublime Text

optional arguments:
  -h, --help            show this help message and exit
  --email EMAIL, -E EMAIL
                        provide the valid email address, defaults to 'maximilionuss@gmail.com'
  --editor {code,sublime}, -M {code,sublime}
                        select editor ('code' - VS Code, 'sublime' - Sublime Text)
  --simple              print generated serial key without any decorations
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
   > You can also run the command below to get all available commands in build script
   > ```bash
   > $ pipenv run python build.py -h  # -h || --help
   > ```
5. After a successful build, the executable file can be found in the `./dist/exec` directory
