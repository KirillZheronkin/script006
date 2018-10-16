example = """
ping ya.ru
PING ya.ru (87.250.250.242) 56(84) bytes of data.
64 bytes from ya.ru (87.250.250.242): icmp_seq=1 ttl=53 time=36.7 ms
64 bytes from ya.ru (87.250.250.242): icmp_seq=2 ttl=53 time=39.5 ms
64 bytes from ya.ru (87.250.250.242): icmp_seq=3 ttl=53 time=37.1 ms
64 bytes from ya.ru (87.250.250.242): icmp_seq=4 ttl=53 time=37.2 ms
64 bytes from ya.ru (87.250.250.242): icmp_seq=5 ttl=53 time=40.6 ms
^C
--- ya.ru ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 36.719/38.254/40.603/1.549 ms
"""


# write decorator that cashes results


