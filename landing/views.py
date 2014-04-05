from django.shortcuts import render
from django.http import HttpResponseRedirect
import mailchimp

# Create your views here.
def home(request):
	return render(request, 'index.html', {})

def thanks(request):
	return render(request, 'thanks.html', {})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
    	try:
    		list = mailchimp.utils.get_connection().get_list_by_id('ad3586ef91')
    		email = request.POST['sender']
    		list.subscribe(email, {'EMAIL':email}, double_optin=False)
    	except:
    		pass

        return HttpResponseRedirect('/thanks') # Redirect after POST
    else:
    	return render(request, 'index.html', {})
