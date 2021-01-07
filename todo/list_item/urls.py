from django.urls import path
from list_item.views import item_view

app_name= 'list_item'

urlpatterns = {
       path('', item_view)
}