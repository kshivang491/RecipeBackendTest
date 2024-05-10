from django.urls import path
from accounts import views

urlpatterns = [
    path('users/', views.users, name="users"),
    path('user/<str:pk>', views.user, name="user"),
    path('signup/', views.signup, name="signup"),
    path('update/<str:pk>', views.update, name="modify"),
    path('delete/<str:pk>', views.delete, name="delete"),


    path('recipes/', views.recipes, name="recipes"),
    path('userrecipes/<str:pk>', views.userrecipes, name="userrecipes"),
    path('searchrecipes/', views.searchrecipes, name="searchrecipes"),
    path('addrecipe/', views.addrecipe, name="addrecipe"),
    path('deleterecipe/<str:pk>', views.deleterecipe, name="deleterecipe"),
    path('updaterecipe/<str:pk>', views.updaterecipe, name="updaterecipe"),
]