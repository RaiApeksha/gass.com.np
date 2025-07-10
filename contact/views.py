from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .utils.send_graph_email import send_graph_email  # Ensure this is correct

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            subject = f"New Contact Form Submission from {contact.name}"

            # Nicely formatted plain text email body
            body = (
                f"New Contact Form Submission\n\n"
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Phone: {getattr(contact, 'phone', 'N/A')}\n"
                f"Subject: {contact.subject}\n\n"
                f"Message:\n{contact.message}"
            )

            try:
                send_graph_email(
                    subject=subject,
                    body=body,
                    to_email='admin@gass.com.np'
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"An error occurred while sending your message: {e}")
                print(f"Error sending email: {e}")  # Optional: log for debugging

            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
