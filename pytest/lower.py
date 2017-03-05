l = ['QWDWQD', 'DWQDQW', '123', 'None']
[x.lower() if isinstance(x,str) else x for x in l]
