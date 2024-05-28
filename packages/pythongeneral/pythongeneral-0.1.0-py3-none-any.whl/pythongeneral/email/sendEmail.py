import email.message as em
import yaml
import smtplib

class MyMail:
    def __init__(self):
        self.getConfig()
        self.setEmailMessage()
        self.setSMTPServer()
            
    def setEmailMessage(self):
        self.msg = em.EmailMessage()
        self.msg["From"] = self.email
        self.msg["To"] = self.to_email
    
    def setSMTPServer(self):
        self.server = smtplib.SMTP_SSL(self.server,int(self.port))
        self.server.login(self.email,self.password)
        
    def getConfig(self):
        config = yaml.load("../config.toml")
        self.email = config["mailSetting"]["email"]
        self.password = config["mailSetting"]["password"]
        self.to_email = config["mailSetting"]["to_email"]
        self.server = config["mailSetting"]["server"]
        self.port = config["mailSetting"]["port"]
    
    def setMailTitle(self,emailTitle):
        self.msg["Subject"] = emailTitle

    def setMailContent(self,emailContent):
        self.msg.add_alternative(emailContent,subtype='html')
    
    def sendMessage(self):
        self.server.send_message(self.msg)
        self.server.close()