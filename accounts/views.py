from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import View

from .models import Profile

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.views.generic import CreateView


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user=authenticate(request,
                              username=data['username'],
                              password=data['password'])
            print(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi')
                else:
                    return HttpResponse('Sizning profilingiz faol holatda emas')

            else:
                return HttpResponse('Login va parolda xatolik bor!')

    else:
        form=LoginForm()
        context = {
            'form':form
        }
    return render(request, 'registration/login.html', context)



@login_required()
def dashboard_view(request):
    user=request.user
    profil_info=Profile.objects.get(user=user)
    context={
        'user':user,
        'profile':profil_info
    }
    return render(request, 'pages/user_profile.html', context)


def user_register(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # If the form is valid, save the user and redirect to a success page
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {'new_user': new_user}
            return render(request, 'account/register_done.html', context)
    else:
        # If the request method is not POST (e.g., GET), or if the form is not valid,
        # render the registration form for the user to fill out
        user_form = UserRegistrationForm()

    # The context should be defined outside the if-else block to ensure it's available in both cases
        context = {'user_form': user_form}
        return render(request, 'account/register.html', {'user_form':user_form})
#     bu yozganimiz funksiya bilan view yozib ishlatdik, ln tayyor klasslardan ham foydalansak bo'ladi, pastda yozamiz




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'

#
# @login_required
# def edit_user(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile,
#                                        data=request.POST,
#                                        files=request.FILES)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#               return redirect('user_profile')
#
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#
#     return render(request, 'account/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})
#

class EditUserView(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'account/profile_edit.html', {"user_form": user_form, "profile_form":profile_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')
