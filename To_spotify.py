# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver=webdriver.Chrome('C:/Users\98115/tutorial-env/snitch/snitch/spiders/chromedriver.exe')
actions=ActionChains(driver)

def main(key,password):
    open_web(key,password)
    add_songs()

def open_web(key,password):

    driver.get("https://www.spotify.com/us/")
    driver.maximize_window()
    time.sleep(4)

    login=driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/header/div/nav/ul/li[6]/a")
    actions.click(login).perform()
    time.sleep(0.5)

    #key=input("please enter ur Email address or username ")
    #password=input("please enter ur password ")
    key_input=driver.find_element(By.XPATH,"//*[@id='login-username']")
    key_input.send_keys(key)
    #driver.find_element_by_id("account_name_text_field").send_keys(key)
    driver.switch_to.default_content()
    password_input=driver.find_element(By.XPATH,"//*[@id='login-password']")
    password_input.send_keys(password)
    Login_botton=driver.find_element(By.XPATH,"//*[@id='login-button']")
    actions.click(Login_botton).perform()
    time.sleep(5)


    actions.move_by_offset(400,400).click().perform()
    time.sleep(2)
    create_playlist=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/nav/div[1]/div[2]/div/div[1]/button')
    actions.move_to_element(create_playlist).click(create_playlist).perform()
    time.sleep(3)



def add_songs():
    with open('playlist.txt','r',encoding='utf8') as s_list:
        while True:
            song = s_list.readline()
            sesrch_songs=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[3]/section/div/div/input')
            sesrch_songs.clear()
            sesrch_songs.send_keys(song)
            time.sleep(2)
            try:
                add_song=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/button')
                actions.click(add_song).perform()
            except NoSuchElementException:
                print(song+'can not be found')

            if not song:
                break



