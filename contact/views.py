from django.shortcuts import render, redirect
from django.contrib import messages
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

from .forms import ContactForm


def contact(request):
    template = 'contact/home.html'
    if request.method == 'GET':
        return render(request, template, {'form': ContactForm()})

    # POST
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form': ContactForm()})
    form.save()
    # send_mail()
    messages.success(request, '您的留言已送出，我們會盡快回覆您，謝謝')
    return redirect('product:product')


def send_mail(mail=None):
    account = 'tingyunchan@gmail.com'
    password = ''

    smtp_obj = SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()

    if mail:
        content = "<h2>感謝您的訂購</h2><p>您已經成功下單阿輝咖啡烘焙坊訂單</p>"  # 郵件內容
        mailto = mail
    else:
        content = "<h2>會員來信通知</h2>"
        mailto = 'ke1905ro@yahoo.com'

    msg = MIMEText(content, "html", "utf-8")
    msg["Subject"] = "阿輝咖啡烘焙"  # 郵件標題

    try:
        smtp_obj.login(account, password)
        smtp_obj.sendmail(account, mailto, msg.as_string())  # 寄信
        print("郵件已發送！")
    except SMTPAuthenticationError:
        print("無法登入！")
    except SMTPException:
        print("郵件發送產生錯誤！")
    smtp_obj.quit()
