#!/usr/bin/env python3

import os
import datetime
import reports
import sys
import emails

today = datetime.date.today().strftime('%Y-%m-%d')

def process_text(dir):
    text = ""
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            file_path = os.path.join(dir, file)
            with open(file_path, 'r') as f:
                content = f.readlines()
                data = [x.strip() for x in [content[0], content[1]]]
                text += "name: " + data[0] + "<br/>" + "weight: " + data[1] + "<br/><br/>"
    return text

if __name__=="__main__":
    text = process_text(sys.argv[1])
    title = "Processed Update on {}".format(today)
    reports.generate_report("/tmp/processed.pdf", title, text)
    
    sender = "automation@example.com"
    receiver = "<username>@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    message = emails.generate_email(sender, receiver, subject, body, attachment_path)
    emails.send_email(message)