def format_name(f_name, l_name):
    """Formats input first and last name into title case."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_name_formatted = f_name.title()
    l_name_formatted = l_name.title()

    return f"{f_name_formatted} {l_name_formatted}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))