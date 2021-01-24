from django.shortcuts import render
from todo_item.models import TodoItemModel
from main.models import ListModel

def todo_item_view(request,pk):
    my_todo_list=ListModel.objects.select_related('user').get(id=pk)
    todo_lists = TodoItemModel.objects.filter(list_model=my_todo_list)

    context = {'todo_lists': todo_lists,
               'user_name': my_todo_list.user.username,
               'item_name': my_todo_list.name

               }
    return render(request, 'todo_index.html', context)

