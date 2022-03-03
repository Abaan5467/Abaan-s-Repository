from pywhatkit.whats import sendwhatmsg

number = input("Enter the number with with the calling code: ")
time=input("Enter the time at which you want to send the message in 24 hour format: ")
message=input("Enter the message: ")
x=time.split(':')
hours=int(x[0])
mins=int(x[1])
sendwhatmsg(number,message,hours,mins)
print("Message sent")
