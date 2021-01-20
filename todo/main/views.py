from django.shortcuts import render
from main.models import ListModel


# data = {
#     'lists': [
#         {'name': 'Работа', 'is_done': True, 'date': '01.12.2019'},
#         {'name': 'Дом', 'is_done': False},
#         {'name': 'Учеба', 'is_done': True}
#     ],
#     'user_name': 'Asus',
# }


def main_view(request):
    # try:
    #     lists=ListModel.objects.get(id=1)
    # except ListModel.DoesNotExist:
    #     pass
    # except ListModel.MultipleObjectsReturned:
    #     raise

    #   lists=ListModel.objects.filter(user_id=request.user.id)
    #    new_list=ListModel(
    #        name='Новый список',
    #        user=request.user
    #    )
    #
    #    new_list.save()
    #    new_list = ListModel.objects.create(
    #        name='Новый список3',
    #        user=request.user
    #    )
    # динамическая генерация списков
    # new_list = [
    #     ListModel.objects.create(
    #         name = 'Новый список{i}',
    #         user=request.user,
    #     )
    #     for i in [6.7.8]
    # ]
    # for i in new_list:
    #     i.save()

    lists = ListModel.objects.filter(user=request.user)

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)
