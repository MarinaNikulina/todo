from django.contrib import admin
from django.urls import path
from main.views import main_view
from list_item.views import item_view

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', main_view),
    path('list_item/', item_view)

}