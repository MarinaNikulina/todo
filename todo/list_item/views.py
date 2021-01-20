from django.shortcuts import render
from list_item.models import ListItemModel

# item_data = {
#     'item_lists': [
#         {'name': 'Курс Python', 'is_done': False },
#         {'name': 'Курс Kotlin', 'is_done': True,'date': '20.11.2020'},
#         {'name': 'Курс Android', 'is_done': True,'date': '20.12.2020'},
#         {'name': 'Курс глубоких нейронных сетей', 'is_done': True,'date': '25.12.2020'},
#         {'name': 'Курс сенсорных систем', 'is_done': False}
#     ],
#     'user_name': 'Admin',
#     'item_name':'Мои курсы'
# }


def item_view(request):
    item_lists = ListItemModel.objects.filter(
        user=request.user,
        id=1
    )

    contex = {'item_lists': item_lists,
              'user_name': request.user.username
              }
    return render(request, 'item_index.html', contex)
