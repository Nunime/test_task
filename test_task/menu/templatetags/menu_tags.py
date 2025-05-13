from django import template
from ..models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'items': []}
    
    items = list(menu.items.select_related('parent').all())
    nodes = {item.id: {'item': item, 'children': []} for item in items}
    root_nodes = []

    for node in nodes.values():
        parent_id = node['item'].parent_id
        if parent_id and parent_id in nodes:
            nodes[parent_id]['children'].append(node)
        else:
            root_nodes.append(node)

    return {'items': root_nodes}
