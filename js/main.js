// Global vars
var generated_key = '';


function call_keygen() {
    let input_email = document.getElementById('input_email').value;
    let vscode_mode = document.querySelector('input[id="radio-vscode"]:checked');
    let sublime_mode = document.querySelector('input[id="radio-sublime"]:checked');

    if (validateEmail(input_email) === false) {
        return false;
    };

    if (vscode_mode !== null) {
        generated_key = keygen_vscode(input_email);
    } else if (sublime_mode !== null) {
        generated_key = keygen_sublime(input_email);
    }

    display_output(generated_key);
}

function display_output(text_to_display) {
    let output_field = document.getElementsByClassName("result_output_box")[0];
    let text_field = document.getElementsByClassName("result_output_text")[0];

    text_field.innerHTML = text_to_display;
    output_field.style.visibility = "visible";
    output_field.style.opacity = 1;
}

function copy_key_to_clipboard() {
    // TODO: Add fallback for unsupported engines
    navigator.clipboard.writeText(generated_key);
    window.alert("License code is copied to the clipboard");
}

function input_field_keypress_handler(event) {
    let input_container = document.querySelector('#input_container');
    let email_input_field = input_container.children.input_email;
    let button_generate = document.querySelector('#btn_generate');

    if (email_input_field.value.length == 0) {
        email_input_field.className = '';
        button_generate.disabled = true;
        return;
    }

    if (validateEmail(email_input_field.value) == true) {
        email_input_field.className = 'success';
        button_generate.disabled = false;
        if (event.key === "Enter") {
            call_keygen();
        }
    } else {
        email_input_field.className = 'error';
        button_generate.disabled = true;
    }
}
