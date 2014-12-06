import re
import subprocess
def ping(website):
    try:
        ping = subprocess.Popen(["ping", "-n", "-c 10", "-i 0.1", "-W 0.5", website], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = ping.communicate()
        if out:
            try:
                minimum = int(re.findall(r"Minimum = (\d+)", out)[0])
                maximum = int(re.findall(r"Maximum = (\d+)", out)[0])
                average = int(re.findall(r"Average = (\d+)", out)[0])
                packet = int(re.findall(r"Lost = (\d+)", out)[0])
                if packet > 1:
                    packet = packet * 10
                return (minimum, maximum, average, packet)
            except:
                print "no data for one of minimum,maximum,average,packet"
        else:
            print 'No ping'
    except subprocess.CalledProcessError:
        print "Couldn't get a ping"

if __name__ == "__main__":
    ping("www.baidu.com")
