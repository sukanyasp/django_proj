
from django.urls import path

from user.views import user_list, user_details, user_create

urlpatterns = [

    path('', user_list),
    path('<int:user_id>/', user_details ),
    path('create/', user_create ),


]