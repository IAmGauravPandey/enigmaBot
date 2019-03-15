from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib import admin,auth
from django.shortcuts import redirect
from .forms import MessageForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth import login,authenticate
from .models import Messages
import zulip

def home(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            print(msg)
            mssg="@**Enigma** "+str(msg)
            print(msg)
            client = zulip.Client(config_file="~/zuliprc")
            rq={
                "type":"private",
                "to":"Enigma-bot@hackfest19.zulipchat.com",
                "content":mssg
            }
            result = client.send_message(rq)
            print(result)
            msg.save()
            return redirect('/')

    else:
        form=MessageForm()
        msgs=Messages.objects.all().order_by('-date')
        args={'form':form,'msgs':msgs}
        return render(request,'enigma/base.html',args)