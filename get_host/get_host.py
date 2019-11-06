from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from subprocess import call
import sys

if __name__ == "__main__":
    hostlist = open('hostlist', 'r')
    hosts = hostlist.readlines()
    call(["mkdir", "output"])
    for host in hosts:
        call(["killall", "firefox"])
        bmcfw = ''
        sdr = ''
        mefw = ''
        address = host.split(';')[0]
        login = host.split(';')[1][:-1]
        call(["mkdir", "output/" + address])
        print 'Processing ' + address
        options = Options()
        options.headless = True
        options.accept_untrusted_certs = True
        driver = Firefox(executable_path='geckodriver', options=options)
        wait = WebDriverWait(driver, timeout=10)
        driver.get("http://" + address)
        check = driver.find_elements_by_xpath('//*[@id]')
        checklist = []
        for element in check:
            checklist.append(element.get_attribute('id'))
        if 'LOGIN_VALUE_1' in checklist:
            driver.get("http://" + address + "/page/login.html")
            driver.find_element_by_id("login_username").click()
            driver.find_element_by_id("login_username").clear()
            driver.find_element_by_id("login_username").send_keys(login)
            driver.find_element_by_id("login_password").clear()
            driver.find_element_by_id("login_password").send_keys("operator")
            driver.find_element_by_id("LOGIN_VALUE_1").click()
            #driver.switch_to_default_content()
            #list = driver.find_elements_by_xpath("//*[@id]")
            #for x in list:
            #    print x.get_attribute("id")
            sleep(10)
            driver.switch_to.frame('MAINFRAME')
            bmcfw = driver.find_element_by_xpath("//*[@id=\'_bmcFwRev\']")
            sdr = driver.find_element_by_xpath("//*[@id=\'_sdrVersion\']")
            mefw = driver.find_element_by_xpath("//*[@id=\'_MEVersion\']")
            mefwp = driver.find_element_by_xpath("//*[@id=\'_MEbldPatch\']")
            bmcfw = bmcfw.text
            sdr = sdr.text
            mefw = mefw.text + mefwp.text
        elif 'loginbtn' in checklist:
            driver.get("http://" + address + "/cgi/url_redirect.cgi?url_name=mainmenu")
            driver.find_element_by_xpath('//input[@name=\'name\']').click()
            driver.find_element_by_xpath('//input[@name=\'name\']').clear()
            driver.find_element_by_xpath('//input[@name=\'name\']').send_keys(login)
            driver.find_element_by_xpath('//input[@name=\'pwd\']').click()
            driver.find_element_by_xpath('//input[@name=\'pwd\']').clear()
            driver.find_element_by_xpath('//input[@name=\'pwd\']').send_keys("operator")
            driver.find_element_by_xpath('//input[@name=\'login_button\']').click()
            sleep(20)
            driver.switch_to.frame('TOPMENU')
            driver.switch_to.frame('frame_main')
            bmcfw = driver.find_element_by_xpath("//*[@id=\'fw_rev\']")
            sdr = driver.find_element_by_xpath("//*[@id=\'sdr_rev\']")
            mefw = driver.find_element_by_xpath("//*[@id=\'me_rev\']")
            bmcfw = bmcfw.text
            sdr = sdr.text
            mefw = mefw.text
        call 
        output = open('output/' + address + '/' + address + '_bmc.txt', 'w')
        output.write('bmcfw:' + bmcfw + '\nsdr:' + sdr + '\nmefw:' + mefw + '\n')
        output.close()
    hostlist.close()
