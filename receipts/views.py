from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipt
from .forms import ReceiptForm


def receipt_list(request):
    receipts = Receipt.objects.all()
    return render(request, "receipts/receipt_list.html", {"receipts": receipts})


def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    return render(request, "receipts/receipt_detail.html", {"receipt": receipt})


def receipt_new(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.save()
            return redirect("receipt_list")
    else:
        form = ReceiptForm()
    return render(request, "receipts/receipt_form.html", {"form": form})


def receipt_edit(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
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


def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == "POST":
        receipt.delete()
        return redirect("receipt_list")
    return render(request, "receipts/receipt_confirm_delete.html", {"receipt": receipt})
