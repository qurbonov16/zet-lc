from django.urls import path
from .views import registration_view, login_view, logout_page, logout_confirm

urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout')
    path('logout/', logout_page, name='logout'),
    path('logout_confirm/', logout_confirm, name='logout_confirm'),

]
