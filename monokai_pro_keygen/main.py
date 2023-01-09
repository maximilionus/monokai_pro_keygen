import re
import sys
import signal

from hashlib import md5
from getpass import getpass
from shutil import get_terminal_size

from argparse import ArgumentParser


__version__ = '1.1.1'
__app_name__ = 'Monokai Pro License Generator'
__author__ = 'maximilionus'
__default_email = 'maximilionuss@gmail.com'
__email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')


def keygen_vscode(email: str, disable_email_check=False) -> str:
    """
    Keygen for Visual Studio Code

    :param email: valid email address
    :type email: str
    :param disable_email_check: disable check for valid `email` address input, defaults to False
    :type disable_email_check: bool, optional
    :raises ValueError: if provided `email` is not valid
    :return: generated key for theme activation
    :rtype: str
    """
    if not disable_email_check:
        _verify_email(email)

    filler_string = 'fd330f6f-3f41-421d-9fe5-de742d0c54c0'
    key_calculated = md5('{}{}'.format(filler_string, email).encode()).hexdigest()[:25]

    return keygen_insert_separator(key_calculated)


def keygen_sublime(email: str, disable_email_check=False) -> str:
    """
    Keygen for Sublime Text 3

    :param email: valid email address
    :type email: str
    :param disable_email_check: disable check for valid `email` address input, defaults to False
    :type disable_email_check: bool, optional
    :raises ValueError: if provided `email` is not valid
    :return: generated key for theme activation
    :rtype: str
    """
    if not disable_email_check:
        _verify_email(email)

    key_calculated = md5('{}'.format(email).encode()).hexdigest()[:25]

    return keygen_insert_separator(key_calculated)


def keygen_insert_separator(key_source: str) -> str:
    """
    Generate the final key, ready for usage

    :param key_source: un-prepared key, basically raw md5 hash
    :type key_source: str
    :return: final key, ready for activation
    :rtype: str
    """
    counter = 1
    key_final = ''

    for letter in key_source:
        if counter % 5 == 0 and counter != 25:
            key_final += letter + '-'
        else:
            key_final += letter

        counter += 1

    return key_final


def __process_input():
    selected_editor = ''
    selected_email = ''

    __draw_sepline()
    print("{} version {}\nby @{}".format(__app_name__, __version__, __author__))

    while True:
        __draw_sepline()
        selected_editor = input("\nSelect your editor:"
                                "\n    1 - Visual Studio Code (VSCode)"
                                "\n    2 - Sublime Text"
                                "\n\n: "
                                )

        if selected_editor not in ('1', '2'):
            _print_action("wrong input", is_failure=True)
        else:
            _print_action("editor selected successfully")
            break

    while True:
        __draw_sepline()
        selected_email = input("\nProvide the valid email address (or press Enter to use '{}')"
                               "\n\n: ".format(__default_email))
        if len(selected_email) == 0:
            _print_action("using the default '{}' email address".format(__default_email))
            selected_email = __default_email
            break

        try:
            _verify_email(selected_email)
        except ValueError as e:
            _print_action('{}'.format(e), is_failure=True)
        else:
            _print_action("using the '{}' email address".format(selected_email))
            break

    passed = False
    if selected_editor == '1':  # VS Code
        key = keygen_vscode(selected_email, True)
        passed = True
    elif selected_editor == '2':  # Sublime Text
        key = keygen_sublime(selected_email, True)
        passed = True

    if passed:
        _print_action("key: {}".format(key), outline=True)

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        getpass("\nPress 'Enter' to exit")


def _print_action(text='', end='\n', is_failure=False, outline=False):
    # Check if `utf-8` encoding is used and modify output for correct printing
    if sys.stdout.encoding == 'utf-8':
        mark_fail = '⮡ ❌'
        mark_succ = '⮡ ✅'
    else:
        mark_fail = '-> [X]'
        mark_succ = '-> [V]'

    mark = mark_fail if is_failure else mark_succ

    if outline: __draw_sepline()
    print(mark, ' ' if len(text) > 0 else '', text, end=end)
    if outline: __draw_sepline()


def _verify_email(email: str) -> None:
    if not __email_regex.match(email):
        raise ValueError('provide the valid email address')


def __draw_sepline():
    terminal_width = get_terminal_size()[0]
    calculated_width = terminal_width - terminal_width // 2
    calculated_width = calculated_width if calculated_width >= 20 else 20

    print('-' * calculated_width)


def __handle_sigint():
    signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(1))


def __handle_cli() -> bool:
    cli_used = False
    parser = ArgumentParser(description='{} for Visual Studio Code and Sublime Text'.format(__app_name__))
    parser.add_argument('--email', '-E', help='provide the valid email address, defaults to \'maximilionuss@gmail.com\'', type=str, default=__default_email, action='store')
    parser.add_argument('--editor', '-M', help='select editor (\'code\' - VS Code, \'sublime\' - Sublime Text)', type=str, action='store', choices=('code', 'sublime'))
    parser.add_argument('--simple', help='(CLI mode only) print generated serial key without any decorations', action='store_true', default=False)
    parser.add_argument('--version', action='version', version='{} version {}'.format(__app_name__, __version__))

    args = parser.parse_args()

    if args.email is not None and args.editor is not None:
        try: _verify_email(args.email)
        except ValueError as e:
            _print_action('{}'.format(e), is_failure=True)
            sys.exit(1)

        if args.editor == 'code':
            key = keygen_vscode(args.email, disable_email_check=True)
        else:
            key = keygen_sublime(args.email, disable_email_check=True)

        if args.simple:
            print(key)
        else:
            _print_action("key: {}".format(key), outline=True)

        cli_used = True

    return cli_used


if __name__ == '__main__':
    if not __handle_cli():
        __handle_sigint()
        __process_input()
