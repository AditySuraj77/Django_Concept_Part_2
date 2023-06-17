#from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives
from team.models import Player
from team.models import Team
from contact.models import ContactUs

def index(request):
    """
    subject='Pandas'
    from_='adity0to9@gmail.com'
    msg="Django"                  # Send Mail by using HTML Tag
    to='adity0to9@gmail.com'
    msg=EmailMultiAlternatives(subject,from_,msg,[to])
    msg.content_subtype='html'
    msg.send()

    send_mail(
        'Testing Mail',
        'Django Mail',      # Sending mail
        'adity0to9@gmail.com',
        ['adity0to9@gmail.com'],
        fail_silently= False
    )
    """


    teamdata = Player.objects.all()
    if request.method == 'GET':
        st = request.GET.get('textsearch')
        if st != None: # Active Search Box to searching item on index.html page
            teamdata = Player.objects.filter(name__icontains=st)  # Code for Active Search Box


    data = {
        'teamdata':teamdata
    }
    return render(request,'index.html',data)

def playerdetail(request,slug):
    playerdetails= Player.objects.get(new_slug =slug)  #Using slug
    data = {
        'playerdetails':playerdetails
    }
                                  # Dynamic Data
    return render(request,'playerdetail.html',data)

def allteams(request):
    teamdata = Team.objects.all()
    paginator = Paginator(teamdata,1)
    page_num = request.GET.get('page')  # This code help to make pagination on site
    finalresult = paginator.get_page(page_num)
    totalpage = finalresult.paginator.num_pages
    #print(totalpage)
    data = {
        #'teamdata':teamdata
        'teamdata':finalresult,
        'totalpage':[n for n in range(totalpage)]

    }
    return render(request,'team.html',data)

def contact(request):
    n = ''
    if request.method == 'POST':
        name = request.POST.get('name')   # This code help to get data from html form and store in
        email = request.POST.get('email')  # database
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contaact_model = ContactUs(name=name,email=email,phone=phone,desc=desc)
        contaact_model.save()
        n = 'Form Submit Sucessfully ! '

    return render(request,'contact.html',{'n':n})