from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import Customer
from .forms import EmailForm

# Create your views here.

class CustomerView(CreateView):
    model=Customer
    fields=['name', 'email', 'phone']
    template_name='customer_form.html'
    success_url='success'

class CustomerList(ListView):
    model=Customer
    template_name="customer_list.html"

class CustomerDetail(DetailView):
    model=Customer
    template_name="detail.html"

class CustomerUpdate(UpdateView):
    model=Customer
    fields=['name', 'email', 'phone']
    template_name="update.html"
    success_url='/success'

class CustomerDelete(DeleteView):
    model=Customer
    success_url="/list"

def sendemailto(request, customerid):
    if request.method=='POST':
        myemailform=EmailForm(request.POST)
        if myemailform.is_valid():
            subject=myemailform.cleaned_data['subject']
            message=myemailform.cleaned_data['text']
            mailfrom=settings.EMAIL_HOST_USER
            recipient_list=[myemailform.cleaned_data['emailto']]
            send_mail(subject, message, mailfrom, recipient_list)
            return HttpResponseRedirect('/success_mail')
    else:
        person=Customer.objects.get(pk=customerid)
        myemailform=EmailForm(initial={'emailto':person.email})
    return render(request, 'customer_email.html', {'form': myemailform})


