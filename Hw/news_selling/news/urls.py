from django.urls import path
from . import views

urlpatterns = [
    # path('',views.user),
    # path('data/',views.details),
    # path('update/',views.Update_record,name='update'),
    # path('delete/<int:id>',views.Delete_record,name='delete'),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout')
    
]