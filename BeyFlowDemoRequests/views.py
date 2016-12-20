from django.views.generic.edit import CreateView
from forms import RequestDemoForm
from django.core.mail import send_mail


class RequestDemoView(CreateView):
    template_name = "requestDemo.html"
    form_class = RequestDemoForm
    success_url = '/'

    def form_valid(self, form):
        adminMessage = "firstName : " + self.request.POST["firstName"] \
                    + ", lastName : " + self.request.POST["firstName"]  \
                    + ", email : " + self.request.POST["email"] \
                    + ", jobTitle : " + self.request.POST["jobTitle"] \
                    + ", workPhoneNumber : " + self.request.POST["workPhoneNumber"]\
                    + ", company : " + self.request.POST["company"] \
                    + ", message : " + self.request.POST["message"] \
                    + ", canReceiveMails : "  
        if 'canReceiveMails' not in self.request.POST :
            adminMessage = adminMessage + "No"
        else :
            adminMessage = adminMessage + "Yes"


        try:
        	send_mail('New demo request',adminMessage,
        		'info@beyflow.com',['info@beyflow.com'],fail_silently=False)

        	send_mail('Bey Flow: Our team has received your message.',"Thank you. You will hearing from us soon.",
        		'info@beyflow.com',[self.request.POST["email"]],fail_silently=False)

        except Exception, e:
            print(e)
        return super(RequestDemoView, self).form_valid(form)

