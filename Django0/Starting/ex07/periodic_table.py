class Element:

    def __init__(self, line: str):
        name_part, attr_part = line.strip().split("=")
        self.name = name_part.strip()
        attrs = {}
        for item in attr_part.split(","):
            key, value = item.split(":")
            attrs[key.strip()] = value.strip()
        self.position = int(attrs['position'])
        self.number = attrs['number']
        self.small = attrs['small']
        self.molar = attrs['molar']
        self.electron = attrs['electron']

    def __str__(self):
        return f"{self.name}, {self.position}, {self.number}, {self.small}, {self.electron}"
    
    def generate_td(self) -> str:
        """Returns the HTML representation of this specific element."""
        return f"""
                <td>
                    <h4>{self.name}</h4>
                    <ul>
                        <li>No {self.number}</li>
                        <li>{self.small}</li>
                        <li>{self.molar}</li>
                        <li>{self.electron} electron</li>
                    </ul>
                </td>"""


def process_file(filename: str) -> list[Element]:
    elements = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                elements.append(Element(line))
    return elements

def generate_html(elements: list[Element]) -> str:
    html_start = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Periodic Table</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <table>
                    <tr>"""
    content = ""
    current_col = 0 # Define it here!
    for el in elements:
        if el.position == 0 and el.name != "Hydrogen":
            content += "\n        </tr>\n        <tr>"
            current_col = 0
        while current_col < el.position:
            content += "<td></td>"
            current_col += 1
        content += el.generate_td()
        current_col += 1
    html_end = "\n        </tr>\n    </table>\n</body>\n</html>"
    return html_start + content + html_end

def generate_css() -> str:
    css_body = """td {
        border: 1px solid black;
        padding: 10px;
    }
    table {
        border-collapse: collapse;
    }"""
    return css_body
    

def generate_files():
    html = generate_html(process_file("periodic_table.txt"))
    with open("periodic_table.html", 'w') as f:
        f.write(html)
    print("Successfully generated periodic_table.html")
    css = generate_css()
    with open("style.css", 'w') as f:
        f.write(css)
        
if __name__ == "__main__":
    generate_files()