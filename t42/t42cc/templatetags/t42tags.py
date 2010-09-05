from django import template

register = template.Library()

class AdminLinkNode(template.Node):
    """Renderer for 'edit_link' tag
    """
    def __init__(self, obj):
        self.obj = obj

    def render(self, context):
        return repr(self.obj)

def edit_link(token):
    """Usage: {% edit_link some_obj %}
    """
    return AdminLinkNode(token)

register.simple_tag(edit_link)
