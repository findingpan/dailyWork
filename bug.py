import sys, httplib, time, sgmllib

class SpeedHTML(sgmllib.SGMLParser):
     
    def __init__(self, verbose=0):
        sgmllib.SGMLParser.__init__(self, verbose)
        self.status = 0
        self.td = 1
        self.in_tag = 0
        self.ipAddr = []
        self.ipData = []
    # 输入分析的数据 s
    def parse(self, s):
        self.feed(s)
        self.close()
#============== 处理 p 标签以获得 IP 地址
    def start_p(self, attributes):
        for name, value in attributes:
           if name == "align" and value == "left":
                self.status = 1
                self.in_tag = 1
    def end_p(self):
        self.status = 0
#============== tag_p
        
        
#============== 处理 td 标签以获得流量的字节数
    def start_td(self, attributes):
        for name, value in attributes:
            if name == "width" and value == "85":
                # 因为有两个 td 标签是 width = 85 的, 所以这里特殊处理一下
                self.td = self.td + 1
                self.status = 2
                self.in_tag = 1
                
    def end_p(self):
        self.status = 0
#============== tag_td
    def handle_data(self, data):
        if self.status == 1 and self.in_tag == 1 :
            self.ipAddr.append(data)
            self.in_tag = 0
                
        if self.status == 2 and self.in_tag == 1 and self.td % 2 == 0:
            self.ipData.append(int(data))
            self.in_tag = 0
    def get_ipAddr(self):
        return self.ipAddr
    def get_ipData(self):
        return self.ipData
print "test starting..."
headers = {
"Accept": "*/*",
"Referer": "http://192.168.36.1/",
"Accept-Language": "zh-cn",
"Accept-Encoding": "gzip, deflate",
"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
"Host": "192.168.36.1",
"Connection": "Keep-Alive",
"Authorization": "Basic YWRtaW46MjQ1MjQ2"
# 因为登录路由器网页需要密码, 所以有 Authorization 这一项
# 使用这个项目就不用 urllib2 里面的那个 HTTPBasicAuthHandler 类了
# 这些数据由网络抓包来的数据中来的
}
while 1:
    ipAddr = []
    ipData = []
    result = []
    # 每隔 2 秒获取一次数据, 共获取两次
    for i in range(0, 2):
        con1 = httplib.HTTPConnection("192.168.36.1")
        con1.request("GET", "/userRpm/SystemStatisticRpm.htm", "", headers)
        r1 = con1.getresponse()
        
        if r1.status == 200:
            r1.read(3796)# 前面有一部分数据完全没有用, 所以预读一下忽略掉它
            d = r1.read()# 开始有用的数据
            
            sg = SpeedHTML()
            sg.feed(d)
            
            ipAddr = sg.get_ipAddr()
            ipData.append(sg.get_ipData())
            
        con1.close()
        time.sleep(2)
        
    for i in range(0, len(ipAddr)):
        # 计算刚才获取数据那段时间的流量,单位: kb/s
        result.append((ipData[1][i] - ipData[0][i]) / 4 / 1000)
        print "IP: ", ipAddr[i], " is ", result[i], " kb/s"
    print "=============================="