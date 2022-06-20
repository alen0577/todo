
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.TaskListView.as_view(), name='home'),
    # path('add/', views.TaskCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.TaskUpdateView.as_view(), name='update')
]
