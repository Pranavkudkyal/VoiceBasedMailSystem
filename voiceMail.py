import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm = "cppproject0@gmail.com"                  # Login credentials of our email id
pwd = "odjjcmuvjzgaglqa"

r = sr.Recognizer()

engine = pyttsx3.init()                                 # Defining an engine for text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

def speak(str):                                         # Function for text to speech
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():                                           # function for speech to text
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)


email_dict = {
    "work": "nandinimudgundi20@gmail.com",
    "friend":"kudkyalpranav@gmail.com",
    "teacher":"ishaamrutam@gmail.com",
    "family":"govardhanboddul8@gmail.com"

}
def sendmail():                                         # Function to send email

    str = "Please speak the key of the recipient of your email"
    speak(str)
    recipient = listen()
    if recipient.lower() in email_dict:
        rec = email_dict[recipient.lower()]
        str = "The email address for " + recipient + " is " + rec
        speak(str)
    else:        str = "Sorry, I could not find an email address for " + recipient
        speak(str)
        return



    str = "Please speak the body of your email"
    speak(str)
    msg = listen()

    str = "You have spoken the message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "The email has been Sent Successfully..!!"
    speak(str)
def readmail():                                         # Function for Reading email from Inbox
    server = e.connect("imap.gmail.com", unm, pwd)
    server.listids()

    str = "Please say the Serial Number of the email you wanna read starting from latest"
    speak(str)

    a = listen()
    if( a == "tu"):
        a = "2"

    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The email is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is:"
    speak(str)
    speak(email.title)
    str = "The body of email is :"
    speak(str)
    speak(email.body)



str = "Welcome to voice controlled email service"
speak(str)

while(1):

    str = "What do you want to do?"
    speak(str)

    str = "Speak SEND to Send email    Speak READ to Read Inbox   Speak EXIT to Exit"
    speak(str)

    ch = listen()

    if (ch == 'send') :
        str = "You have chosen to send an email"
        speak(str)
        sendmail()

    elif ( ch == 'read') :
        str = "You have chosen to read email"
        speak(str)
        readmail()

    elif (ch == 'exit') :
        str = "You have chosen to exit, bye bye"
        speak(str)
        exit(1)
    else:
        str = "Invalid choice, you said:"
        speak(str)
        speak(ch)
