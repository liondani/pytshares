#!/usr/bin/python
from btsrpcapi import *
import config
import re

payouttarget = "payouts.charity"
withdrawfee = 0.5 * 1e5;
rpc = btsrpcapi(config.url, config.user, config.passwd)

if __name__ == "__main__":
 print rpc.getstatus()
 print rpc.walletopen("delegate")
 rpc.disableblockproduction("ALL")
 print rpc.unlock(config.unlock)
 r = json.loads(rpc.walletgetaccounts())
 accounts = r["result"]
 for account in accounts :
  if  re.match(".*charity.*", account["name"]) :
   if account["delegate_info"] :
    if account["delegate_info"]["pay_balance"] > withdrawfee:
     payout = float(account["delegate_info"]["pay_balance"]) - withdrawfee
     print "%20s -- %20.5f -- %20.5f" % (account["name"], account["delegate_info"]["pay_balance"]/1.0e5, payout/1.0e5)
     print rpc.withdrawdelegatepay(account["name"],payouttarget,payout/1.0e5) 
 print rpc.lock()
