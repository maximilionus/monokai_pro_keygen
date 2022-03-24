function validateEmail (email) {
    return email.match(
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
}

function call_keygen() {
    let input_email = document.getElementById('input_email').value
    let vs_code_mode = document.querySelector('input[id="radio_mode_vscode"]:checked');
    let sublime_code_mode = document.querySelector('input[id="radio_mode_sublime"]:checked');

    if (validateEmail(input_email) === null) {
        return false;
    };

    if (vs_code_mode !== null) {
        display_output(keygen_vscode(input_email));
    } else if (sublime_code_mode !== null) {
        display_output(keygen_sublime(input_email));
    }
}

function display_output(text_to_display) {
    let output_field = document.getElementsByClassName("result_output_field")[0];
    let text_field = document.getElementsByClassName("result_output_text")[0];

    text_field.innerHTML = text_to_display;
    output_field.style.opacity = 100;
}

function input_field_keypress_handler(event) {
    if (event.key === "Enter") {
        call_keygen();
    } else {
        // Fix the visual response to email regex match
        let email_field = document.querySelector('#email_input_field');
        let email_input_field = email_field.children.input_email;

        if (validateEmail(email_input_field.value) != null) {
            email_input_field.setCustomValidity('');
        } else {
            email_input_field.setCustomValidity('wrong email');
        }
    }
}
