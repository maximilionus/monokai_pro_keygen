function set_acccolor(variant) {
    if (variant === 'code') {
        document.documentElement.style.setProperty('--color-primary', '#36a8ff');
    } else if (variant === 'sublime') {
        document.documentElement.style.setProperty('--color-primary', '#ff9c5b');
    }
}

function call_keygen() {
    let generated_key = '';
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
    let output_field = document.getElementById("result_output_box");
    let text_field = document.getElementById("result_output_text");

    text_field.innerHTML = text_to_display;
    output_field.style.visibility = "visible";
    output_field.style.opacity = 1;
}

function copy_key_to_clipboard() {
    let key_str = document.getElementById('result_output_text').textContent;

    // TODO: Add fallback for unsupported engines
    navigator.clipboard.writeText(key_str)
        .then(() => {
            window.alert("License code is copied to the clipboard");
        })
        .catch(() => {
            window.alert("Can not copy the license code to the clipboard. This feature is probably unsupported by your browser.");
        });
}

function input_field_keypress_handler(event) {
    let email_input_field = document.getElementById('input_email');
    let button_generate = document.getElementById('btn_generate');

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
