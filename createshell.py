import readline,code

def readfilter(*args,**kwargs):
    inline = input(*args,**kwargs)
    if any(map(lambda x:x in inline,blist)):
        print("Not Allowed")
        return ""
    return inline

print("CTRL-D to move to next trick")
blist = ['import','eval','compile']
code.interact(banner='shell 1', readfunc=readfilter)

print("CTRL-D to move to next trick")
blist = ['import','exec','compile']
code.interact(banner='shell 2', readfunc=readfilter)

print("CTRL-D to move to next trick")
blist = ['import','exec','eval']
code.interact(banner='shell 3', readfunc=readfilter)

print("CTRL-D to move to next trick")
blist = ['import','exec','eval','compile']
code.interact(banner='shell 4', readfunc=readfilter)
