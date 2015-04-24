#codeing:utf-8
__author__ = 'bingalsky'

import re,urllib2

check_url = 'http://imgad0.3conline.com/ivy/image/20129/18/13479307086930.htm'#HelloWorld!

proxies = open('proxies.txt','r')
proxies_checked = open('proxies_checked.txt','w')
for line in proxies.readlines():
	line = line.strip()
	if len(line)<1:
		continue
	m = re.match(r'^.+\s+([\w.]+)\s*$',line)
	#print m
	if m is None:
		continue
	proxy = m.group(1)
	#print proxy
	request = urllib2.Request(check_url)
	request.set_proxy('%s:8090'%proxy,'http')
	try:
		resault = urllib2.urlopen(request,timeout=10).read()
		if 'HelloWorld!' in resault:
			proxies_checked.write(line)
			proxies_checked.write('\n')
			print proxy,'ok'
	except Exception,e:
		print proxy,'error',e
proxies.close()
proxies_checked.close()