import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://localhost:8001/')

t  = proxy.file_reader('/tmp/secret.txt')
print t