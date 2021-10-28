import socket
import struct
import sys
import time
from datetime import datetime


def RequestTimefromNtp_t(addr='0.de.pool.ntp.org'):
  REF_TIME_1970 = 2208988800      # Reference time
  client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
  data = b'\x1b' + 47 * b'\0'
  client.sendto( data, (addr, 123))
  data, address = client.recvfrom( 1024 )
  if data:
    t = struct.unpack( '!12I', data )[10]
    t -= REF_TIME_1970
  return t 


if __name__ == "__main__":
  current_datetime = datetime.now()
  datetime2 = RequestTimefromNtp_t()
  print("system time %s "%(current_datetime))
  print("NTP time %s "%(time.ctime(datetime2)))
  print("time difference %d sec"%(time.time() - datetime2))
 
  print("difference %s hour"%(time.strftime("%H", time.localtime(time.time() - datetime2))))
  print("difference %s minutes"%(time.strftime("%M", time.localtime(time.time() - datetime2))))
  print("difference %s seconds"%(time.strftime("%S", time.localtime(time.time() - datetime2))))  
   
