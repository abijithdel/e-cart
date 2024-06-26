from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('account/',views.account, name='account'),
    path('edit_account/',views.edit_profile, name="edit_account"),
    path('change_pass/',views.reset_pass, name="newpass"),
    path('account_delete/',views.delete_accout_user, name="delete_account"),
    path('logout',views.logout, name="logout")

]
