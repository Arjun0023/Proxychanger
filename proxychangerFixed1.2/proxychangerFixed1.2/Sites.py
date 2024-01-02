# import webbrowser
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



websites = [
    "http://play518.atmequiz.com/",
    "http://138.live.qureka.com/",
    "http://play595.atmequiz.com/",
    "https://3136.play.quizzop.com/",
    "https://ml83.mchamplite.com/",
    "http://138.live.predchamp.com/",
    "https://3135.play.gamezop.com/",
    "http://266.go.mglgamez.com/",
    "https://3135.play.gamezop.com/",
    "http://1109.game.qureka.com/",
]




# browser_path = r"C:\Path\to\your\browser\executable\chromedriver.exe"

#     your control panel
delay_seconds = 30
proxy_file = 'proxychangerFixed1.2\Valid_proxies.txt'




proxy_list = []
with open(proxy_file, 'r') as f:
    proxy_list = f.readlines()



chrome_driver_path = ChromeDriverManager().install()
# chrome_driver_path = browser_path
chrome_service = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()

for proxy in proxy_list:
    for site in websites:
        print(f"Opening {site} with proxy {proxy}")
        
        chrome_options.add_argument(f'--proxy-server={proxy}')
        # Use webdriver_manager to automatically download and manage the Chrome webdriver
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        try:
            browser.get(site)
            # Add additional actions as needed
            time.sleep(30)  # Let the page load for a few seconds
            browser.close()
        except:
            print(f"Failed to open {site} with proxy {proxy}")
            # browser.quit()
            browser.close()
            

