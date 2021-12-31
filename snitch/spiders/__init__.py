# coding: utf-8
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapy.spiders import Spider
import time
import regex

class neteastSpider (Spider):
    name = "snitch"
    start_urls = ['https://music.163.com/playlist?id=486457701']

    def cookies(self):
        driver=webdriver.Chrome('C:/Users\98115/tutorial-env/snitch/snitch/spiders/chromedriver.exe')

        driver.get("https://music.163.com/")

        #RME:
        driver.maximize_window()
        time.sleep(4)
        actions=ActionChains(driver)


		#RME:
        login=driver.find_element(By.LINK_TEXT, "登录")
        actions.click(login).perform()
        time.sleep(0.3)

        #
        other_way_login=driver.find_element(By.LINK_TEXT,"选择其他登录模式")
        actions.click(other_way_login).perform()
        time.sleep(0.3)

        #
        aggree = driver.find_element(By.ID, "j-official-terms")
        actions.click(aggree).perform()
        time.sleep(0.3)

        #
        login_phone = driver.find_element(By.LINK_TEXT,"手机号登录")
        actions.click(login_phone).perform()
        time.sleep(0.3)
        phone_password = driver.find_element(By.LINK_TEXT,"密码登录")
        actions.click(phone_password).perform()
        time.sleep(0.3)

        # 输入账号密码
        #key=input("please enter ur key ")
        #password=input("please enter ur password ")
        driver.find_element_by_css_selector("#p").send_keys("13873167901")
        driver.find_element_by_css_selector("#pw").send_keys("LZYliziyu519")
        time.sleep(0.3)

        # 点击登录
        login_confirm = driver.find_element(By.LINK_TEXT,"登　录")
        actions.click(login_confirm).perform()
        #actions.move_by_offset(113, 10).click().perform()
        time.sleep(2)


        # 找到头像悬浮
        img = driver.find_element_by_css_selector("div.head:nth-child(1) > img:nth-child(1)")
        actions.move_to_element(img).perform()
        time.sleep(2)

        # 点击我的主页
        my_page = driver.find_element(By.LINK_TEXT,"我的主页")
        actions.click(my_page).perform()
        time.sleep(0.5)

        # 点击喜欢的音乐
        driver.switch_to.frame("contentFrame")
        time.sleep(0.3)
        playlist_fav = driver.find_element(By.XPATH,"//ul[@id='cBox']/li/div/img")
        actions.click(playlist_fav).perform()
        time.sleep(0.3)
        playlist_url=driver.current_url
        print(playlist_url)



        temp = []

        # 遍历driver给的cookies字典
        for i in driver.get_cookies():
            temp.append(i['name'] + "=" + i['value'])

        # 返回字符串cookie
        return ';'.join(temp)

    def start_requests(self):
        # 定义请求头的时候调用一下getCookie获取一下cookie
        headers = {
            'Cookie': self.cookies(),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        # url是个列表这里拿下标[0],然后把headers请求头塞进去,交给parse函数
        yield scrapy.Request(url=self.start_urls[0], headers=headers, callback=self.parse)

    def parse(self, response):
        # 匹配歌曲名的正则表达式
        patt = regex.compile(r'<a href="/song.id=.*?">([^<|{]*?)</a>')
        patt2 = regex.compile(r'<span.title="(.*?)"><a class="" href="(.*?)".hidefocus="true">')

        # 找到所有歌曲名
        listdata = regex.findall(patt, response.text)
        print(response.text)
        print(listdata)

        with open(file="response.txt", mode="w+", encoding="utf-8") as file:
            for item in listdata:
                file.write(item+"\n")

