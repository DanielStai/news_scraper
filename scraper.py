#for getting the http response
import requests

#for parsing the html
from bs4 import BeautifulSoup 

#for sending the email
import smtplib

#for the email body
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#system time and date manipulation
import datetime

now  = datetime.datetime.now()

#email content placeholder
empty_mail = ''


#function to get links from guardian football webpage
def extract_news(url):
    print ("Scraping from: " + url)
    content = ''
    content += '<h1>'+'Top Football News Today'+'</h1>' + '\n' + '\n'
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a', attrs = { 'class' : "u-faux-block-link__overlay js-headline-text",  })
    for i, link in enumerate(links):
        content += str(i+1) +' '+':::' + ' ' + link.text + ' '+ '-'+ ' ' + link['href'] + '<br>' + '\n'
    return content


empty_mail = extract_news('https://www.theguardian.com/football')

#setting up the email and starting the server

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'scrapertesting5041@gmail.com'
TO = 'arcticm2015@gmail.com'
PASS = 'verejykymrtopgnq'

#creating the email

msg = MIMEMultipart()
#creating a dynamic subject line
msg['Subject'] = 'Here is your daily dose of Football news [Automated]' + ' '+ str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(empty_mail, 'html')) #can be plain or html

#starting the server
print('Initializing server...')
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent!')







































