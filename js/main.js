document.getElementById('radio-vscode').click();

// ---------------------------------

function get_selected_editor() {
    let result_str = '';
    let vscode_radio = document.querySelector('input[id="radio-vscode"]:checked');
    let sublime_radio = document.querySelector('input[id="radio-sublime"]:checked');

    if (vscode_radio !== null) {
        result_str = 'code';
    } else if (sublime_radio !== null) {
        result_str = 'sublime';
    }

    return result_str;
}

function set_editor(editor) {
    set_acccolor(editor);
    set_apply_license_explanation(editor);
}

function set_acccolor(variant) {
    if (variant === 'code') {
        document.documentElement.style.setProperty('--color-primary', '#36a8ff');
    } else if (variant === 'sublime') {
        document.documentElement.style.setProperty('--color-primary', '#ff9c5b');
    }
}

function set_apply_license_explanation(editor) {
    const explanation_elements = document.querySelectorAll('[data-license-explanation]');

    explanation_elements.forEach((element) => {
        if (element.dataset.licenseExplanation === editor) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
}
function update_license_json(email, key) {
    const license_json = JSON.stringify({ email: email, license_key: key }, null, 2);
    document.getElementById('license-json').textContent = license_json;
    document.getElementById('license-explanation-update-placeholder').style.display = 'none';
}

function call_keygen() {
    let generated_key = '';
    let input_email = document.getElementById('input_email').value;
    let selected_editor = get_selected_editor();

    if (validateEmail(input_email) === false) {
        return false;
    }

    if (selected_editor === 'code') {
        generated_key = keygen_vscode(input_email);
    } else if (selected_editor === 'sublime') {
        generated_key = keygen_sublime(input_email);
    }

    display_output(generated_key);
}

function display_output(text_to_display) {
    let output_field = document.getElementById('result_output_box');
    let text_field = document.getElementById('result_output_text');
    let selected_editor = get_selected_editor();
    let email_field = document.getElementById('input_email');

    // Modify accent colors for outbut box bg gradient depending on the selected editor
    if (selected_editor == 'code') {
        document.documentElement.style.setProperty('--color-outputbox-0', '#2a78b4');
        document.documentElement.style.setProperty('--color-outputbox-1', '#3e468a');
    } else if (selected_editor == 'sublime') {
        document.documentElement.style.setProperty('--color-outputbox-0', '#ff6287');
        document.documentElement.style.setProperty('--color-outputbox-1', '#ff9c5b');
    }

    text_field.innerHTML = text_to_display;
    output_field.style.display = 'block';

    update_license_json(email_field.value, text_to_display);
}

function showToast({ text, isError = false }) {
    Toastify({
        text: text,
        duration: isError ? 10000 : 3000,
        style: {
            background: isError
                ? 'var(--color-error)'
                : 'linear-gradient(to right, var(--color-outputbox-0), var(--color-outputbox-1))',
            borderRadius: '4px',
            boxShadow: 'none',
        },
    }).showToast();
}

async function copy_key_to_clipboard() {
    const key = document.getElementById('result_output_text').textContent;

    try {
        await navigator.clipboard.writeText(key);
        showToast({
            text: 'License code is copied to the clipboard',
        });
    } catch (error) {
        const errorMessage = 'message' in error ? error.message : String(error);
        showToast({
            text: `Can not copy the license code to the clipboard. \n${errorMessage}`,
            isError: true,
        });
    }
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
        if (event.key === 'Enter') {
            call_keygen();
        }
    } else {
        email_input_field.className = 'error';
        button_generate.disabled = true;
    }
}
