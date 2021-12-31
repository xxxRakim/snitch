# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


def open_web():
    driver=webdriver.Chrome('C:/Users\98115/tutorial-env/snitch/snitch/spiders/chromedriver.exe')

    driver.get("https://music.apple.com/us/listen-now?ign-itscg=10000&ign-itsct=402x")

        #RME:
    driver.maximize_window()
    time.sleep(4)
    actions=ActionChains(driver)


    signin=driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/a")
    actions.click(signin).perform()
    time.sleep(0.5)

    commerce_frame=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/iframe")
    driver.switch_to.frame(commerce_frame)
    #driver.switch_to.frame(0)
    driver.switch_to.default_content()
    div_list=driver.find_elements(By.ID,"aid-auth-widget-iFrame")
    print(div_list)
    #iframe=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/iframe")
    #driver.switch_to.frame(iframe)
    #driver.switch_to.default_content()
    subframe=driver.find_element(By.ID,"aid-auth-widget-iFrame")
    driver.switch_to.frame("aid-auth-widget")
    ##iframe_frame=driver.find_element(By.XPATH,"/html/body/div/div/div/main/div/div/iframe")
    #driver.switch_to.frame(iframe_frame)
    key=input("please enter ur key ")
    password=input("please enter ur password ")
    key_input=driver.find_element(By.XPATH,"/html/body/div[3]/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[1]/div/div/input")
    key_input.send_keys(key)
    #driver.find_element_by_id("account_name_text_field").send_keys(key)
    driver.switch_to.default_content()
    password_input=driver.find_element(By.XPATH,"/html/body/div[3]/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[2]/div/div/input")
    password_input.send_keys([password])
    #driver.find_element_by_css_selector("#pw").send_keys(password)
open_web()
