from django.shortcuts import render
from django.contrib import messages

from pizza.forms import MultiplePizzaForm, PizzaForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id

            size = filled_form.cleaned_data.get('size')
            topping1 = filled_form.cleaned_data.get('topping1')
            topping2 = filled_form.cleaned_data.get('topping2')

            messages.success(request, f'Thanks for ordering! Your {size}, {topping1} and {topping2} pizza is on its way!')

            filled_form = PizzaForm()
        else:
            created_pizza_pk=None
            messages.warning(request,'Pizza order failed,try again')
            
        return render(request,'pizza/order.html',{'created_pizza_pk':created_pizza_pk,'pizzaform':filled_form,"multiple_form":multiple_form})
    
    
    else:
        form= PizzaForm()
        return render(request,'pizza/order.html',{'pizzaform':form,"multiple_form":multiple_form})