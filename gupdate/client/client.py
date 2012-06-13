#These functions generate client end content

import html_gen
html = html_gen.generate_html()

class page:
    def default(self):
        head = html.header(html.title("GUpdate ~ Test"))
        body = html.body(html.ul(["data","more data","other data"]))
        return head + body
    def test(self):
        return html.test()
