from django.shortcuts import render
from apps.message.models import UserMessage
import random
import os
'''
获取留言表单，填入留言信息并存储到数据库中
'''
def submitform(request):
    return render(request,'message_form.html')
'''
显示留言板信息
'''
def showform(request):
    # 上传到数据库
    if request.method == 'POST':
        usermessage = UserMessage()
        usermessage.name = request.POST.get('name','')
        usermessage.email = request.POST.get('email','')
        usermessage.address = request.POST.get('address','')
        usermessage.message = request.POST.get('message','')
        usermessage.object_id = str(random.randint(0,10000)).zfill(5) # 自动补零
        usermessage.save()
    # 取出当前数据库中所有记录，并传入到下一个html中
    all_messages = UserMessage.objects.all()
    return render(request,'message_board.html', {
        'all_messages':all_messages,
    })

def hello(request):
    print(os.getcwd())
    return render(request,'index.html')

def hi(request):
    print("page")
    return render(request,'page.html')

def home_view(request):
    print("home")
    #post_list = Thing.objects.all()  #获取全部的Article对象
    #return render(request, 'index.html', {'post_list' : post_list})
    return render(request,'index.html')