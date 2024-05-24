class wbdev:

    def dev(url):
        system = __import__("os").name
        if system == "posix":  # For Linux/macOS
            __import__("os").system(f'xdg-open {url}')
        elif system == "nt":   # For Windows
            __import__("os").system(f'start {url}')
        else:
            print("Unsupported operating system.")

    if __name__ == "__main__":
        link = "https://blueboy.dev"
        dev(link)
