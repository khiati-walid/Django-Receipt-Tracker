from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Receipt
from .forms import ReceiptForm, RegistrationForm


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("receipt_list")
    else:
        form = RegistrationForm()

    login_form = AuthenticationForm()

    return render(
        request,
        "registration/registration.html",
        {"form": form, "login_form": login_form},
    )


def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("receipt_list")

    login_form = AuthenticationForm()
    return render(request, "registration/login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login after logout


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, "receipts/receipt_list.html", {"receipts": receipts})


@login_required
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    return render(request, "receipts/receipt_detail.html", {"receipt": receipt})


@login_required
def receipt_new(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            return redirect("receipt_list")
    else:
        form = ReceiptForm()
    return render(request, "receipts/receipt_form.html", {"form": form})


@login_required
def receipt_edit(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_list")
    else:
        form = ReceiptForm(instance=receipt)
    return render(
        request, "receipts/receipt_edit.html", {"form": form, "receipt": receipt}
    )


@login_required
def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk, user=request.user)
    if request.method == "POST":
        receipt.delete()
        return redirect("receipt_list")
    return render(request, "receipts/receipt_confirm_delete.html", {"receipt": receipt})
