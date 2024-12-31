from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import Role
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return redirect('admin:index') 
                elif user.roles.filter(id=Role.TEACHER).exists() :
                    if   not user.has_reset_password:
                        return redirect('password_reset')
                    else: 
                        login(request, user)
                        return redirect('admin:index') # Replace with your teacher dashboard URL name
                else:
                    messages.error(request, "ليس لديك صلاحية للدخول.")
            else:
                print('#'*100)
                messages.error(request, 'البريد الإلكتروني أو كلمة المرور غير صحيحة.')
        else:
            messages.error(request, 'الرجاء تصحيح الأخطاء في النموذج.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.has_reset_password = True 
        if user.is_teacher:
            user.is_staff=True
        user.save()
        return super().form_valid(form)
