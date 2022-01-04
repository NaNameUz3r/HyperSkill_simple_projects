

def start_editor():
    formatters = ["plain", "bold", "italic",
                  "header", "link", "inline-code",
                  "ordered-list", "unordered-list", "new-line"]
    special_commands = ["!help", "!done", "!exit"]
    help_message = '''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
    Special commands: !help !done'''
    error_message = "Unknown formatting type or command"
    processed_text = ""
    while True:
        user_input = input("Choose a formatter:")
        if user_input in formatters:
            processed_text = markdown_text(processed_text, formatters.index(user_input))
            print(processed_text)
        elif user_input in special_commands:
            if user_input == special_commands[0]:
                print(help_message)
            elif user_input == special_commands[1]:
                save_markdown(processed_text)
                return True
            elif user_input == special_commands[2]:
                exit(0)
        else:
            print(error_message)
            continue


def markdown_text(processing_text, formatter_type):
    if formatter_type == 0:
        processing_text += input("Text:")
        return processing_text
    elif formatter_type == 1:
        processing_text += "**" + input("Text:") + "**"
        return processing_text
    elif formatter_type == 2:
        processing_text += "*" + input("Text:") + "*"
        return processing_text
    elif formatter_type == 3:
        while True:
            header_level = int(input("Level:"))
            if header_level < 1 or header_level > 6:
                print("The level should be within the range of 1 to 6")
                continue
            else:
                processing_text += "#" * header_level + " " + input("Text:") + "\n"
                return processing_text
    elif formatter_type == 4:
        link_label = input("Label:")
        link_url = input("URL:")
        processing_text += "[" + link_label + "](" + link_url + ")"
        return processing_text
    elif formatter_type == 5:
        processing_text += "`" + input("Text:") + "`"
        return processing_text
    elif formatter_type == 6:
        processing_text += markdown_list()
        return processing_text
    elif formatter_type == 7:
        processing_text += markdown_list(ordered=False)
        return processing_text
    elif formatter_type == 8:
        processing_text += "\n"
        return processing_text


def markdown_list(ordered=True):
    rows_to_process = ""
    while True:
        rows_count = int(input("Number of rows:"))
        if rows_count < 1:
            print("The number of rows should be greater than zero")
            continue
        else:
            for row in range(1, rows_count + 1):
                new_row = input(f'Row #{row}:') + '\n'
                if ordered:
                    rows_to_process += f'{row}. {new_row}'
                else:
                    rows_to_process += f'* {new_row}'
            return rows_to_process


def save_markdown(text_to_save):
    with open("output.md", "w") as markdown_file:
        markdown_file.write(text_to_save)


if __name__ == '__main__':
    start_editor()
