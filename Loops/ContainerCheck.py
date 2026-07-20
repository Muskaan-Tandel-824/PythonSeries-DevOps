container=("web","database","dev","backend","frontend")
for i in container:
    if i=="web" or i =="database":
     print(f"Container {i} is Running Smoothly")
    else:
       print(f"Container {i} is Stopped !!") 