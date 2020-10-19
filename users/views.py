
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import BusinessForm, UserForm, CategoryForm
from django.utils.http import urlencode
import json
from django.shortcuts import render,get_object_or_404

from shelvesapp.models import Phone, Shoe, Laptop, Business, Customer
from shelvesapp.forms import PhoneForm


def registerView(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        business_form = BusinessForm(request.POST)
        categories_form = CategoryForm(request.POST)
        if business_form.is_valid() and user_form.is_valid() and categories_form.is_valid():
            picked = categories_form.cleaned_data.get("categories")
            user = user_form.save()
            business_form = business_form.save(commit=False)
            business_form.user = user
            business_form.dealers_in = json.dumps(picked)
            business_form.save()
            return render(request, "users/loginpage.html", {
                "message": "Registration complete! you may login now"
            })
    else:
        user_form = UserForm(request.POST)
        business_form = BusinessForm(request.POST)
        categories_form = CategoryForm(request.POST)
    context = {
        "business_form": business_form,
        "shelf_account_form": user_form,
        "categories_form": categories_form
    }
    return render(request, "users/registerpage.html", context)

def shelfView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        biz = request.GET.get("biz")
        categories = request.GET.get("list")
        pk = request.GET.get("i")
        meso = request.GET.get("message")
        try:
            phones = Phone.objects.filter(addedBy=pk)
        except Phone.DoesNotExist:
            raise Http404("No phones to show")
        try:
            shoes = Shoe.objects.filter(addedBy=pk)
        except Phone.DoesNotExist:
            raise Http404("No shoes to show")
        try:
            laptops = Laptop.objects.filter(addedBy=pk)
        except Phone.DoesNotExist:
            raise Http404("No laptops to show")

        context = {
            "categories_list": categories,
            "bisness": biz,
            "phones": phones,
            "shoes": shoes,
            "laptops": laptops,
            "message": meso
        }
    return render(request, "users/shelfpage.html", context)

def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['bizz'] = user.business.business_name
            categories = user.business.dealers_in
            json_dec = json.decoder.JSONDecoder()
            categories_list = json_dec.decode(categories)
            base_url = reverse("shelf")
            query_String = urlencode({"biz": user.business.business_name,
                                      "list": categories_list,
                                      "i": user.business.id,
                                      })
            url = '{}?{}'.format(base_url, query_String)
            return redirect(url)
        else:
            return render(request, "users/loginpage.html", {
                "message": "invalid credentials"
            })
    return render(request, "users/loginpage.html")

def logoutView(request):
    logout(request)
    return render(request, "users/loginpage.html",{
     "message": "logged out"
    })


def delete_phone(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        phone.delete()
        business = request.session["bizz"]
        b = Business.objects.get(business_name=business)
        categories = b.dealers_in
        json_dec = json.decoder.JSONDecoder()
        categories_list = json_dec.decode(categories)
        base_url = reverse("shelf")
        query_String = urlencode({"biz": b.business_name,
                                  "list": categories_list,
                                  "i": b.id,
                                  "message": "product added"
                                  })
        url = '{}?{}'.format(base_url, query_String)
        return redirect(url)
    context = {
        "phone": phone,
        "bisness": request.session["bizz"]
    }
    return render(request, "users/product_delete.html", context)


def update_phone(request, product_id):
    phone = get_object_or_404(Phone, id=product_id)
    phone_form = PhoneForm(request.POST or None, instance=phone)
    if phone_form.is_valid():
        phone_form.save()
        business = request.session["bizz"]
        b = Business.objects.get(business_name=business)
        categories = b.dealers_in
        json_dec = json.decoder.JSONDecoder()
        categories_list = json_dec.decode(categories)
        base_url = reverse("shelf")
        query_String = urlencode({"biz": b.business_name,
                                  "list": categories_list,
                                  "i": b.id,
                                  "message": "product added"
                                  })
        url = '{}?{}'.format(base_url, query_String)
        return redirect(url)
    context = {
        "phone": phone,
        "phone_form": phone_form
    }
    return render(request, "users/phoneUpdate.html", context)

def orders_view(request):
    b = request.session["bizz"]
    business = Business.objects.get(business_name=b)
    customer = Customer.objects.filter(business=business)
    context = {
        "business": b,
        "customer": customer
    }
    return render(request, "users/orders.html", context)

def delete_order_view(request, product_id):
    b = request.session["bizz"]
    business = Business.objects.get(business_name=b)
    customer = Customer.objects.filter(business=business)
    phone_customer = get_object_or_404(Customer, id=product_id)
    if request.method == "POST":
        phone_customer.delete()
        context = {
            "business": b,
            "customer": customer
        }
        return render(request, "users/orders.html", context)
    context = {
        "business": b,
        "customer": customer
    }
    return render(request, "users/orders.html", context)
