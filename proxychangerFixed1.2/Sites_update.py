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

delay_seconds = 30
proxy_file = 'proxychangerFixed1.2\Valid_proxies.txt'

proxy_list = []
with open(proxy_file, 'r') as f:
    proxy_list = f.readlines()

chrome_driver_path = ChromeDriverManager().install()
chrome_service = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()

for proxy in proxy_list:
    print(f"Using proxy: {proxy}")
    
    chrome_options.add_argument(f'--proxy-server={proxy}')
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    try:
        tabs = []
        for i, site in enumerate(websites):
            print(f"Opening {site} in a new tab with proxy {proxy}")
            
            if i == 0:
                browser.get(site)
            else:
                browser.execute_script(f"window.open('{site}', '_blank');")
            
            tabs = browser.window_handles
            time.sleep(2)  # Add a delay if needed
        
        while True:
            # Switch between tabs in the order they were opened
            for tab in tabs:
                browser.switch_to.window(tab)
                time.sleep(2)  # Add a delay if needed
    except Exception as e:
        print(f"Failed to open sites with proxy {proxy}. Error: {e}")
    finally:
        browser.quit()
        