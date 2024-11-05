
def http_status(status):

    match status:

        case 200:
            return "OK"
        case 401:
            return "Unauthorised"
        case 500:
            return "Internal Server Error"
        case _: # default case
            return "Unknown status"

print(http_status(200))
print(http_status(400))
print(http_status(401))
print(http_status(500))
print(http_status(700))