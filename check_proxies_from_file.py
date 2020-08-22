from socks5_proxy_check import socks5_proxy_check


def load_proxies():
    """
    Loads proxies from a local file in the format
        - Single line per ipv4:port
    :return:
    """
    proxy_filename = '/home/nubonix/proxies/socks5_proxies.txt'
    with open(proxy_filename, 'r') as reader:
        proxy_list = reader.readlines()
    return proxy_list


raw_socks5_proxies_list = load_proxies()


with open('working_proxies.txt', 'w') as writer:
    for proxy in raw_socks5_proxies_list:
        if socks5_proxy_check(proxy):
            writer.write(f'{proxy}\n')