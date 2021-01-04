from django.shortcuts import render
item_data = {
    'item_lists': [
        {'name': 'Курс Python', 'is_done': False },
        {'name': 'Курс Kotlin', 'is_done': True,'date': '20.11.2020'},
        {'name': 'Курс Android', 'is_done': True,'date': '20.12.2020'},
        {'name': 'Курс глубоких нейронных сетей', 'is_done': True,'date': '25.12.2020'},
        {'name': 'Курс сенсорных систем', 'is_done': False}
    ],
    'user_name': 'Admin',
    'item_name':'Мои курсы'
}


def item_view(request):
    contex=item_data
    return render(request, 'item_index.html',contex)