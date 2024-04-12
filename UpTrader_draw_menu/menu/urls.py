from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<path:menu_url>/', views.draw_menu, name='draw_menu')
]
