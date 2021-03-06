#!/usr/bin/python
import csv
import os
from btsrpcapi import *
import config

def updatemissedblocks() :
 rpc = btsrpcapi(config.url, config.user, config.passwd)
 f = open(os.getenv("HOME") + '/pytshares/missedblocksnew.csv', 'wb')
 w = csv.writer(f, delimiter=':')
 with open(os.getenv("HOME") + '/pytshares/missedblocks.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=':')
  for row in spamreader:
   name      = row[0]
   a         = json.loads(rpc.getaccount(name))
   newmissed = int(a["result"]["delegate_info"]["blocks_missed"])
   w.writerow([name, newmissed])
 f.close()
 os.rename(os.getenv("HOME") + '/pytshares/missedblocksnew.csv', os.getenv("HOME") + '/pytshares/missedblocks.csv')

if __name__ == "__main__":
 updatemissedblocks()
