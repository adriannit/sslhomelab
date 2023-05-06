class Dnsmasq(object):
    def __init__(self, dnsmasq_conf="./dnsmasq.conf") -> None:
        self.dnsmasq_conf = dnsmasq_conf
        self.list = self.__read_conf()
        pass

    def __read_conf(self):
        origin = []
        for i in open(self.dnsmasq_conf, "r"):
            origin.append(i.rstrip())
        return origin

    def print_dnsA(self):
        Alist = []
        for i in self.list:
            li = list(i.split("="))
            if li[0] == "address":
                out = list(li[1][1:].split("/"))
                Alist.append(out)
        print(Alist)

    def print_dnsCNAME(self):
        CNAMElist = []
        for i in self.list:
            li = list(i.split("="))
            if li[0] == "cname":
                out = list(li[1][1:].split(","))
                CNAMElist.append(out)
        print(CNAMElist)


dns = Dnsmasq("./dnsmasq.conf")
dns.print_dnsA()
print("=====")
dns.print_dnsCNAME()
