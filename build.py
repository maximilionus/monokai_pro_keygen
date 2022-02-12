import tarfile
from platform import machine
from shutil import make_archive, rmtree
from sys import platform as sys_platform
from os import path, chdir, mkdir, system as shell_exec
from argparse import ArgumentParser

from monokai_pro_keygen.main import __version__, _print_action

from PyInstaller.__main__ import run as pyi_run


ARCHIVE_NAME_TEMPLATE = r'monokai_pro_keygen_v{0}_{1}_{2}'
BUILD_PATH = './dist/exec/'
PACKED_DIR = './dist/packed/'


if __name__ == '__main__':
    if sys_platform == 'win32':
        # Force 'utf-8'
        shell_exec('chcp 65001')

    chdir(path.dirname(path.abspath(__file__)))

    parser = ArgumentParser(
        description='Build tool for creating the executable files'
    )

    parser.add_argument('--mode', type=str, default='one_file', choices=('one_file', 'one_dir'),
                        help='`one_file` - build project to single executable. '
                        '`one_dir` - build project to directory with all files in one location')
    parser.add_argument('--create-archive', action='store_true', help='built executable will be packed to archive '
                                                                      '(.tar.gz or .zip - according to platform) '
                                                                      'with special naming applied and saved to ./dist/packed/')

    args = parser.parse_args()
    pyi_params = []

    if args.mode == 'one_file':
        pyi_params = ['./monokai_pro_keygen/main.py', '--console', '--clean', '-y', '--name', 'monokai_pro_keygen', '--icon', './data/icons/icon_main.ico', '--distpath', BUILD_PATH, '--onefile', '--runtime-tmpdir', './']
    elif args.mode == 'one_dir':
        pyi_params = ['./monokai_pro_keygen/main.py', '--console', '--clean', '-y', '--name', 'monokai_pro_keygen', '--icon', './data/icons/icon_main.ico', '--distpath', BUILD_PATH, '--onedir']

    if path.isdir(BUILD_PATH):
        rmtree(path.abspath(BUILD_PATH))

    try:
        pyi_run(pyi_params)
    except Exception as e:
        _print_action('Build failed: {}'.format(e), is_failure=True, outline=True)
    else:
        _print_action('Successfull build to "{}"'.format(path.abspath(BUILD_PATH)), outline=True)

    # Pack executable to archive
    if args.create_archive:
        if not path.isdir(PACKED_DIR): mkdir(PACKED_DIR)

        archive_name = ARCHIVE_NAME_TEMPLATE.format(__version__, sys_platform, machine().lower())

        try:
            if sys_platform == 'win32':
                make_archive(path.join(PACKED_DIR, archive_name), 'zip', BUILD_PATH)
            else:
                with tarfile.open(path.abspath(path.join(PACKED_DIR, archive_name + '.tar.gz')), "w:gz") as tar:
                    tar.add(path.abspath(BUILD_PATH), arcname=archive_name)
        except Exception as e:
            _print_action('Packing failed: {}'.format(e), is_failure=True, outline=True)
        else:
            _print_action('Successfull packaging to "{}"'.format(path.abspath(path.join(PACKED_DIR))), outline=True)
