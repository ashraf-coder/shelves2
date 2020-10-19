from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .import views

urlpatterns = [
    path("laptops/", views.laptopView, name="laptops"),
    path("shoes/", views.shoesView, name="shoes"),
    path("phones/", views.phonesView, name="phones"),

    path("", views.homeView),
    path("shelf/phoneentry/", views.phoneEntryView, name="phones_form"),
    path("laptopentry/", views.laptopEntryView, name="laptops_form"),
    path("shoeentry/", views.shoeEntryView, name="shoes_form"),

    path("phones/<int:product_id>/", views.phones_details, name="phone_details"),
    path("phones/<int:product_id/customer/", views.phone_customer_entry, name="customer"),
    path("shoes/<int:product_id>/", views.shoe_details, name="shoe_details"),
    path("phones/<int:product_id>/other_phones/", views.otherProducts, name="other_phones"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)