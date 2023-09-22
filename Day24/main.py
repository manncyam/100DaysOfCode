PLACEHOLDER = "[name]"

def get_file_content(file_path):
    with open(file_path) as f:
        content = f.read()

    return content

def get_letter_template():
    return get_file_content("Input/Letters/starting_letter.txt")

def get_name_list():
    content = get_file_content("Input/Names/invited_names.txt")
    name_list = content.split("\n")

    return name_list

def generate_letter(template, name):
    return template.replace(PLACEHOLDER, name)

def save_letter(letter, name):
    with open(f"Output/ReadyToSend/invited_{name}.txt", mode="w") as of:
        of.write(letter)

def main():
    template = get_letter_template()    
    name_list = get_name_list()

    for name in name_list:
        letter = generate_letter(template, name)
        save_letter(letter, name)

if __name__ == "__main__":
    main()