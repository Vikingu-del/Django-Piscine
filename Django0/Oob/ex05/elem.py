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

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
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
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ""
        attr = self.__make_attr()
        if self.tag_type == 'double':
            result = f"<{self.tag}{attr}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{attr}/>"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

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
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or isinstance(content, Text) or
                (isinstance(content, list) and all([isinstance(elem, Text) or
                                                    isinstance(elem, Elem)
                                                    for elem in content])))


def main():
    html = Elem(tag='html', content=[
        Elem(
            tag='head',
            content=Elem(tag='title', content=Text('"Hello ground!"'))),
        Elem(tag='body', content=[
            Elem(tag='h1', content=Text('"Oh no, not again!"')),
            Elem(
                tag='img',
                attr={'src': 'http://i.imgur.com/pfp3T.jpg'},
                tag_type='simple')
        ])
    ])
    print(html)


if __name__ == '__main__':
    main()
