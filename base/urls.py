from django.contrib import admin
from django.urls import path
from .views import Tasklist,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLogin,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',Tasklist.as_view(),name='tasks'),
    path('task/<pk>',TaskDetail.as_view(),name='task'),
    path('task-create',TaskCreate.as_view(),name='task-create'),
    path('task-update/<pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<pk>',TaskDelete.as_view(),name='task-delete'),
    
    


]
