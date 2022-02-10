import re
from hashlib import md5


__version__ = '1.0.0'
__default_email = 'maximilionuss@gmail.com'


def keygen_vscode(email: str) -> str:
    filler_string = 'fd330f6f-3f41-421d-9fe5-de742d0c54c0'
    key_calculated = md5('{}{}'.format(filler_string, email).encode()).hexdigest()[:25]

    counter = 1
    key_final = ''

    for letter in key_calculated:
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

    print("Monokai Pro Theme - Key Generator (v{})".format(__version__))

    while True:
        selected_editor = input("----"
                                "\nselect your editor:"
                                "\n    1 - Visual Studio Code (VSCode)"
                                "\n    2 - Sublime Text"
                                "\n\n: "
                                )

        if selected_editor not in ('1', '2'):
            __print_action("wrong input", is_failure=True)
        else:
            __print_action("editor selected successfully")
            break

    while True:
        selected_email = input("----"
                               "\nprovide the email address (or press Enter to use '{}')"
                               "\n\n: ".format(__default_email))
        if len(selected_email) == 0:
            __print_action("using the default '{}' email address".format(__default_email))
            selected_email = __default_email
            break
        elif not email_regex.match(selected_email):
            __print_action("provide the valid email address", is_failure=True)
        else:
            __print_action("using the '{}' email address".format(selected_email))
            break

    if selected_editor == '1':  # VS Code
        key = keygen_vscode(selected_email)
        __print_action("key: {}".format(key), outline=True)
    elif selected_editor == '2':  # Sublime Text
        pass


def __print_action(text='', pre='', end='\n', is_failure=False, outline=False):
    mark = "⮡ ❌" if is_failure else "⮡ ✅"
    outline_sample = '\n----\n' if outline else ''

    print(pre, outline_sample, mark, ' ' if len(text) > 0 else '', text, outline_sample, end=end)


if __name__ == '__main__':
    __process_input()
