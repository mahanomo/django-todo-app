from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='base-todo'),
    path('create/',views.TodoCreateView.as_view(),name='create-todo'),
    path('delete/<int:pk>',views.TodoDeleteView.as_view(),name='delete-todo'),
    path('done/<int:pk>/', views.DoneTodoView.as_view(), name='done-todo'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update-todo'),
]