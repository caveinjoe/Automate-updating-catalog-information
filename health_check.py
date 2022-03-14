#!/usr/bin/env python3

import psutil
import shutil
import emails
import socket

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_disk_space():
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    return free > 20

def check_memory():
  free = psutil.virtual_memory().available
  free_mb = free / 1024 ** 2 #convert to MB
  return free_mb > 500

def check_host():
    localhost_ip = socket.gethostbyname('localhost')
    return localhost_ip == "127.0.0.1"

def send_error_email(type):
    sender = "automation@example.com"
    receiver = "<username>@example.com"
    subject = type
    body = "Please check your system and resolve the issue as soon as possible."
    emails.generate_email(sender, receiver, subject, body)
    
def error_type():
    if not check_cpu_usage():
        type = "Error - CPU usage is over 80%"
        send_error_email(type)

    if not check_disk_space():
        type = "Error - Available disk space is less than 20%"
        send_error_email(type)

    if not check_memory():
        type = "Error - Available memory is less than 500MB"
        send_error_email(type)

    if not check_host():
        type = "Error - localhost cannot be resolved to 127.0.0.1"
        send_error_email(type)
        
error_type()