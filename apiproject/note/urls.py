from django.urls import path
from note import views
urlpatterns = [
    path('',views.createnote,name='create'),
    path('edit/(?P<id>\w+)',views.editnote,name='edit'),
    path('view/',views.viewnote,name='view'),
    path('del/(?P<id>\w+)',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    # path('home/',views.home,name="home"),
    path('GET/api/v1/notes',views.getlist,name="list"),
    path('POST/api/v1/notes',views.postlist,name="post"),
    path('GET/api/v1/notes/<str:pk>/',views.single_list,name="single"),
    path('PUT/api/v1/notes/<str:pk>/',views.updatelist,name="update"),
    path('DELETE/api/v1/notes/<str:pk>/',views.deletelist,name="delete_"),
]
