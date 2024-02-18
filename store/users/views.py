from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from users.models import User


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
    else:
        form = UserLoginForm()
        context = {'form': form}
    return render(request, 'users/login.html', context)

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - регистрация'
        return context

# аналог

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse_lazy('users:login'))
#     else:
#         form = UserRegisterForm()
#     context = {'form': form}
#     return render(request, 'users/register.html', context)

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object])

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

#     аналог
# @login_required()
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return  HttpResponseRedirect(reverse_lazy('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     baskets = Basket.objects.filter(user=request.user)
#
#     context = {
#         'title': 'Store - Профиль',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#
#     }
#     return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))
