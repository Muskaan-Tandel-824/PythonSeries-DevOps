# In Python, functions are reusable blocks of code that perform specific tasks. They can be built-in (provided by Python), user-defined, lambda (anonymous), or recursive. Functions can also differ based on how they accept and return values.

def check_disk_usage(used_gb , total_gb):
    percentage=(used_gb / total_gb)*100
    if percentage < 70:
        return "ok"
    elif percentage <=90:
        return "Warning"
    else:
        return "Critical"    
result=check_disk_usage(54,100)
print(result)



 
        