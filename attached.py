import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

email = 'xxxx'
password = 'password'
send_to_emails = ['xxxxx@gmail.com',"yyyyyyy"]
subject = 'static subject'
messageHTML ='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\
<html lang="en">\
<head>\
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\
<meta name="viewport" content="width=device-width, initial-scale=1">\
<meta http-equiv="X-UA-Compatible" content="IE=edge">\
<title>Grids Master Template</title>\
</head>\
<body>\
<div style="width:600px; margin:auto;">\
<div style="font-size:45px; background-color:blue; width:600px; color:white;text-align:center; ">\
we do python\
</div>\
<div>\
<img src="cid:myimage" width="600px" height="200px" >\
</div>\
<div style="font-size:35px; background-color:green; width:600px; color:white;text-align:center;" >\
python is beautiful  and simple\
</div>\
</div>\
</body>\
</html>'

messagePlain = ""
msg = MIMEMultipart('alternative')
msg['From'] = email
msg['Subject'] = subject
# Attach files. 
msg.attach(MIMEText(messagePlain, 'plain'))
msg.attach(MIMEText(messageHTML, 'html'))
filename = "image.jpg "

with open(filename, "rb") as attachment:
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(attachment.read())
  
encoders.encode_base64(part2)
part2.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
msg.attach(part2)
# images inside html-email.
fp = open('image.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<myimage>')
msg.attach(msgImage)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
for send_to_email in send_to_emails:
    msg['To'] = send_to_email
    server.sendmail(email, send_to_email, text)
server.quit()
