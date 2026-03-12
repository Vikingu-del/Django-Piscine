#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        text = super().__str__()
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        return text.replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, msg="Error: Missing Content"):
            super().__init__(msg)

    def __init__(
        self,
        tag='div',
        attr={},
        content=None,
        tag_type='double'
    ):
        self.tag = tag
        self.attr = attr
        if content is not None and not Elem.check_type(content):
            raise Elem.ValidationError("Error: Invalid Content Type")
        if content is None:
            self.content = []
        elif not isinstance(content, list):
            self.content = [content]
        else:
            self.content = content
        self.tag_type = tag_type

    def __str__(self):
        result = ""
        attr = self.__make_attr()
        if self.tag_type == 'double':
            result = f"<{self.tag}{attr}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{attr}/>"
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            element_str = str(elem)
            if element_str:
                result += "  " + str(elem).replace('\n', '\n  ') + '\n'
        if result == '\n':
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError("Error: Missing Content")
        if isinstance(content, list):
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        is_single = isinstance(content, (Elem, Text))
        is_list = (isinstance(content, list) and
                   all(isinstance(e, (Elem, Text)) for e in content))
        return is_single or is_list


def main():
    try:
        html = Elem(
            tag='html',
            content=[
                Elem(
                    tag='head',
                    content=Elem(
                        tag='title',
                        content=Text('"Hello ground!"')
                    )
                ),
                Elem(
                    tag='body',
                    content=[
                        Elem(
                            tag='h1',
                            content=Text('"Oh no, not again!"')
                        ),
                        Elem(
                            tag='img',
                            attr={
                                'src': 'http://i.imgur.com/pfp3T.jpg'
                            },
                            tag_type='simple'
                        )
                    ]
                )
            ]
        )
        print(html)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    # 5. Replicating the required structure
    main()
