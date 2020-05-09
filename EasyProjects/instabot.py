from time import sleep
from selenium import webdriver
chromedriver = "C:\\Users\\DELL\\Desktop\\chromedriver"



class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(chromedriver)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(3)
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        login_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht , ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_element_by_tag_name('a')
        print(name.text for name in links if name.text != '')



#
# my_bot = InstaBot(username, password)
# my_bot.get_unfollowers()
