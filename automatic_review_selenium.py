from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import re
import requests
from lxml import etree

class AutomaticComment(object):

    def __init__(self):
        # 代理ip
        # self.options = Options()
        # self.options.add_argument('--proxy-server=http://%s' % proxy)
        # user-agent
        # self.options.add_argument('--user-agent=%s' % ua)
        # self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', chrome_options=self.options)
        # 无头请求
        # self.options.add_argument('--headless')
        # 验证ip和ua
        # self.driver.get("http://httpbin.org/ip")
        # self.driver.get("http://httpbin.org/user-agent")

        self.url = 'http://www.dianping.com/'
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

    def login_dianPing(self, account, password):
        '''
        大众点评模拟登陆,随机睡眠
        :param phone: 账号
        :param password: 账号密码
        :return:
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
        sleep(3)
        passwd.send_keys(password)
        login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button-account"]'))
        )
        sleep(3)
        login.click()

        # 悬停动作
        # attrible1 = self.driver.find_element_by_link_text("美食")
        # ActionChains(self.driver).move_to_element(attrible1).perform()  # 鼠标悬停动作
        # sleep(2)  # 防止被判定为机器
        # attrible2 = self.driver.find_element_by_link_text("日本菜")  # 选择二级分类
        # ActionChains(self.driver).move_to_element(attrible2).click().perform()
        #
        # current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        # all_windows = self.driver.window_handles  # 获取所有窗口handle name
        #
        # # 切换window，如果window不是当前window，则切换到该window
        # for window in all_windows:
        #     if window != current_window:
        #         self.driver.switch_to.window(window)
        # print(self.driver.title)  # 打印该页面title

        sleep(3)  # 等待页面完全加载，否则数据不全，可根据电脑配置改变



    def get_host_info(self, city=1, keyword='星巴克'):
        """
        获取每个城市星巴克的商户id
        :param city: 城市编号
        :param keyword: 搜索的关键字
        :return: 商户信息如商户id
        """
        data = []
        for page in range(1, 49):
            url = 'https://www.dianping.com/search/keyword/{}/0_{}/p{}'.format(city, keyword, page)
            self.driver.get(url)
            host_id_list = etree.HTML(self.driver.page_source).xpath('//div[@class="pic"]/a/@data-shopid')
            host_name_list = etree.HTML(self.driver.page_source).xpath('//div[@class="pic"]/a/img/@title')
            for x, y in zip(host_id_list, host_name_list):
                data.append((x, y))
            print(data)
            sleep(10)
            print('第【%s】页爬取完毕' % page)

        return data


    def comment_to_host(self, account, password):

        self.login_dianPing(account, password)
        # start comment
        self.driver.get('http://www.dianping.com/shop/95912540/review')
        try:
            # 取消之前的评论
            # comment_cancel = self.driver.find_element_by_xpath('//*[@id="confirmCancel"]')
            # if len(comment_cancel):
            #     comment_cancel.click()
            # 总体评价
            total_rating = self.driver.find_element_by_xpath('//*[@id="J_shop-rating"]/div/ul/li[5]/a')
            ActionChains(self.driver).move_to_element(total_rating).click(total_rating).perform()
            # 口味评价
            taste_rating = self.driver.find_element_by_xpath('//*[@id="J_review-s1"]/div/ul/li[5]/a')
            ActionChains(self.driver).move_to_element(taste_rating).click(taste_rating).perform()
            # 环境评价
            env_rating = self.driver.find_element_by_xpath('//*[@id="J_review-s2"]/div/ul/li[5]/a')
            ActionChains(self.driver).move_to_element(env_rating).click(env_rating).perform()
            # 服务评价
            service_rating = self.driver.find_element_by_xpath('//*[@id="J_review-s3"]/div/ul/li[5]/a')
            ActionChains(self.driver).move_to_element(service_rating).click(service_rating).perform()
            # 人均价格
            mean_price = self.driver.find_element_by_xpath('//*[@id="J_review-ap"]')
            mean_price.send_keys('30')
            # 上传照片
            # import win32gui, win32con
            # upload = self.driver.find_element_by_xpath('//*[@id="rt_rt_1cs8a9q3th6u31n8cpohg1iod1"]/label')'//*[@id="rt_rt_1cs8dce581jej11a129b1ravfma1"]/label'
            # upload.click()
            # sleep(2)
            # # win32gui
            # dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
            # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
            # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
            #
            # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\\yhouse\\Desktop\\1.png')  # 往输入框输入绝对地址
            # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

            # 喜欢的菜
            open = self.driver.find_element_by_xpath('//*[@id="review_form_div"]/div[7]/div/div/a')
            open.click()
            sleep(5)   # 必须加载时间否则元素不可见
            user_input = self.driver.find_element_by_xpath('//*[@id="review_form_div"]/div[7]/div/div/div/div/input')
            ActionChains(self.driver).click(user_input).send_keys('星巴克咖啡').send_keys(Keys.ENTER).perform()

            # like_meal1 = self.driver.find_element_by_xpath('//*[@id="review_form_div"]/div[6]/div/div/div/a[1]')
            # like_meal2 = self.driver.find_element_by_xpath('//*[@id="review_form_div"]/div[6]/div/div/div/a[2]')
            # ActionChains(self.driver).move_to_element(like_meal1).click(like_meal1).perform()
            # ActionChains(self.driver).move_to_element(like_meal2).click(like_meal2).perform()

            # 输入评语（最少15个字）
            com = self.driver.find_element_by_xpath('//*[@id="J_review-body"]')
            com.send_keys('菜品丰富，及其美味，是一个非常非常好的地儿！')
            # 提交评论
            sleep(3)
            commit = self.driver.find_element_by_xpath('//*[@id="J_review-submit"]')
            commit.click()
            sleep(2)
        except NoSuchElementException as e:
            print(e)


        # if '点评已提交，感谢你的分享！' in etree.HTML(self.driver.page_source).xpath('/html/body/div[3]/div[1]/div/div[2]/text()')[0]:
        #     print('评论成功')
        self.driver.quit()  # close all windows
        # self.driver.close() # close current window


    def comment_to_user(self, account, password):
        self.login_dianPing(account, password)
        # 每一个商户下面有很多的评论，而这些评论每一个都有自己的data-id
        self.driver.get('http://www.dianping.com/shop/95912540')

        # 模拟鼠标滚轮滑动，执行js
        js1 = 'window.scrollTo(0,1000)'  #window.scrollTo(xpos,ypos)
        self.driver.execute_script(js1)
        sleep(3)

        # 点赞
        self.driver.find_element_by_xpath('//*[@id="review_473737276_action"]/div/a[1]').click()
        # 回应
        self.driver.find_element_by_xpath('//*[@id="review_473737276_action"]/div/a[2]').click()

        # 切换窗口（必须要有这一步，否则会在上一个页面执行下面的操作）
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name

        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)

        sleep(3)
        # 跳转到评论页
        js2 = 'window.scrollTo(0,1200)'
        self.driver.execute_script(js2)
        sleep(3)

        # 在我想回应里写字
        wo_want_comment = self.driver.find_element_by_xpath('//*[@id="review-detail"]/div[2]/div[1]/div[2]/div[2]/textarea')
        wo_want_comment.send_keys('菜品丰富，及其美味，是一个非常非常好的地儿！')

        # 发布
        publish = self.driver.find_element_by_xpath('//*[@id="review-detail"]/div[2]/div[1]/div[2]/div[2]/div/a')
        publish.click()

        sleep(2)
        # 确定发布
        try:
            # 必须要有这一步
            self.driver.switch_to.window(self.driver.current_window_handle)
            # 确认
            confirm = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/span[1]/a')
            confirm.click()

        except (NoSuchElementException,NoAlertPresentException) as e:
            print(e)
        finally:
            self.driver.quit()



    def every_host_comment_id(self):
        pass

    def upload_picture(self):
        import win32gui
        import win32con
        # self.driver.get(r'C:\Users\yhouse\Desktop\upload.html')
        upload = self.driver.find_element_by_xpath('//*[@id="rt_rt_1cs8a9q3th6u31n8cpohg1iod1"]/label')
        upload.click()
        sleep(1)

        # win32gui
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\\yhouse\\Desktop\\1.png')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

if __name__ == '__main__':
    comment = AutomaticComment()
    comment.comment_to_user('15029269754', 'women.419')