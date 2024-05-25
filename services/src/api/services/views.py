from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Import Inventory and Item from term-util/libs
from inventory.Inventory import Inventory
from inventory.Item import Item

@csrf_exempt
def inventory_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        items = data.get('items')

        if items == "*":
            inventory_items = Inventory.objects.filter(user_id=user_id)
        elif isinstance(items, list):
            inventory_items = Inventory.objects.filter(user_id=user_id, item__name__in=items)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)

        result = {item.item.name: item.quantity for item in inventory_items}
        return JsonResponse(result, status=200)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
