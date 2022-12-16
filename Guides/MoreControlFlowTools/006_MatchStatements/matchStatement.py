def http_response(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case _:
            return "Something's wrong with the internet"

print(http_response(429))
