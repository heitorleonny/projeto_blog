from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_post', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('deletar_post/<int:post_id>/', views.deletar_post, name='deletar_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
