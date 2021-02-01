# Write a function that takes an IP address and returns the domain name
# using PTR DNS records.

import socket


def get_domain(x):
    name, alias, addresslist = socket.gethostbyaddr(x)
    print(name)
    return name


get_domain("8.8.8.8")  # "dns.google"

get_domain("8.8.4.4")  # "dns.google"
