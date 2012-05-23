#These functions generate client end content

import html_gen
html = html_gen.generate_html()

class page():
    def default():
        return html.test()
