



#
class OldPhone:
    __brand = ""

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand


    def Call(self,number:str):
        print("正在给",number,"打电话")

class NewPhone(OldPhone):
    # def setBrand(self,brand):
    #     self.__brand = brand
    # def getBrand(self):
    #     return self.__brand

    def Call(self,phone_number):

        print("语音拨号中。。。")
        super().Call(phone_number)
    def Phone_show(self):
        print("品牌为：",self.getBrand(),"的手机很好用")


class Test2:
    np = NewPhone()
    # op = OldPhone()
    np.Call("18386752524")
    np.setBrand("华为")
    np.Phone_show()




#厨师

class Check:
    __name = ""
    __age = ""

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def Rice(self):
        print(self.__name,"开始蒸饭了")

class Check_Student(Check):

    def Stir_fry(self):
        print("开始炒菜了")


class Check_Student_student(Check_Student):

    def Rice(self):
        print(self.getName(),"蒸饭")

    def Stir_fry(self):
        print(self.getName(),"炒菜")
        # super().Rice()

    def Show(self):
        print("姓名",self.getName(),"年龄",self.getAge())

class Test1:
    Css = Check_Student_student()
    Css.setName("詹姆斯")
    Css.setAge(35)
    Css.Show()
    Css.Rice()
    Css.Stir_fry()



#人

class Hunmen:
    __name = ""
    __age = 0
    __sex = ""

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name


    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

class Hunmen_work(Hunmen):

    def work(self):
        print("工人",self.getName(),"开始工作")

class Student(Hunmen):

    def study(self):
        print("学生",self.getName(),"开始学习")

    def Sing_song(self):
        print("学生",self.getName(),"练习唱歌")


class Test:
    hw = Hunmen_work()
    hw.setName("张三")
    hw.setAge(25)
    hw.setSex("男")
    hw.work()


    st = Student()
    st.setName("王英")
    st.setAge(15)
    st.setSex("男")
    st.study()
    st.Sing_song()
