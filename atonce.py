from AppOpener import open as app_open
import webbrowser
import time

# -------------------------------
# CONFIGURATION
# -------------------------------

apps = [
    "notepad",
    "file explorer"
]

urls = [
    "https://www.youtube.com",
]

APP_DELAY = 1
URL_DELAY = 2

# -------------------------------
# FUNCTIONS
# -------------------------------

def open_apps(app_list):
    for app in app_list:
        try:
            app_open(app)
            time.sleep(APP_DELAY)
        except:
            pass

def open_websites(url_list):
    for url in url_list:
        try:
            webbrowser.open(url, new=2)
            time.sleep(URL_DELAY)
        except:
            pass

# -------------------------------
# MAIN
# -------------------------------

if __name__ == "__main__":
    open_apps(apps)
    time.sleep(5)
    open_websites(urls)
