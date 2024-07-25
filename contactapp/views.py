from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    form_contacto = ContactForm()
    
    if request.method == 'POST':
        form_contacto = ContactForm(data=request.POST)
        if form_contacto.is_valid():
            nombre = request.POST.get('nombre')
            asunto = request.POST.get('asunto')
            email = request.POST.get('mail')
            mensaje = request.POST.get('mensaje')
            
            correo = EmailMessage(
                asunto,
                'Mesaje: {} De: {}'.format(mensaje,nombre),
                "",
                ["giannix13@gmail.com"],
                reply_to=[email],
            )
            
            try:
                correo.send()
            
                return redirect('/contact/?valido')
            except:
                return redirect('/contact/?novalido')
    
    return render(request, 'contact.html', {'form':form_contacto})