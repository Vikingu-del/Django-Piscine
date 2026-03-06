#!/usr/bin/python3

from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', content=content, attr=attr, tag_type='double')


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', content=content, attr=attr, tag_type='double')


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', content=content, attr=attr, tag_type='double')


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', content=content, attr=attr, tag_type='double')


class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='meta', content=None, attr=attr, tag_type='simple')


class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', content=content, attr=attr, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', content=content, attr=attr, tag_type='double')


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', content=content, attr=attr, tag_type='double')


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', content=content, attr=attr, tag_type='double')


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', content=content, attr=attr, tag_type='double')


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', content=content, attr=attr, tag_type='double')


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', content=content, attr=attr, tag_type='double')


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', content=content, attr=attr, tag_type='double')


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', content=content, attr=attr, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', content=content, attr=attr, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', content=content, attr=attr, tag_type='double')


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', content=content, attr=attr, tag_type='double')


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', content=content, attr=attr, tag_type='double')


class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', content=content, attr=attr, tag_type='simple')


class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', content=content, attr=attr, tag_type='simple')


def main():
    filename = "index.html"
    try:
        # Create the object first to catch ValidationErrors before opening the file
        content = Html([
            Head(Title(Text('"Hello ground!"'))),
            Body([
                H1(Text("Oh no, not again!")),
                Img(None, {"src": "http://i.imgur.com/pfp3T.jpg"})
            ])
        ])
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(content))
            
    except Elem.ValidationError as e:
        print(f"Content Validation Error: {e}")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory.")
    except (OSError, IOError) as e:
        # This catches "No space left" and other system/disk issues
        print(f"System/Disk Error: {e}")
    except Exception as e:
        # Catch-all for anything unexpected
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()