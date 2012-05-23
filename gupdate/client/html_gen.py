#this is a python file where i will create some basic html things
#this keeps the python clean and makes it so that I only need to make changes in one place =)

class generate_html():
    def head(items):
        return "<HEAD>" + items + "</HEAD>"

    def title(name):
        return "<TITLE>Gupdate: " + name + "</TITLE>"

    def list(items):
        item_list = []
        for item in items:
            item_list.append("<LI>" + item + "</LI>")
        return "<UL>" + item_list + "</UL>"

    def test():
        return """
<HTML>
    <BODY>
        <P>It Works!</P>
    </BODY>
</HTML>"""
