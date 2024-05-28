import ipaddress
import pickle
from _socket import gethostbyaddr
from collections import Counter
from random import randint

from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, TCP, ICMP, traceroute, UDP, TracerouteResult
from scapy.layers.l2 import ARP, Ether


def synScan(dstip, dstport=80, timeout=5, iface=conf.iface):
    """
    使用syn包对dstip范围和dstport范围的进程进行扫描

    :param dstip:目标主机（集）
    :param dstport:目标端口（集）
    :param timeout:发送完数据包后等待的最长时间
    :param iface:选择网卡
    :return:返回回应数据包的SndRcvList 和 未响应数据包的PacketList
    """
    return sr(IP(dst=dstip) / TCP(sport=RandShort(), dport=dstport, flags="S"), iface=iface, threaded=True,
              timeout=timeout,
              filter="tcp")


def ackScan(dstip, dstport=80, timeout=5, iface=conf.iface):
    """
    使用ack包对dstip范围和dstport范围的进程进行扫描

    :param dstip:目标主机（集）
    :param dstport:目标端口（集）
    :param timeout:发送完数据包后等待的最长时间
    :param iface:选择网卡
    :return:返回回应数据包的SndRcvList 和 未响应数据包的PacketList
    """
    return sr(IP(dst=dstip) / TCP(sport=RandShort(), dport=dstport, iface=iface, flags="A"), threaded=True,
              timeout=timeout,
              filter="tcp")


def xmasScan(dstip, dstport=666, timeout=5, iface=conf.iface):
    """
    使用xmas包(flag为'FPU'的tcp包)对dstip范围和dstport范围的进程进行扫描

    :param dstip:目标主机（集）
    :param dstport:目标端口（集）
    :param timeout:发送完数据包后等待的最长时间
    :param iface:选择网卡
    :return:返回回应数据包的SndRcvList 和 未响应数据包的PacketList
    """
    return sr(IP(dst=dstip) / TCP(dport=dstport, flags="FPU"), iface=iface, threaded=True, timeout=timeout,
              filter="tcp")


def ipScan(dstip, proto=0, timeout=5, iface=conf.iface):
    """
    使用协议号为proto的ip包对dstip范围和proto协议范围进行扫描

    :param dstip:目标主机（集）
    :param proto:目标协议（集）
    :param timeout:发送完数据包后等待的最长时间
    :param iface:选择网卡
    :return:返回回应数据包的SndRcvList 和 未响应数据包的PacketList
    """
    return sr(IP(dst=dstip, proto=proto) / "SCAPY", retry=2, iface=iface, threaded=True, timeout=timeout, filter="ip")


def arpScanHost(ans):
    """
    扫描局域网的主机，返回ip地址和主机名元组的列表

    :param ans:arpScan返回的SndRcvList
    :return:返回ip地址和主机名元组的列表
    """
    res = []
    tmp = len(ans)
    for (s, r) in ans:
        print(f"还剩{tmp}个地址待解析")
        tmp -= 1
        dip = s["ARP"].pdst
        try:
            res.append(gethostbyaddr(dip))
        except:
            pass
    return res


def icmpPing(dstnet, retry=3, count=4, timeout=3, iface=conf.iface):
    """
    模拟ping

    :param count:发送个数
    :param dstnet:目标主机(集)
    :param timeout:发送完数据包后等待的最长时间
    :param iface:选择网卡
    :return:返回回应数据包的SndRcvList 和 未响应数据包的PacketList
    """
    if isinstance(iface, str):
        iface = IFACES.dev_from_name(iface)
    randseq = randint(30, 50)
    return sr([IP(src=iface.ip, dst=dstnet) / ICMP(id=1, seq=i) / b'abcdefghijklmnopqrstuvwabcdefghi' for i in
               range(randseq, randseq + count)],
              threaded=True, iface=iface, timeout=timeout, filter="icmp", retry=retry)


def icmpScan(dstnet, timeout=3):
    """
    icmp扫描

    :param dstnet:目标主机(集)
    :param timeout:发送完数据包后等待的最长时间
    :return:返回回应数据包的SndRcvList 和 未响应数据包的PacketList
    """
    return sr(IP(dst=dstnet) / ICMP(), timeout=timeout)


def ipScanHost(ans):
    """
    将SndRcvList类型的ans对应的IP地址转换为主机名

    :param ans:SndRcvList类型的对象
    :return:返回ip地址和主机名元组的列表
    """
    res = []
    tmp = len(ans)
    for (s, r) in ans:
        print(f"还剩{tmp}个地址待解析")
        tmp -= 1
        dip = r["IP"].src
        try:
            res.append(gethostbyaddr(dip))
        except:
            pass
    return res


def traceroute_ip(target, k=6, maxttl=32):
    """
    对target进行最大值为maxttl的traceroute，并将traceroute的结果计数和更新的最大ttl返回

    :param target:目标ip
    :param k:k次traceroute
    :param maxttl:初始最大ttl
    :return:返回traceroute的counter和更新后的maxttl
    """
    ret = Counter()
    for i in range(k):
        ans, unans = traceroute(target=target, maxttl=maxttl)
        for s, r in ans:
            if r.src != target:
                t = ipaddress.ip_interface(r.src + "/24").network
                ret[t] += 1
            else:
                if maxttl > s.ttl:
                    maxttl = s.ttl
    return ret, maxttl


def loadLFA(name):
    with open(name, "rb") as f:
        ret = pickle.load(f)
    return ret


class LFA:
    """
    LFA攻击的类，具有发送traceroute包，计算流密度，对链路进行排序以及对目标链路发起攻击的方法
    """

    def __init__(self, name, target, decoy, maxttl=32):
        """
        构造函数

        :param name:当前主机名
        :param target:目标ip列表
        :param decoy:诱饵服务器ip列表
        """
        self.name = name

        # 目标服务器相关属性
        self.target = target
        self.target_counters = {}
        self.target_counter = Counter()
        self.target_maxttls = {}

        # 目标服务器相关属性
        self.decoy = decoy
        self.decoy_counters = {}
        self.decoy_maxttls = {}
        self.links_to_decoy = {}

    def traceroute_target(self, k):
        # 计算每个目标服务器的流密度，并记录每个目标服务器的maxttl
        self.target_counters.clear()
        self.target_maxttls.clear()
        for t in self.target:
            maxttl = 32
            if t in self.target_maxttls:
                maxttl = self.target_maxttls[t]
            counter, maxttl = traceroute_ip(t, k, maxttl)
            self.target_counters[t] = counter
            self.target_maxttls[t] = maxttl

        # 聚合每个目标服务器的流密度
        self.target_counter.clear()
        for _, c in self.target_counters:
            self.target_counter += c

    def traceroute_decoy(self, k):
        # 计算到每个诱饵服务器的稳定链路，并记录链路到诱饵服务器的映射
        self.decoy_counters.clear()
        self.decoy_maxttls.clear()
        for d in self.decoy:
            maxttl = 32
            if d in self.decoy_maxttls:
                maxttl = self.decoy_maxttls[d]
            counter, maxttl = traceroute_ip(d, k, maxttl)
            self.decoy_counters[d] = counter
            self.decoy_maxttls[d] = maxttl

    def store(self):
        with open(self.name + '_target', 'wb') as f:
            pickle.dump(self, f)
