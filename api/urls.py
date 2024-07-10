from django.urls import path
from . import views as apiapp_views

urlpatterns = [
    path('books/',apiapp_views.getData,name='books'),
    path('books/<int:id>/',apiapp_views.getDataDetail,name='books_id')
]