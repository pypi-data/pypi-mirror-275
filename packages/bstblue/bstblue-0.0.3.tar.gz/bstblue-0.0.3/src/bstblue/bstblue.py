# bstblue/browser.py

class SimpleBrowser:
    def __init__(self):
        print("Simple Browser")

    def open_url(self, url):
        import os

        platform = os.name

        if platform == 'posix':
            cmd = 'xdg-open'
        elif platform == 'nt':
            cmd = 'start'
        else:
            raise Exception("Platform not supported")

        os.system(f"{cmd} {url}")

def dev():
    browser = SimpleBrowser()
    url = input("Enter URL: ")
    browser.open_url(url)

if __name__ == "__main__":
    dev()
