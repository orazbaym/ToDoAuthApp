from django.urls import path
from . import views

app_name = "tasks"   

urlpatterns = [
		path('', views.index, name="list"),
		
		path("register/", views.register_request, name="register"),
		path("login/", views.login_request, name="login"),
		path("logout/", views.logout_request, name= "logout"),
		path('update_task/<str:pk>/', views.updateTask, name="update_task"),
		path('delete/<str:pk>/', views.deleteTask, name="delete"),
		
		

]
