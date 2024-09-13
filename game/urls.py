from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from .views import custom_404_view, custom_500_view
from django.conf.urls import handler400
from .views import custom_400_view
urlpatterns = [
    path('', views.home, name='home'),
    
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('turnaments/', views.turnaments, name='turnaments'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about-us'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms-and-conditon/', views.terms_conditon, name='terms_conditon'),
    path('cancellation-refund/', views.cancellation, name='cancellation'),
    path('login', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('game-paas/', views.game_paas, name='game_paas'),
    path('Profile/', views.profile_update_view, name='profile_update'),  # Profile update URL
    path('profile/social-links/', views.social_links_update_view, name='social_links_update'),  # Social media links update URL
    path('tournament/<slug:slug>/', views.turnament_description, name='turnament_description'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('report/<str:username>/', views.user_report, name='user_report'),
     path('join-tournament/<int:tournament_id>/', views.join_tournament, name='join_tournament'),

]

# These handlers point to the custom error views
handler404 = 'game.views.custom_404_view'
handler500 = 'game.views.custom_500_view'

handler400 = 'game.views.custom_400_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)