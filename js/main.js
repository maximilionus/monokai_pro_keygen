function call_keygen() {
    let input_email = document.getElementById('input_email').value
    let vscode_mode = document.querySelector('input[id="radio_mode_vscode"]:checked');
    let sublime_mode = document.querySelector('input[id="radio_mode_sublime"]:checked');

    if (validateEmail(input_email) === null) {
        return false;
    };

    if (vscode_mode !== null) {
        display_output(keygen_vscode(input_email));
    } else if (sublime_mode !== null) {
        display_output(keygen_sublime(input_email));
    }
}

function display_output(text_to_display) {
    let output_field = document.getElementsByClassName("result_output_field")[0];
    let text_field = document.getElementsByClassName("result_output_text")[0];

    text_field.innerHTML = text_to_display;
    output_field.style.opacity = 1;
}

function input_field_keypress_handler(event) {
    if (event.key === "Enter") {
        call_keygen();
    } else {
        // Fix the visual response to email regex match
        let input_container = document.querySelector('#input_container');
        let email_input_field = input_container.children.input_email;
        let button_generate = document.querySelector('#btn_generate');

        if (validateEmail(email_input_field.value) != null) {
            email_input_field.className = 'success';
            button_generate.disabled = false;
        } else {
            email_input_field.className = 'error';
            button_generate.disabled = true;
        }
    }
}
