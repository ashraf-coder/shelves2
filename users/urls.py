from django.urls import path

from . import views

urlpatterns = [
    path("shelf/", views.shelfView, name="shelf"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("register/", views.registerView, name="register"),

    path("shelf/delete/<int:id>/", views.delete_phone, name="delete"),
    path("shelf/update/<int:product_id>/", views.update_phone, name="update"),
    path("shelf/order/", views.orders_view,  name="orders"),
    path("shelf/order/<int:product_id>/order", views.delete_order_view, name="delete-order")
]