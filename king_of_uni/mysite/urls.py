"""coursework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from personal.views import (
    home_screen_view,
    rules_screen_view,
    leaderboard_view,
    privacy_policy_view
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name = "home"),
    path('rules/',rules_screen_view, name = "rules"),
    path('leaderboard', leaderboard_view, name="leaderboard"),
    path('register/', registration_view, name = "register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('privacy/', privacy_policy_view, name="privacy"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('game_keeper/', include('gameKeeper.urls', 'game_keeper')),
    path('territory_game/', include('territoryGame.urls', 'territory_game')),
    path('group/', include('group.urls', 'group')),


    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]
