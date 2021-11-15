from selenium import webdriver
from selenium.webdriver.common.by import By
import time

##京东
# chromrdriver = webdriver.Chrome()
#
# chromrdriver.get("https://www.jd.com/")
#
# # chromrdriver.maximize_window()
#
# chromrdriver.find_element(By.ID,"key").send_keys("保暖袜")
#
# chromrdriver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button").click()
#
# time.sleep(5)
#
# chromrdriver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]/div/div[4]/a").click()
#
#
# # 在浏览器中切换网页时，有时代码会无法找到元素路径，这是因为网页没有切换，执行代码任停留在上一个网页的代码中
# handles = chromrdriver.window_handles
#
# for handle in handles:
#     if handle != chromrdriver.current_window_handle:
#         chromrdriver.switch_to.window(handle)
#
# time.sleep(2)
# chromrdriver.find_element(By.ID,"InitCartUrl").click()
#
# time.sleep(10)
# chromrdriver.quit()







# #苏宁
# chromrdriver = webdriver.Chrome()
#
# chromrdriver.get("https://www.suning.com/")
#
# # chromrdriver.maximize_window()
#
# chromrdriver.find_element(By.ID,"searchKeywords").send_keys("保暖袜")
#
# chromrdriver.find_element(By.ID,"searchSubmit").click()
#
# time.sleep(5)
#
# chromrdriver.find_element(By.ID,"ssdsn_search_pro_baoguang-1-1-1_1_01:0070091089_11799436234-gg").click()
#
#
# # 在浏览器中切换网页时，有时代码会无法找到元素路径，这是因为网页没有切换，执行代码还停留在上一个网页的代码中
# handles = chromrdriver.window_handles
#
# for handle in handles:
#     if handle != chromrdriver.current_window_handle:
#         chromrdriver.switch_to.window(handle)
#
# time.sleep(2)
# chromrdriver.find_element(By.ID,"addCart").click()
#
# time.sleep(10)
# chromrdriver.quit()




#B站
chromrdriver = webdriver.Chrome()

chromrdriver.get("https://www.bilibili.com/")

chromrdriver.maximize_window()
time.sleep(1)
chromrdriver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/input").send_keys("金光布袋戏")

chromrdriver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button").click()

chromrdriver.switch_to.window(chromrdriver.window_handles[1])

time.sleep(2)
chromrdriver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul[1]/li[1]/div/div/div[3]/ul/li[1]/a/div").click()
time.sleep(2)
chromrdriver.switch_to.window(chromrdriver.window_handles[2])
time.sleep(2)
chromrdriver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[4]/div[1]/div[1]/i").click()



time.sleep(10)
chromrdriver.quit()




































