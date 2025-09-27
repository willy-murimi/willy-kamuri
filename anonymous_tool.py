#This is the backend class of anonymous browsing
import mechanize, random

class anonymousBrowser(mechanize.Browser):
    def __init__(self, proxies = [], user_agents = []):
        mechanize.Browser.__init__(self)
        self.set_handle_robots = False
        self.proxies = proxies
        self.user_agents = user_agents()
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar = self.cookie_jar
        self.anonymize()

    def clear_cookies(self):
        self.cookie_jar = cookieLWPCookieJar()
        self.set_cookiejar = self.cookie_jar
        for cookie in ab.cookie_jar:
            print('THIS IS YOUR COOKIE')
            print(cookie)


    def change_user_agent(self):
        index = random.randrange(0, len(self.user_agents))
        self.addheaders = [("user-agents".self(user_agents[index]))]
    def user_agents():
        for user_agents in page.read(browser.open(url)):
            try:
                url = 'http://useragentstring.com/'
                urli = requests.get(url)
                if response.status_code == 200:
                    return page.read
                   
                    for user_agents in self.user_agents:
                        try:
                            user_agents = user_agents
                        except:
                             self.user_agents = user_agents

            except:
                user_upheld = ('X11: U ' + 'Linux 2.4.2-2 i586: en-US: m18') 
                user_agents = [(f'user-agents','Mozilla/5.0 {user_upheld}' +  ' Gecko/20010131 Netscape6/6.01')]
                self.user_agents = user_agents

                
    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.user_agents))
            self.set_proxies('http' , self.proxies[index])
    def anonymize(self, sleep = False):
        self.clear_cookies()
        self.change_proxy()
        self.change_user_agent()
        if sleep:
            time.sleep(60)
            sleep(60)


