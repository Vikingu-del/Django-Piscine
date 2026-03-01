#!/usr/bin/env python3

import sys, os, re


# Function to open and read a file
def process_file(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            template_content = f.read()
            return template_content
    except PermissionError:
        print(f"Error: Permission denied for {filename}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: {filename} not found")


# Parses the global settings
def parse_settings() -> None:
    settings_path = os.path.join(os.path.dirname(__file__), "settings.py")
    settings = {}
    try:
        with open(settings_path, "r") as f:
            for line in f:
                matched = re.match(r'(\w+)\s*=\s*"([^"]+)"', line)
                if matched:
                    key, value = matched.groups()
                    settings[key] = value
            globals().update(settings)
    except FileNotFoundError:
        print("Error: settings.py not found")
        sys.exit(1)


# Creates the structure of an Html Dom
def create_htmlDom() -> str:
    return  """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Cv</title>
</head>
<body>
    {content}
</body>
</html>"""


# Creates a file filename.html
def create_index(html: str, filename: str) -> None:
    try:
        with open(filename, 'w') as f:
            f.write(html)
        print(f"File {filename} created")
    except PermissionError:
        print(f"You dont have permissions to write in {filename}")
    except IsADirectoryError:
        print(f"{filename} is a directory not a file")
    except OSError:
        print(f"No space left on device")
    except UnicodeDecodeError:
        print("You are trying to write characters that cannot be encoded by the default character encoding")



def main():
    args = sys.argv
    if len(args) == 2:
        parse_settings()
        if args[1].endswith(".template"):
            content = process_file(args[1])
            html = create_htmlDom()
            rendered_content = html.format(content=content.format(**globals()))
            create_index(rendered_content, "index.html")
        else:
            print("Wrong file extension, template file must end with .template")
    else:
        print("Usage: python3 render.py <file.template>")


if __name__ == '__main__':
    main()