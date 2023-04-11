from django.shortcuts import render, redirect, HttpResponse
from .models import Coffee, Burger
from .forms import CoffeeForm

# Create your views here.
def coffee_view(request, pk=None):
    if pk:
        try:
            coffee = Coffee.objects.get(cid=pk)
        except Exception as err:
            return HttpResponse(f"Coffee ID '{pk}' does not exist!")
        
        method = request.POST.get('_method', '')
        print(method)
        if method == 'PUT':
            put_form = CoffeeForm(request.POST)
            print(put_form.is_valid())
            coffee.name = put_form['name'].value()
            coffee.price = put_form['price'].value()
            coffee.is_ice = put_form['is_ice'].value()
            coffee.stock = put_form['stock'].value()
            coffee.save()
            return redirect('/coffees')

        elif method == 'DELETE':
            coffee.delete()
            return redirect('/coffees')
        
        coffee_all = [coffee]
        put_form = CoffeeForm()

        return render(request, 'coffee.html', {
        "coffee_list" : coffee_all,
        "coffee_put" : put_form,
        "pk":pk
        })

    else:
        coffee_all = Coffee.objects.all()
        if request.method == 'POST':
            post_form = CoffeeForm(request.POST)
            if post_form.is_valid():
                post_form.save()
            return redirect('/coffees')

        post_form = CoffeeForm()

        return render(request, 'coffee.html', {
            "coffee_list" : coffee_all,
            "coffee_post" : post_form,
            "pk":pk
            })

def burger_view(request):
    burger_all = Burger.objects.all()

    return render(request, 'burger.html', {
        "burger_list" : burger_all,
        })