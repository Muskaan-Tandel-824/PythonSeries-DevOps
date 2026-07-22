ports=[22,80,443,3306,53,8080]
def is_port_open(port):
    if port in ports:
        return True
    else :
        return False
a=is_port_open(3307)
b=is_port_open(443)
print(a)
print(b)