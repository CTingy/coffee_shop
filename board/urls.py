from django.urls import path
from board import views

app_name = 'board'
urlpatterns = [
    path('', views.board, name='board'),
    path('<int:pk>/', views.BoardDetailView.as_view(), name='board'),
    path('create_board/', views.create_board, name='create_board'),
    path('update_board/<int:board_id>/', views.update_board, name='update_board'),
    path('delete_board/<int:board_id>/', views.delete_board, name='delete_board'),
]