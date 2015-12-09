import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://localhost:8080/')

t  = proxy.file_reader('/tmp/secret.txt')
print t