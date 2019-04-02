import time
from datetime import datetime as dt     # creating namespace of "dt"

hosts_path="/private/etc/hosts"
hosts_temp = "hosts"
redirect="127.0.0.1"
website_list=["gmail.com","www.cnn.com","cnn.com"]

while True:

    # Create a datetime object "dt" of the year, month, day and hours and compare with dt.now()
    # So, for example, if (2018, 04, 01, 8) < (2018, 04, 01, 13) < (2018, 04, 01, 16) then print "working hours"
    # Where, 8 is 8 am, and 16 is 4 pm
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")

        # open the file for read and append
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    # we will pass, because the website is already in the file
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        # We are outside working hours. Now we want to delete the websites to allow access
        print("Fun hours...")
        with open(hosts_path,'r+') as file:
            # read all of the file into content. When doing this, the pointer will be at the
            # last character of the file.
            content=file.readlines()

            # this takes us back to the first position in the file. We're doing this
            # because we want to insert the new file write (done below) so we can
            # truncate the rest of the text.
            file.seek(0)

            # for each line in the content, starting with line 1
            for line in content:
                # If there a no websites in the line (which are in the website_list), then
                # write the line. This writes a line of the file, but doesn't write the
                # website to the file.
                if not any(website in line for website in website_list):
                    file.write(line)
            
            file.truncate()

     # Delay 5 seconds
    time.sleep(5)
