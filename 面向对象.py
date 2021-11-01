# # 分析一个水杯的属性和功能，使用类描述并创建对象
# '''
# 水杯：
#     属性：容量，形状，价格，颜色，类型，生产厂商
#     功能:装水，加热
#
# '''

color = ["红色","白色","蓝色","绿色","紫色","橙色","粉色","黄色","青色"]
cailiao = ["陶瓷","木材","塑料","钢材"]
class Cup():
    __capacity = 0        #水杯的容量
    __hegith = 0          #水杯的高度
    __colour = ""         #水杯的颜色
    __material = ""       #原材料




    def setcapacity(self,capacity):
        if capacity >=0 and capacity <= 3000:
            self.__capacity = capacity
        else:
            print("你是在装河吗？？？")
    def getcapacity(self):
        return self.__capacity

    def sethegith(self,hegith):
        if hegith>=10 and hegith<=20:
            self.__hegith = hegith
        else:
            print("你拿的是杯子吗")
    def gethegith(self):
        return self.__hegith


    def setcolour(self,colour):
        if colour not in color:
            print("现在不使用这些颜色")
        elif colour in color:
            self.__colour = colour
    def getcolour(self):
        return self.__colour


    def setmaterial(self,material):
        if material not in cailiao:
            print("现在不使用这些材料")
        elif material in color:
            self.__material = material
    def getmaterial(self):
        return self.__material





    def contain(self,cap,drink):      #装水功能
        print("我在杯子里装了",cap,"ml的",drink)



c = Cup()
c.setcapacity(1500)
c.sethegith(12)
c.setcolour("红色")
c.setmaterial("陶瓷")

c.contain(120,"牛奶")

'''
笔记本电脑：
    属性：屏幕大小，CPU型号，内存大小，待机时长
    行为：打字，打游戏，看视频

'''
cpu = ["Intel Core i5","Intel Core i6","Intel Core i7","Intel Core i9","Intel Core i11"]
class Computer():
    __screen_size = 0
    __cpu_type = ""
    __ram_size = 0
    __standby_time = 0



    def setScreen_size(self,screen_size):
        if screen_size>=10 and screen_size<=20:
            self.__screen_size = screen_size
        else:
            print("屏幕太大或太小了")
    def getScreen_size(self):
        return self.__screen_size


    def setCpu_type(self,cpu_type):
        if cpu_type in cpu:
            self.__cpu_type = cpu_type
        else:
            print("暂时不支持这种型号的cpu")
    def getCpu_type(self):
        return self.__cpu_type

    def setRam_size(self,ram_size):
        if ram_size < 128:
            print("运存太小，带不动啊T_T")
        else:
            self.__ram_size = ram_size
    def getRam_size(self):
        return self.__ram_size

    def setStandby_time(self,standby_time):
        if standby_time<=0 or standby_time >=30:
            print("......哪有这么坑的待机时间")
        else:
            self.__standby_time = standby_time
    def getStandby_time(self):
        return self.__standby_time


    def typing(self,ram):
        print("打字只需要",ram,"M的内存就行了")
    def paly_game(self,cpu,ram):
        print("打游戏最少需要",ram,"m内存和",cpu,"以上的cpu")
    def watch_videos(self,hours):
        print("我看了",hours,"h的视频")

c = Computer()

c.setScreen_size(15)
c.setStandby_time(0)
c.setRam_size(24)
c.setCpu_type("Intel Core i5")


c.paly_game("Intel Core i5",128)
c.watch_videos(12)

























