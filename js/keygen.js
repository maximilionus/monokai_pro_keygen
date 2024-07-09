function keygen_vscode(email) {
    filler_string = 'fd330f6f-3f41-421d-9fe5-de742d0c54c0';
    key_calculated = md5(filler_string + email).substring(0, 25);

    return keygen_insert_separator(key_calculated);
}

function keygen_sublime(email) {
    key_calculated = md5(email).substring(0, 25);

    return keygen_insert_separator(key_calculated);
}

function keygen_insert_separator(key_raw) {
    let key_final = '';

    for (var i = 0; i < key_raw.length; i++) {
        if (i % 5 == 0 && i != 25 && i != 0) key_final += '-' + key_raw.charAt(i);
        else key_final += key_raw.charAt(i);
    }

    return key_final;
}
