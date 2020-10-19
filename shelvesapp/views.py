import json
from tokenize import String

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import UpdateView
from multiselectfield.utils import string

from .models import Phone, Shoe,  Laptop, Business
from .forms import PhoneForm, LaptopForm, ShoeForm, CustomerForm
from django.contrib.auth.models import User


def homeView(request):
    return render(request, "shelvesapp/home2.html")


def phonesView(request):
    try:
        phones = Phone.objects.all()
    except Phone.DoesNotExist:
        raise Http404("No phones to show")
    context = {
        "phones": phones
    }
    return render(request, "shelvesapp/phonesviewpage2.html", context)

def shoesView(request):
    try:
        shoes = Shoe.objects.all()
    except Phone.DoesNotExist:
        raise Http404("No shoes to show")
    context = {
        "shoes": shoes
    }
    return render(request, "shelvesapp/shoesviewpage.html", context)

def laptopView(request):
    try:
        laptops = Laptop.objects.all()
    except Phone.DoesNotExist:
        raise Http404("No laptops to show")
    context = {
        "laptops": laptops
    }
    return render(request, "shelvesapp/laptopsviewpage.html", context)

def phoneEntryView(request):
    phone_form = PhoneForm()
    if request.method == "POST":
        phone_form = PhoneForm(request.POST, request.FILES)
        if phone_form.is_valid():
            business = request.session["bizz"]
            b = Business.objects.get(business_name=business)
            phone = phone_form.save(commit=False)
            phone.addedBy = b
            phone.save()
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
        "phone_form": phone_form,
    }
    return render(request, "shelvesapp/phoneEntryPage.html", context)

def laptopEntryView(request):
    laptop_form = LaptopForm()
    if request.method == "POST":
        laptop_form = LaptopForm(request.POST)
        if laptop_form.is_valid():
            business = request.session["bizz"]
            b = Business.objects.get(business_name=business)
            laptop = laptop_form.save(commit=False)
            laptop.addedBy = b
            laptop.save()
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
        "laptop_form": laptop_form,
    }
    return render(request, "shelvesapp/laptopEntrypage.html", context)

def shoeEntryView(request):
    shoe_form = ShoeForm()
    if request.method == "POST":
        shoe_form = ShoeForm(request.POST)
        if shoe_form.is_valid():
            business = request.session["bizz"]
            b = Business.objects.get(business_name=business)
            shoe = shoe_form.save(commit=False)
            shoe.addedBy = b
            shoe.save()
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
        "shoe_form": shoe_form,
    }
    return render(request, "shelvesapp/shoeEntrypage.html", context)

def phones_details(request, product_id):
    phone = get_object_or_404(Phone, id=product_id)
    request.session['pname'] = phone.name
    request.session['pmodel'] = phone.model
    request.session['pram'] = phone.RAM
    request.session['pstorage'] = phone.storage
    request.session['pcolor'] = phone.color
    print(request.session['pname'])
    context = {
        "phone": phone,
    }
    return render(request, "shelvesapp/productdisplay.html", context)

def phone_customer_entry(request):
    customer_form = CustomerForm()
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            p = request.session['pname']
            phone = Phone.objects.get(name=p,
                                      model=request.session["pmodel"],
                                      RAM=request.session["pram"],
                                      storage=request.session["pstorage"],
                                      color=request.session["pcolor"],)
            b = phone.addedBy
            business = Business.objects.get(business_name=b)
            customer = customer_form.save(commit=False)
            customer.business = business
            customer.productName = phone
            customer.save()
            context = {
                "phone": phone,
                "message": "seller notified"
            }
            return render(request, "shelvesapp/productdisplay.html", context)
    context = {
        "customer_form": customer_form,
    }
    return render(request, "shelvesapp/customerEntryPage.html", context)

def shoe_details(request, product_id):
    shoe = get_object_or_404(Shoe, id=product_id)
    context = {
        "shoe": shoe,
    }
    return render(request, "shelvesapp/productdisplay.html", context)


def otherProducts(request, product_id):
    phone = get_object_or_404(Phone, id=product_id)
    adder = phone.addedBy
    other = Phone.objects.filter(addedBy=adder)
    context = {
        "adder": adder,
        "phone": phone,
        "others": other
    }
    return render(request, "shelvesapp/shoppage.html", context)




