# Write a function that takes an IP address and returns the domain name
# using PTR DNS records.

# Example
# get_domain("8.8.8.8") ➞ "dns.google"

# get_domain("8.8.4.4") ➞ "dns.google"
# Notes
# You may want to import socket.
# Don't cheat and just print the domain name, you need to make a real DNS request.
# Return as a string.


import socket

name, alias, addresslist = socket.gethostbyaddr('8.8.8.8')
# print(name)
# 'dns.google'


def get_domain(s):
    name, _, _ = socket.gethostbyaddr(s)
    print(name)
    # return socket.gethostbyaddr(ip_address)[0]


get_domain("8.8.8.8")  # "dns.google"

get_domain("8.8.4.4")  # "dns.google"
