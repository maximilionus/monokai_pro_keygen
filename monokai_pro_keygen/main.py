import re
import sys
import signal
from hashlib import md5


__version__ = '1.0.0'
__author__ = 'maximilionus'
__default_email = 'maximilionuss@gmail.com'


def keygen_vscode(email: str) -> str:
    """
    Keygen for Visual Studio Code

    :param email: valid email address
    :type email: str
    :return: generated key for theme activation
    :rtype: str
    """
    filler_string = 'fd330f6f-3f41-421d-9fe5-de742d0c54c0'
    key_calculated = md5('{}{}'.format(filler_string, email).encode()).hexdigest()[:25]

    return keygen_insert_separator(key_calculated)


def keygen_sublime(email: str) -> str:
    """
    Keygen for Sublime Text 3

    :param email: valid email address
    :type email: str
    :return: generated key for theme activation
    :rtype: str
    """
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
            key_final += '-'
        else:
            key_final += letter

        counter += 1

    return key_final


def __process_input():
    selected_editor = ''
    selected_email = ''
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    print("Monokai Pro Theme - Key Generator (v{})\nby @{}".format(__version__, __author__))

    while True:
        selected_editor = input("----"
                                "\nselect your editor:"
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
        selected_email = input("----"
                               "\nprovide the email address (or press Enter to use '{}')"
                               "\n\n: ".format(__default_email))
        if len(selected_email) == 0:
            _print_action("using the default '{}' email address".format(__default_email))
            selected_email = __default_email
            break
        elif not email_regex.match(selected_email):
            _print_action("provide the valid email address", is_failure=True)
        else:
            _print_action("using the '{}' email address".format(selected_email))
            break

    passed = False
    if selected_editor == '1':  # VS Code
        key = keygen_vscode(selected_email)
        passed = True
    elif selected_editor == '2':  # Sublime Text
        key = keygen_sublime(selected_email)
        passed = True

    if passed:
        _print_action("key: {}".format(key), outline=True)

    input("\npress 'Enter' to exit")


def _print_action(text='', pre='', end='\n', is_failure=False, outline=False):
    mark = ("⮡ ❌" if is_failure else "⮡ ✅") if sys.stdout.encoding == 'utf-8' else '->'  # Set the mark accordingly to provided `is_failure` param and check `utf-8`
    outline_sample = '\n----\n' if outline else ''

    print(pre, outline_sample, mark, ' ' if len(text) > 0 else '', text, outline_sample, end=end)


def __handle_sigint():
    signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(1))


if __name__ == '__main__':
    __handle_sigint()
    __process_input()
