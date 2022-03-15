from queue import Empty
import time
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType

def linha():
    print('-='*60)
class viewBot:
    def __init__(self, proxyIp, linkIp):
        self.proxyIP = proxyIp
        self.PROXY = self.proxyIP
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = self.PROXY
        self.proxy.ssl_proxy = self.PROXY
        self.linkIp = linkIp
        if len(self.proxyIP) < 10:
            linha()
            print('Você está navegando sem proxy.')
            linha()
        else:
            linha()
            print(f'Você está navegando com o proxy {self.PROXY}.')
            linha()
    def openGoogleWithProxy(self):
        self.capabilities = webdriver.DesiredCapabilities.CHROME
        self.proxy.add_to_capabilities(self.capabilities)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(f'--proxy--server={self.PROXY}')
        self.capabilitiesdriver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options, desired_capabilities=self.capabilities)
        self.capabilitiesdriver.get(self.linkIp)
        # self.capabilitiesdriver.get('https://ipinfo.io/') #SITE PARA VISUALIZAR O ENDERECO DE IP 
        time.sleep(5)
        self.capabilitiesdriver.refresh()
    def openGoogleWithoutProxy(self):
            self.capabilities = webdriver.DesiredCapabilities.CHROME
            self.chrome_options = webdriver.ChromeOptions()
            self.capabilitiesdriver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options, desired_capabilities=self.capabilities)
            self.capabilitiesdriver.get(self.linkIp)
            time.sleep(5)
            self.capabilitiesdriver.refresh()
linha()
proxy = input('Insira o IP do PROXY => ')
linha()
link = input('Insira um LINK => ')
while (len(link) == 0):
    linha()
    print('Você precisa inserir um link')
    print('')
    link = input('Insira um LINK => ')
bot = viewBot(proxy, link)
if len(proxy) < 10:
    bot.openGoogleWithoutProxy()
if len(proxy) > 11:
    bot.openGoogleWithProxy()