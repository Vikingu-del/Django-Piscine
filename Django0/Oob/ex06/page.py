from elem import Elem, Text
from elements import (
    Html, Head, Body, Title, Meta, Img, Table,
    Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
)


class Page:

    def __init__(self, root: Elem):
        if not isinstance(root, Elem):
            raise Elem.ValidationError("Root must be an instance of Elem")
        self.root = root

    def __str__(self):
        result = ""
        if isinstance(self.root, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.root)
        return result

    def write_to_file(self, filename: str):
        if not self.is_valid():
            raise Elem.ValidationError("The document is not valid")
        with open(filename, "w") as f:
            f.write(self.__str__())
        

    def __recursive_check(self, node) -> bool:
        allowed_types = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td,
                         Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)

        if not isinstance(node, allowed_types):
            return False

        if isinstance(node, Html):
            if (len(node.content) != 2 or
                    not isinstance(node.content[0], Head) or
                    not isinstance(node.content[1], Body)):
                return False

        elif isinstance(node, Head):
            titles = [c for c in node.content if isinstance(c, Title)]
            if len(titles) != 1:
                return False

        elif isinstance(node, (Body, Div)):
            valid_children = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            if not all(isinstance(c, valid_children) for c in node.content):
                return False

        elif isinstance(node, P):
            if not all(isinstance(c, Text) for c in node.content):
                return False

        elif isinstance(node, (Ul, Ol)):
            if len(node.content) == 0 or\
                    not all(isinstance(c, Li) for c in node.content):
                return False

        elif isinstance(node, Tr):
            if len(node.content) == 0:
                return False

            has_th = any(isinstance(c, Th) for c in node.content)
            has_td = any(isinstance(c, Td) for c in node.content)
            if (has_th and has_td) or\
                    not all(isinstance(c, (Th, Td)) for c in node.content):
                return False

        elif isinstance(node, Table):
            if not all(isinstance(c, Tr) for c in node.content):
                return False

        elif isinstance(node, Span):
            if not all(isinstance(c, (P, Text)) for c in node.content):
                return False

        elif isinstance(node, (Title, H1, H2, Li, Th, Td)):
            if len(node.content) != 1 or not isinstance(node.content[0], Text):
                return False

        if isinstance(node, Elem):
            for child in node.content:
                if not self.__recursive_check(child):
                    return False

        return True

    def is_valid(self) -> bool:
        return self.__recursive_check(self.root)


def main():
    valid_p = Page(
        Html(
            [
                Head(
                    [
                        Title(Text("Erik")),
                        Meta(attr={"charset": "UTF8"}),
                        Meta(attr={
                            "name": "viewport",
                            "content": "width=device-width, initial-scale=1.0"
                        })
                    ]
                ),
                Body(
                    [
                        H1(Text("A test Exercise")),
                        H2(Text("Tables")),
                        Table([
                            Tr([
                                Th(Text("First Table Header")),
                                Th(Text("Second Table Header")),
                                Th(Text("Third Table Header"))
                            ]),
                            Tr([
                                Td(Text("First Table Data")),
                                Td(Text("Second Table Data")),
                                Td(Text("Third Table Data"))
                            ])
                        ]),
                        Div([
                            H2(Text("Div and Lists")),
                            Div([
                                Span(
                                    P(Text("Unordered lists")),
                                ),
                                Ul([
                                    Li(Text("First element")),
                                    Li(Text("Second element")),
                                    Li(Text("Third element"))
                                ]),
                                Span(
                                    P(Text("Ordered lists")),
                                ),
                                Ol([
                                    Li(Text("First element")),
                                    Li(Text("Second element")),
                                    Li(Text("Third element"))
                                ])
                            ])
                        ])
                    ]
                )
            ],
            attr={"lang": "en"}
        )
    )
    valid_p.write_to_file("index.html")
    


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
