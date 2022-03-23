function display_output(text_to_display) {
    output_field = document.getElementsByClassName("result_output_field")[0];
    text_field = document.getElementsByClassName("result_output_text")[0];

    text_field.innerHTML = text_to_display;
    output_field.style.opacity = 100;
}
