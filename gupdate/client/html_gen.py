#this is a python file where i will create some basic html things
#this keeps the python clean and makes it so that I only need to make changes in one place =)

class generate_html:
    def header(self,items = None):
        return "<HEAD>" + items + "</HEAD>"

    def title(self,name):
        return "<TITLE>Gupdate: " + name + "</TITLE>"

    def ul(self,items):
        item_str = ""
        for item in items:
            item_str += ("<LI>" + item + "</LI>")
        return "<UL>" + item_str + "</UL>"

    def body(self, items = None):
        return "<BODY>"+items+"</BODY>"
    
    def test(self):
        return """
<HTML>
    <BODY>
        <P>It Works!</P>
    </BODY>
</HTML>"""
