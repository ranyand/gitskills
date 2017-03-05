print 'process (%s) start...' %s os.getpid()
pid = os.fork()
if pid == 0:
	print 'i am child process (%s) and my parent process is (%s)' % (os.getpid(), os.getppid())
else:
	print 'i (%s) have a child process (%s)' % (os.gepid, pid)
