#This script usefull for monitor disk 
try:

 space = int(input("Enter disk space in GB's : "))
 if space < 0 :
  print("Invalid Value !!!")
 elif space < 10:
  print("Critical: Free up disk space immediately.") 
 elif space > 10 and space < 50:
  print("Warning: Monitor disk usage.") 
 else:
  print("Healthy: Sufficient disk space available.")

except ValueError:
 print("Enter a Valid input")