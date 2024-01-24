import subprocess
import time

def myip():
    me = open('ipconfig.txt','wb')
    subprocess.run('ipconfig', stdout=me)
    me.close
    me = open('ipconfig.txt','r')
    out = me.read()
    me.close
    pos = out.find("IPv4 Address. . . . . . . . . . . :")
    out = out[pos+35:pos+48]
    return(out)

def determine(start):
    ip = start.replace('.','')
    down = int(ip[7:10]) - 1
    up = 999 - int(ip[7:10])
    prefix = int(ip[0:7])
    return(prefix, down, up)

def find(prefix, down, up):
    results = open("results.txt", 'wb')
    cur = down
    prefix = str(prefix)
    prefix = prefix[0:2] + '.' + prefix[2:4] + '.' + prefix[4:6] + '.'
    #Down
    while( cur > 0):
        subprocess.check_call("ping " + prefix + str(cur) + " -n 1",stdout=results)
        results.flush
        if(result)
        print(prefix + str(cur))

        cur += -1
    #Up
    


if __name__ == "__main__":
    me = myip()
    where = determine(me)
    find(where[0], where[1], where[2])
    
