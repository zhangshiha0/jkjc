#需要用到谷歌浏览器，以及浏览器相应的版本驱动
#将驱动放到python安装目录下的srict目录下，并且复制一份到谷歌浏览器的安装目录下
#亦可以使用火狐浏览器，但也要下载相应版本的驱动，如上
#学号 密码 温度为必填项目
#如果爬脚本在服务器上没有执行可以设置一个邮箱提醒
import time
from selenium import webdriver

uname = 'Z18035536'  #####设置学号
passwd = '123456'    #####设置密码
Temperature = '36.8' #####设置温度（可以写一个列表，利用随机数索引传入保证每天的温度不一样，避免辅导员约茶）

def jitb(uname,passwd,Temperature):
    start_url = 'http://hmgr.sec.lit.edu.cn/web/#/login'
    brower = webdriver.Chrome("d:/guge/chromedriver.exe")  #调用谷歌浏览器（可以使用火狐，调用驱动的绝对路径）
    brower.get(start_url)
    login_input = brower.find_element_by_xpath("//input[@placeholder='请输入密码']") #利用xpath获取选中框，键入，密码
    login_input.click()
    login_input.send_keys(passwd)
    time.sleep(2)
    login_input = brower.find_element_by_xpath("//input[@placeholder='请输入账号']")#利用xpath选中用户框
    login_input.click()
    login_input.send_keys(uname)

    login_click = brower.find_element_by_xpath("//button[contains(@class,'van-button van-button--default')]") #登录
    login_click.click()
    time.sleep(2)
    login_click = brower.find_element_by_xpath("//p[text()='单位个人每日健康状况一键上报，快速收集']") #进入页面
    login_click.click()
    time.sleep(2)
    try:
        login_click = brower.find_element_by_xpath("//button[contains(@class,'bottom_btn van-button')]") #于昨日无差别 点击完成
        login_click.click()
        time.sleep(2)
        login_click = brower.find_element_by_xpath("//input[@placeholder='腋下温度(小数或整数)']") #输入度数
        login_click.send_keys(Temperature)
        time.sleep(2)
        login_click = brower.find_element_by_xpath("//button[contains(@class,'ensure_button van-button')]") #输入度数
        login_click.click()
        print('今日份健康填报已经完成')
        time.sleep(2)
    except:
        print('已经填报过了，请明天再来')
    brower.quit()
jitb(uname,passwd,Temperature)
