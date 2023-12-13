# import socket
# import sys

# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket successfully created with address family IPV4")
# except socket.error as err:
#     print("Socket creation failed with error message: %s" % (err))
#     sys.exit()

# port = 80

# try:
#     host = socket.gethostbyname('www.google.com')
# except socket.gaierror:
#     print("Error resolving the host")
#     sys.exit()

# s.connect((host, port))
# print("Socket successfully connected to the website")
             
