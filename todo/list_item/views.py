from django.shortcuts import render
from list_item.models import ListItemModel
from main.models import ListModel

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


def item_view(request,pk):

    my_list=ListModel.objects.select_related('user').get(id=pk)
    item_lists = ListItemModel.objects.filter(list_model=my_list)

    context = {'item_lists': item_lists,
               'user_name': my_list.user.username,
               'item_name': my_list.name
               }
    return render(request, 'list_index.html', context)
