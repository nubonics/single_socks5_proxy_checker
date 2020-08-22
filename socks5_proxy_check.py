import requests


def socks5_proxy_check(proxy):
    # url = 'http://ifconfig.me/ip'
    url = 'http://ipv4.icanhazip.com'
    # proxy = '216.144.230.233:15993' # working proxy august/22/2020
    proxies = {
        'http': f'socks5://{proxy}',
        'https': f'socks5://{proxy}',
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=3)
    except requests.exceptions.ConnectTimeout:
        return False
    except requests.exceptions.ReadTimeout:
        return False
    except requests.exceptions.ConnectionError:
        return False
    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == '__main__':
    socks5_proxy_check()
