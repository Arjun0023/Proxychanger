import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

# Check if the number of proxies is at least 2
if len(proxy_list) < 2:
    print("Please provide at least 2 proxies for two browsers.")
    exit()

try:
    for i in range(2):  # Create two browser instances
        chrome_options = webdriver.ChromeOptions()

        proxy = proxy_list[i].strip()  # Remove any leading/trailing whitespaces
        print(f"Using proxy for browser {i + 1}: {proxy}")
        chrome_options.add_argument(f'--proxy-server={proxy}')

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        try:
            for site in websites:
                print(f"Opening {site} in browser {i + 1}")
                browser.get(site)
                time.sleep(2)  # Add a delay if needed

            # Do other operations if needed

        except Exception as e:
            print(f"Failed to open sites in browser {i + 1}. Error: {e}")
        finally:
            browser.quit()
            time.sleep(2)  # Add a delay between browsers if needed

except Exception as e:
    print(f"Error: {e}")
