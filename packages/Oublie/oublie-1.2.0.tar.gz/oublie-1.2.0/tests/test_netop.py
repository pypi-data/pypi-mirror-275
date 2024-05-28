from _socket import gethostbyaddr

import scapy.route
from scapy.layers.l2 import arping

from src.Oublie.netop import *

# ans, unans = None, None

# ans, unans = synScan("172.16.14.0/27")

# ans, unans = icmpScanHost("172.16.14.0/24", timeout=3)
# ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") )

# res = icmpScanHost("172.16.14.0/24", timeout=3)

# ans, unans = xmasScan("172.16.76.91")

# ans, unans = sr(IP(dst="127.0.0.1",proto=80)/"SCAPY",retry=2)

# ans.summary(lambda s,r:(s.summary(),r.summary()))

# ans, unans = ackScan("172.16.76.91",(80,90))

# ans, unans = arpPing("172.16.76.0/24", iface="以太网")

# res = arpScanHost("172.16.76.0/27", "以太网", timeout=10)

# ans, unans = icmpPing("172.16.14.87", timeout=5, iface='以太网', count=1)

# ans, unans = icmpPing("172.16.76.1", 10, iface='以太网')

# ans = udpTraceroute("172.16.14.1", 3, 5)

# ans = tcpSynTraceroute("172.16.14.1", 3, 5)

# res, _ = traceroute("www.baidu.com", maxttl=17, timeout=5)

# res = dnsTraceroute("172.16.14.87", maxttl=5)

# for s, r in res:
#     print(s.ttl)

# res.graph()

# ans.summary()

# for i in res:
#     print(i)

# for s, r in ans:
#     print(s["IP"].ttl, r["IP"].sip)

# ans.summary()
# print("----")
# if unans != None:
#     unans.summary()
#
# print("---")
# print(ans.res[0])

# if ans:
#     print(ans.summary)
# else:
#     print("没有响应")

# print(conf.route.route("172.16.14.1"))
# ifa = IFACES.dev_from_name('以太网')
# print(ifa.name, ifa.index, ifa.network_name, ifa.description)


# arpingans.summary(lambda s, r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
# ans, unans = arping("172.16.76.0/27")
# k = arpScanHost(ans)
# print(k)

lfa = LFA("H1", "172.16.14.87", "")

lfa.traceroute_target()

scapy.route.Route
