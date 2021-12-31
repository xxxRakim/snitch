# coding: utf-8
import re
from bs4 import BeautifulSoup
import urllib
import urllib.request,urllib.response,urllib.error
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import regex

def main(url,key,password):
    # url="https://music.163.com/playlist?id=2086570274"
    cookie=cookies(key,password)
    getsong_artist(url,cookie)

def get_web(key,password):
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
    driver.find_element_by_css_selector("#p").send_keys(key)
    driver.find_element_by_css_selector("#pw").send_keys(password)
    time.sleep(0.3)

        # 点击登录
    login_confirm = driver.find_element(By.LINK_TEXT,"登　录")
    actions.click(login_confirm).perform()
    time.sleep(2)


        # 找到头像悬浮
    img = driver.find_element_by_css_selector("div.head:nth-child(1) > img:nth-child(1)")
    actions.move_to_element(img).perform()
    time.sleep(3)

        # 点击我的主页
    my_page = driver.find_element(By.LINK_TEXT,"我的主页")
    actions.click(my_page).perform()
    time.sleep(1)

        # 点击喜欢的音乐
    driver.switch_to.frame("contentFrame")
    time.sleep(1)
    playlist_fav = driver.find_element(By.XPATH,"//ul[@id='cBox']/li/div/img")
    actions.click(playlist_fav).perform()
    time.sleep(0.3)
    playlist_url=driver.current_url

    return playlist_url



def cookies(key,password):
    driver=webdriver.Chrome('C:/Users\98115/tutorial-env/snitch/snitch/spiders/chromedriver.exe')

    driver.get("https://music.163.com/")

    #RME:
    driver.maximize_window()
    time.sleep(4)
    actions=ActionChains(driver)


		#RME:
    login=driver.find_element(By.LINK_TEXT, "登录")
    actions.click(login).perform()
    time.sleep(0.5)

    #
    other_way_login=driver.find_element(By.LINK_TEXT,"选择其他登录模式")
    actions.click(other_way_login).perform()
    time.sleep(0.5)

        #
    aggree = driver.find_element(By.ID, "j-official-terms")
    actions.click(aggree).perform()
    time.sleep(0.5)

        #
    login_phone = driver.find_element(By.LINK_TEXT,"手机号登录")
    actions.click(login_phone).perform()
    time.sleep(0.5)
    phone_password = driver.find_element(By.LINK_TEXT,"密码登录")
    actions.click(phone_password).perform()
    time.sleep(0.5)

        # 输入账号密码
        #key=input("please enter ur key ")
        #password=input("please enter ur password ")
    driver.find_element_by_css_selector("#p").send_keys(key)
    driver.find_element_by_css_selector("#pw").send_keys(password)
    time.sleep(0.3)

        # 点击登录
    login_confirm = driver.find_element(By.LINK_TEXT,"登　录")
    actions.click(login_confirm).perform()
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
    time.sleep(0.5)
    playlist_fav = driver.find_element(By.XPATH,"//ul[@id='cBox']/li/div/img")
    actions.click(playlist_fav).perform()
    time.sleep(0.5)

    #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'g_iframe')))
    # playlist=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody')
    temp = []

    for i in driver.get_cookies():
        temp.append(i['name'] + "=" + i['value'])


    return ';'.join(temp)

def start_requests(url,cookie):

    headers = {
        'Host': 'music.163.com',
        'Referer':'https://music.163.com/',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }

    try:
        response = requests.get(url=url,headers=headers)
        html=response.content.decode(encoding='utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



def getsong_artist(url,cookie):
    song_artist=[]
    html=start_requests(url,cookie)
    soup=BeautifulSoup(html,"lxml")
    result=soup.find('ul',{'class':'f-hide'})
    results=result.find_all('a')
    # print(results)
    f = open("playlist.txt","w",encoding='utf-8')
    for songs in results:
        id=regex.compile(r'<a href=".song.id=(\d*)">')
        song_id=regex.findall(id,str(songs))[0]
        # print(song_id)
        # print(songs.text)
        song_url="https://music.163.com/song?id={}".format(song_id)
        # print(song_url)
        headers = {
        'Host': 'music.163.com',
        'Referer':'https://music.163.com/',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        try:
            response = requests.get(url=song_url, headers=headers)
            html = response.content.decode(encoding='utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        song_soup=BeautifulSoup(html,'lxml')
        title = song_soup.find('title')
        split=regex.compile(r'<title>(.*?) - (.*?) - (.*?) - 网易云音乐</title>')
        titlesplit=regex.findall(split,str(title))[0]
        song_title=str(titlesplit).split(',')
        song_name=song_title[0].strip("('",)
        artist_name=song_title[1].strip(" '").replace('/',' ')
        f.write(song_name+' ')
        f.write(artist_name+'\n')


# if __name__=="__main__":
#     main()

