import imaplib
import email
from email.header import decode_header
import speech_recognition as sr
import pyttsx3

username = email id
password = emaul password
def talk(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(text)
    engine.runAndWait()
def get_info():
    try:
        listener = sr.Recognizer()
        listener.pause_threshold = 0.7
        listener.energy_threshold = 400
        with sr.Microphone() as source:
            print('listening...')
            talk('listening...')
            voice = listener.listen(source, timeout=5)
            info = listener.recognize_google(voice)

            print(info)
            return info
    except:
        talk('please say again')
        d =get_info()
        return d
    ################################
def dell():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    imap.select("INBOX")
    status, messages = imap.search(None, "ALL")
    messages = messages[0].split(b' ')

    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                email_from = msg['from']
                print("from:"+email_from+'\n')
                talk("from:"+email_from+'\n')
                subject = decode_header(msg["Subject"])[0][0]

                if isinstance(subject, bytes):
                    subject = subject.decode()
                print("subject:"+subject+'\n')
                talk("subject:"+subject+'\n')
                talk("can i delete this mail")
                print("Deleting", subject)
                data=get_info()
        if data == (data =="yes" or data =="s"):
            talk(" deleting subject:" + subject + '\n')
            imap.store(mail, "+FLAGS", "\\Deleted")
            print("deleted")
            talk("deleted")
        elif data == "no":
            print(" reading next mail")
            talk(" reading next mail")
        elif data =="stop":
            import login

dell()
