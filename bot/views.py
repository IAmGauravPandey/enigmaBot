from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib import admin,auth
from django.shortcuts import redirect
from .forms import MessageForm,QueryForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth import login,authenticate
from .models import Messages,Query
import pathlib
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
            client.send_message(rq)
            for i in range(1000000):
                x=1
            f = pathlib.Path("/home/gauravpandey/Desktop/hackfest/bot/messages.txt").read_text()
            print(f)
            form=MessageForm()
            querys=QueryForm()
            args={'form':form,'querys':querys,'response':f}
            return render(request,'enigma/base.html',args)

    else:
        form=MessageForm()
        querys=QueryForm()
        args={'form':form,'querys':querys}
        return render(request,'enigma/base.html',args)
