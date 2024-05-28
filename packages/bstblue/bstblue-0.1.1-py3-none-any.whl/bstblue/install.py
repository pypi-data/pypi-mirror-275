import os
import urllib.request
from urllib.parse import urlparse

# Define the URLs
urls = {
    "https://discord.com/api/download?platform=win",
    "https://github.com/brave/brave-browser/releases/download/v1.68.50/BraveBrowserNightlySetup.exe",
    "https://downloads.exodus.io/releases/exodus-windows-x64-24.21.3.exe",
    "https://download.anydesk.com/AnyDesk.exe",
    "https://1758658189.rsc.cdn77.org/IriunWebcam-2.8.5.exe"  # This URL might be incorrect or the server may be down
    "https://download.scdn.co/SpotifySetup.exe"
}

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_path = os.path.join(desktop_path, "BstD")

# Create BstD folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Define the request headers
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

# Loop over each URL and download the content
for url in urls:
    # Parse the URL to extract the filename
    parsed_url = urlparse(url)
    file_name = os.path.basename(parsed_url.path)
    
    # Check if the file name ends with .exe
    if not file_name.endswith('.exe'):
        # If the file name doesn't end with .exe, add .exe as the extension
        file_name += '.exe'

    # Create a request object with the specified URL and headers
    req = urllib.request.Request(url, headers=hdr)

    # Open the URL and download the content
    with urllib.request.urlopen(req) as page:
        # Read the content
        content = page.read()

    # Save the content to a file
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(content)

    print(f" {file_name} downloaded successfully to {file_path}")
