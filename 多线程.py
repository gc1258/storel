from threading import Thread
import time
# import datetime
start_time = time.time()

Max_Food = 0            #最大的食物量
Cashier = 0  # 收银台的钱

class Cook(Thread):
    username = ""
    Food_count = 0  # 制作食物计数
    def run(self) -> None:
        global Max_Food,Cashier
        while True:
            if time.time() - start_time < 30:
                if Max_Food == 500:
                    time.sleep(3)
                elif Max_Food>=0 and Max_Food < 500:
                    Max_Food += 1
                    self.Food_count = self.Food_count +1
                    Cashier -= 1.5
            else:
                wages = self.Food_count*1.5  # 厨师工资
                print("厨师", self.username, "制作了", self.Food_count, "个面包,工资为：", wages)
                break


class Customer(Thread):
    username = ""
    holding_money = 3000  # 顾客手中的钱
    customer_food = 0  # 顾客的食物
    def run(self) -> None:
        global Cashier,Max_Food
        while True:
            if time.time() - start_time < 30:
                if self.holding_money >=3:
                    if Max_Food >0:
                        self.holding_money -= 3
                        self.customer_food += 1
                        Max_Food -= 1
                        Cashier += 3
                    else:
                        time.sleep(2)
                else:
                    print(self.username, "抢到了", self.customer_food, "个面包,还剩", self.holding_money, "元")
                    break
            else:
                print(self.username, "抢到了", self.customer_food, "个面包,还剩", self.holding_money, "元")
                break


c1 = Cook()
c2 = Cook()
c3 = Cook()
c1.username = "张一"
c2.username = "张二"
c3.username = "张三"


cu1 = Customer()
cu2 = Customer()
cu3 = Customer()
cu4 = Customer()
cu5 = Customer()
cu6 = Customer()
cu1.username = "李一"
cu2.username = "李二"
cu3.username = "李三"
cu4.username = "李四"
cu5.username = "李五"
cu6.username = "李六"

c1.start()
c2.start()
c3.start()
cu1.start()
cu2.start()
cu3.start()
cu4.start()
cu5.start()
cu6.start()


time.sleep(35)
print("最后的利润",Cashier)





















