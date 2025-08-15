from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from datetime import date
from .models import Transaction
from .forms import TransactionForm

@login_required
def dashboard(request):
    today = date.today()
    qs = Transaction.objects.all()
    if request.user.is_authenticated:
        qs = qs.filter(user=request.user)

    month = qs.filter(date__year=today.year, date__month=today.month)
    spent = month.filter(t_type="expense").aggregate(s=Sum("amount"))["s"] or 0
    income = month.filter(t_type="income").aggregate(s=Sum("amount"))["s"] or 0
    net = income - spent

    ctx = {"spent": spent, "income": income, "net": net, "today": today}
    return render(request, "dashboard.html", ctx)

@login_required
def transaction_list(request):
    qs = Transaction.objects.filter(user=request.user)
    return render(request, "transactions/list.html", {"transactions": qs})

@login_required
def transaction_add(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "transactions/add.html", {"form": form})
