from django.contrib import messages
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from django.contrib.auth.decorators import login_required
from .models import Condition,feedback,Laptop,Reservation,Studentprofile,Transaction,User,History
# Create your views here
def registration(request):
    if request.method=='POST':
        try:
            user=User.objects.create(username=request.POST.get('username'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'))
            user.set_password(request.POST.get('Password'))
            user.save()
            
            

        except:
                print("enter Valid data again")
    return render(request, 'registration.html')



class customLOgin(LoginView):
     model=Studentprofile
     template_name='login.html'
     success_url=reverse_lazy('register')
     def form_valid(self, form):
        
        super().form_valid(form)

      
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return redirect('allocated_laptops')
        else:
            return redirect('userpage')

def alocateLaptop(request):
     if request.method=='POST':
          try:
            laptop=Transaction.objects.create(student=request.POST.get('student'),laptop=request.POST.get('laptop'),check_out_time=request.POST.get('check_out_time'),check_in_time=request.POST.get('check_in_time'))
            laptop.save()
          except:
            print("enter Valid data again")
     return render(request, 'admin.html')
     
class listview(ListView):
    model=Transaction
    context_object_name = "transaction"
    success_url=reverse_lazy('allocated_laptops')
    template_name='allocated_laptops.html'

class Delete(DeleteView):
    model=Transaction
    context_object_name = "delete"
    success_url=reverse_lazy('allocated_laptops')
    template_name='deletelaptop.html'
    

class Update(UpdateView):
    model=Transaction
    fields='__all__'
    context_object_name = "update"
    success_url=reverse_lazy('allocated_laptops')
    template_name='admin.html'
    

class TransactionCreate(CreateView):
    model=Transaction
    fields='__all__'
    context_object_name = "create"
    success_url=reverse_lazy('allocated_laptops')
    template_name='admin.html'


def get_history(request):
    if request.method=='GET':
        queryset = History.objects.all().order_by('-time')
    return render(request, 'history_list.html', {'history_list': queryset})

@login_required
def user_history(request):
    user = request.user
    history = History.objects.filter(student=user)
    return render(request, 'user.html', {'history': history})


class ReservationCreateView(CreateView):
    model = Reservation
    fields=['laptop','fromtime','totime']
    template_name = 'reservation.html'
    success_url = reverse_lazy('listreser')  

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
    
class ListReservations(ListView):
    model = Reservation
    template_name = 'viewreservation.html'
    success_url = reverse_lazy('userpage')  

    def get_queryset(self):
        
        return Reservation.objects.filter(student=self.request.user)
    
class DeleteReservation(DeleteView):
    model=Reservation
    context_object_name = "delete"
    success_url=reverse_lazy('listreser')
    
class listreserve(ListView):
    model=Reservation
    template_name="listreserve.html"
    success_url=reverse_lazy("allocated_laptops")

class Deleteone(DeleteView):
    model=Reservation
    context_object_name = "delete"
    success_url=reverse_lazy('adminreservation')



def post_feedback(request):
    if request.method == 'POST':
        try:
            feedback_instance = feedback.objects.create(
                laptop=request.POST.get('laptop'),
                Date=request.POST.get('Date'),
                feedback=request.POST.get('feedback'),
                student=request.user  
            )
            feedback_instance.save()
            return redirect('user')  

        except Exception as e:
            print("Error:", str(e))
            

    return render(request, 'postfeedback.html')

