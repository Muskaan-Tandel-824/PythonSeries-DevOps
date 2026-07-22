
status_map = {200:"Success",404:"Not Found",500:"Server Error"}
def get_http_status_message(code):
    return status_map.get(code, "Unknown status")
result = get_http_status_message(400)  
print(result)  






# option2

# messages={200:"Success",404:"Not Found",500:"Server Error"}
# def get_http_status_message(code):
#     for i, j in messages.items():
#         if code==i:
#             return j

# result=get_http_status_message(404)
# print(result)        
