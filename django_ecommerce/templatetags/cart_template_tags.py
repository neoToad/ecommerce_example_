from django import template
from ..models import Order, OrderItem

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs1 = Order.objects.filter(user=user, ordered=False)
        qs = OrderItem.objects.filter(user=user, ordered=False)
        if qs1.exists():
            if qs1[0].items.count() > 0:
                total_items = 0
                for x in qs:
                    print(x.quantity)
                    total_items += x.quantity
                return total_items
            else:
                return 0
    return 0
