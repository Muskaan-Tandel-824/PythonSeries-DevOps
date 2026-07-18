#This is an Script for monitoring the cpu usage

try :
   
 usage = int(input("Enter CPU Usage in (%) : "))
 if usage < 0 or usage > 100:
    print("Invlid CPU Usage : Enter a valid value between 0 to 100")
 elif usage > 80:
    print("🔴 High CPU Alert!")
 elif usage >= 50:
    print("🟡 Moderate CPU Usage.")
 else:
    print("🟢 CPU Usage is Normal.")   
     
except ValueError:
 print("please enter numbers only .")          
