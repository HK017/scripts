from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class automatic_comment(object):

    def __init__(self):
        self.url = 'http://www.dianping.com/'
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

    def login_dianPing_and_comment(self, account, password):
        '''
        大众点评模拟登陆,随机睡眠
        :param phone: 账号
        :param password: 账号密码
        :return: 登陆的cookie
        '''
        self.driver.get(self.url)
        self.driver.maximize_window()
        # login

        # 点击头部的你好，请登陆
        top_hello_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="top-nav"]/div/div[2]/span[2]/a[1]'))
        )
        top_hello_login.click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="J_login_container"]/div/iframe'))  # 切入
        # 切入网页框架(在网页中嵌套网页所以必须切入到嵌套的网页中才能找到相应的元素)
        # 其中浮动框架(iframe)是镶嵌在一个网页中的另一个网页。相当网页中又嵌套了一个窗口
        # frame相当于独立的网页，如果在父类网frame查找子类的，则必须切换到子类的frame，子类如果查找父类也需要先切换
        # print(driver.page_source)
        sleep(2)
        # 点击账号登录
        account_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[5]/span'))
        )
        account_login.click()
        # 点击手机密码登录 (如果没这一步会报错)
        mobile_password_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-account"]'))
        )
        sleep(random.uniform(1, 3))
        mobile_password_login.click()
        # 输入手机号
        sleep(random.uniform(1, 3))
        self.driver.find_element_by_xpath(r'//*[@id="account-textbox"]').send_keys(account[:3])
        sleep(random.uniform(0, 2))
        self.driver.find_element_by_xpath(r'//*[@id="account-textbox"]').send_keys(account[3:7])
        sleep(random.uniform(0, 2))
        self.driver.find_element_by_xpath(r'//*[@id="account-textbox"]').send_keys(account[7:])

        # 输入密码
        passwd = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password-textbox"]'))
        )
        sleep(random.uniform(0, 2))
        passwd.send_keys(password)
        login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button-account"]'))
        )
        sleep(random.uniform(0, 2))
        login.click()
        if "验证码"  in self.driver.page_source:
            # assert "验证码" not in self.driver.page_source, '需要验证码'
            print(self.driver.page_source)
            #TODO:破解验证码

        sleep(random.uniform(2, 3))

        # comment
        attrible = self.driver.find_element_by_link_text("美食")
        ActionChains(self.driver).move_to_element(attrible).perform()  # 鼠标悬停动作
        sleep(2)  # 防止被判定为机器
        attrible = self.driver.find_element_by_link_text("日本菜")  # 选择二级分类
        ActionChains(self.driver).move_to_element(attrible).click().perform()
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        print(self.driver.title)  # 打印该页面title
        sleep(10)  # 等待页面完全加载，否则数据不全，可根据电脑配置改变

        # 先获取每个商家的id

        # 再对每一个url进行评论
        self.driver.get('http://www.dianping.com/shop/93217352/review')

        # start comment
        try:
            self.driver.find_elements_by_xpath('//*[@id="J_shop-rating"]/div/ul/li[5]/a').send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
        finally:
            print(list(self.driver.find_elements_by_xpath('//*[@id="J_shop-rating"]/div/ul/li[5]/a')))
        # total_rating = self.driver.find_elements_by_xpath('//*[@id="J_shop-rating"]/div/ul/li[5]/a')
        # taste_rating = self.driver.find_elements_by_xpath('//*[@id="J_review-s1"]/div/ul/li[5]/a')
        # env_rating = self.driver.find_elements_by_xpath('//*[@id="J_review-s2"]/div/ul/li[5]/a')
        # service_rating = self.driver.find_elements_by_xpath('//*[@id="J_review-s3"]/div/ul/li[5]/a')
        #
        # ActionChains(self.driver).move_to_element(total_rating).click()
        # ActionChains(self.driver).move_to_element(taste_rating).click()
        # ActionChains(self.driver).move_to_element(env_rating).click()
        # ActionChains(self.driver).move_to_element(service_rating).click()
        #
        # # 输入评语（最少15个字）
        self.driver.find_elements_by_xpath('//*[@id="J_review-body"]').send_keys('菜品丰富，及其美味，是一个非常非常好的地儿！')
        #
        # # 提交评论
        # self.driver.find_elements_by_xpath('//*[@id="J_review-submit"]').click()
        # if '已成功发表对' in self.driver.page_source:
        #     print('评论成功')
        #     self.driver.quit()  # self.driver.close()  只能关闭当前的窗口，不能关闭所有的




if __name__ == '__main__':
    comment = automatic_comment()
    login = comment.login_dianPing_and_comment('15029269754', 'women.419')

