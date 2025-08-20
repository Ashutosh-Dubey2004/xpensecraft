from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from datetime import date
from .models import Transaction
from .forms import TransactionForm

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

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
    return render(request, "transactions/dashboard.html", ctx)

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, "transactions/list.html", {"transactions": transactions})


@login_required
def transaction_add(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # link to current user
            transaction.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "transactions/add.html", {"form": form})

