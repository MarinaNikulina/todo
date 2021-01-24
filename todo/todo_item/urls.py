from django.contrib import admin
from django.urls import path
from main.views import main_view
from todo_item.views import todo_item_view

app_name='todo_item'

urlpatterns = [
       path('', todo_item_view),
       path('<int:pk>', todo_item_view, name='todo_item')

]

