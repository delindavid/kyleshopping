from django.shortcuts import render, redirect

def index(request):
    if request.method == "POST":
        return redirect('shop')   # THIS MUST MATCH URL NAME
    return render(request, 'myapp/index.html')

def shop(request):
    return render(request, 'myapp/shop.html')

def shop1(request):
    return render(request, 'myapp/shop1.html')

def payment(request):
    if request.method == "POST":
        return redirect('success')

    return render(request, 'myapp/payment.html')

def success(request):
    return render(request, 'myapp/success.html')