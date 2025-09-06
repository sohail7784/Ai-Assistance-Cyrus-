import logging
from livekit.agents import function_tool, RunContext
import webbrowser
from datetime import datetime,timedelta
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
import threading
import speech_recognition as sr




@function_tool
async def search(context: RunContext, query: str) -> str:
    """Search anything on the web"""
    try:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        logging.info(f"Searching result for {query} : {url}")
        return url
    except Exception as e:
        logging.error(f"Error searching for {query}: {e}")
        return f"An error occurred while searching for {query}"
    
@function_tool
async def youtube(context: RunContext, query: str) -> str:
    """play any videos on youtube"""
    try:
        y_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(y_url)
        logging.info(f"playing your video on youtube{query}:{y_url}")
        return f"playing your video in youtube {y_url}"
    except Exception as e:
        logging.error(f"canot search your video in youtube")
        return f"an error occured while searching for {query}"

@function_tool
async def set_timer(context:RunContext,seconds:str) ->str:
    """set the timer """
    def alert():
        logging.info(f"hey bro timer is complete")
    try:
        alert="the time is up "
        sec=int(seconds)
        timer=threading.Timer(sec,alert)
        timer.start()
        logging.info(f"the timer is set {seconds}")
        return f"the timer is set {seconds}"
    except Exception as e:
        logging.error(f"i'm so sorry i can't set the timer plaese{e}")
        return f"sorry i can't set the timer{e}"



@function_tool
async def whatsapp(context:RunContext,message:str,number:str)->str:
    """send a whats app message"""
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        logging.info(f"say the message please!")
        audio=recognizer.listen(source)
        speak=recognizer.recognize_google(audio)
        logging.info(f"the message you said is{speak}")
        return f"{speak}"
    try:
        number='+919052539782'
        whatsapp_url=f"https://web.whatsapp.com/send?phone={number}&text={speak.replace(' ', '%20')}"
        webbrowser.open(whatsapp_url)
        logging.info(f"sending the message to your number{speak}")
        return f"sended the message in to your whats app{speak}"
    except Exception as e:
        logging.info(f"i can't send your message in the whats app")
        return f"sorry i can't send you the message"

@function_tool
async def email(contex:RunContext,
                to_email:str,
                subject:str,
                message:str,
                cc_email:str = None
    ) ->str:
        """
        send an email through Gamil SMTP
        
        Args:
        to_email:Recipient email address
        subject:Email subject line
        message:Email body conntent
        cc_email:optional cc email address

        """
        try:
            smtp_server="smtp.gmail.com"
            smtp_port=587
            gmail_user=os.getenv('sohailmohammed5425@gmail.com')
            gmail_passowrd=os.getenv('kzmf cqze zvea ussh')
            if not gmail_user or not gmail_passowrd:
                logging.error("gmail credentials not found in enviornment variables")
                return "email sending failed:gmail credentials not configured"
            msg=MIMEMultipart()
            msg['From']=gmail_user 
            msg['To']=to_email.input("write the mail")
            logging.info(to_email.input("write the email"))
            msg['Subject']=subject
            recipients=[to_email]
            if cc_email:
                msg['cc']=cc_email
                recipients.append(cc_email)
            msg.attach(MIMEText(message,'plain'))
            
            server=smtplib.SMTP(smtp_server,smtp_port)
            server.starttls()
            server.login(gmail_user,gmail_passowrd)

            text=msg.as_string()
            server.sendmail(gmail_user,recipients,text)
            logging.info(f"email sent succesfully to {to_email}")
            return f"email sent succesfully to {to_email}"
        except smtplib.SMTPAuthenticationError:
            logging.error("gmail authentication failed")
            return f"email sending failed : authentication error please check"
        except smtplib.SMTPException as e:
            logging.error(f"smtp error occured :{e}")
            return f"email sending fail:smtp error -{str(e)}"
        except Exception as e:
            logging.error(f"error sending email:{e}")
            return f"an errror occured sending the email:{e}"
        """     
        mail_id='sohailmohammed5425@gmail.com'
        mail_password='kzmf cqze zvea ussh'
        to_email='sohail.shaa786@gmail.com'

        msg=MIMEMultipart()
        msg['From']=gmail_user
        msg['To']=to_email
        msg['Subject']=subject
        msg.attach(MIMEText(body, "plain"))
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(mail_id,mail_password)
            server.sendmail(mail_id,to_mail,msg.as_string())
            server.quit()
            logging.info(f"the mail is sended successfully!")
            return f"the mail is sended {to_mail,subject,body,process}"
        except Exception as e:
            return f"i cannot send mail i'm sorry"
"""

@function_tool
async def maps(context:RunContext,location:str)->str:

    """show the address and the location"""
    try:
        google_maps=f"https://www.google.com/maps/search/?api=1&query={location.replace(' ', '%20')}"
        webbrowser.open(google_maps)
        logging.info(f"showing you the address{google_maps}")
        return f"here is thedirection from current location you have said{google_maps}"
    except Exception as e:
        logging.info(f"sorry i can't show you the loaction{e}")
        return f"sorry to say i can't tell you the location{e}"
    
@function_tool
async def current_location(context:RunContext,origin:str,destination:str) ->str:
    """show location from the current address"""
    try:
        current_map=f"https://www.google.com/maps/dir/?api=1&origin={origin.replace(' ', '%20')}&destination={destination.replace(' ', '%20')}"
        webbrowser.open(current_map)
        logging.info(f"showing you the address according to your current location{current_map}")
        return f"showing you the address according to your current location"
    except Exception as e:
        logging.info(f"soory i can't get the address{e}")
        return f"i'm so sorry i can't get the address"
@function_tool
async def weather(context:RunContext,location: str="your locatoin") ->str:
    """tell the weather of a place"""
    try:
        if location.lower()=="kurnool":
         kurnool_weather= f"https://www.google.com/search?q=weather+{location.replace(' ', '+')}"
         logging.info(f"the current weather is {kurnool_weather}")
         return f"the current weather is {kurnool_weather}"
        else:
            other_weather=f"https://www.google.com/search?q=weather+{location.replace(' ', '+')}"
            logging.info(f"the current weather is {other_weather}")
            return f"the current weather is {other_weather}"
    except Exception as e:
        logging.error(f"i'm so sorry i can't say the weather")
        return f"i'm so sorry i can't say the current weather"
    
@function_tool
async def todaysdate(context:RunContext) -> str:
    """ say the todays date"""
    try:
        date=datetime.now()
        formatedate=date.strftime("todays date is %A, %d %B %Y")
        logging.info(f"todays date is {formatedate}")
        return formatedate
    except Exception as e:
        logging.error(f"sorry cannot give you the current date roght now")
        return f"Im so sorry sohail"
    
@function_tool
async def current_time(context:RunContext) -> str:
    """say the current time"""
    try:
        timing=datetime.now()
        setting=timing.time().strftime(" its %I clock  %M %ps")
        logging.info(f"the current time is {setting}")
        return f"the current time is {setting}"
    except Exception as e:
        logging.error(f"i'm so sorry to tell the current time")
        return f"i'm sorry to say the current time"
    

@function_tool
async def yesterdaysdate(context:RunContext) -> str:
    """say the yesterdays date"""
    try:
        yesterday=datetime.now()-timedelta(days=1)
        sets_yesterday=yesterday.strftime("yesterday was %A,%d %B %Y")
        logging.info(f"the yesterdays date was{yesterday}")
        return f"yesterdays date was {yesterday}"
    except Exception as e:
        logging.error(f"i'm so sorry to tell the yesterdays date")
        return f"i'm sorry to say the yesterdays date"
    
@function_tool
async def tommorowsdate(context:RunContext) -> str:
    """say the tommoorows date"""
    try:
        tommorow=datetime.now()+timedelta(days=1)
        sets_tommorow=tommorow.strftime("tommorows date will be  %A,%d %B %Y")
        logging.info(f"tommorows date will be  {sets_tommorow}")
        return f"tommorows date will be {sets_tommorow}"
    except Exception as e:
        logging.error(f"i'm so sorry to tell the tommorows date")
        return f"i'm sorry to say the tommorows date"
    
@function_tool
async def present_month(context:RunContext) -> str:
    """say the present month"""
    try:
        month=datetime.now().strftime("%B")
        logging.info(f"the current month is {month}")
        return f"the current month is  {month}"
    except Exception as e:
        logging.error(f"i'm so sorry to tell the current month")
        return f"i'm sorry to say the current month"

@function_tool
async def current_year(context:RunContext) -> str:
    """say the present year"""
    try:
        year=datetime.now().strftime("%Y")
        logging.info(f"the current year is {year}")
        return f"the current year is {year}"
    except Exception as e:
        logging.error(f"i'm so sorry to tell the current year")
        return f"i'm sorry to say the current year"

    







