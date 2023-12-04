from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import message_form
from .views import delete_data
urlpatterns=[
    path('index/',views.index),
    path('login/',views.login),
    path('signup/',views.signup),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('booking/',views.booking),
    path('login_page/',views.login_page),
    path('base/',views.base),
    path('message/', message_form, name='message_form'),
    path('resto/delt/<int:pk>/', delete_data, name='delt_data'),
    path('nav/',views.nav),
]
