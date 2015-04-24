#!/usr/bin/python
# encoding: utf-8
# Copyright (c) Wangbin <wangbin@pconline.com.cn>


def main():
	import os,time
	# print os.path.basename(__file__)
	for fn in os.listdir(os.curdir):
		fp = os.path.join(os.curdir,fn)
		if not os.path.isfile(fp):
			continue
		if fn.startswith('.'):
			continue
		if fn == os.path.basename(__file__):
			continue
		ctime = int((time.time()-os.stat(fp).st_ctime)*1.0/(60*60*24))
		if ctime >15:
			os.remove(fp)
			print 'deleted:',fn,ctime

if __name__=="__main__":
	main()