from django.urls import path
from .views import RegisterView, LoginView, UserView, Logout


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', Logout.as_view()),
    path(r'^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
    path(r'^makeshort/$', 'shorten_url', name='shortenurl')
]

