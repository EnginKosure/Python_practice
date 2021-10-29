def sock_merchant(l):
    return [[x, l.count(x)] for x in set(l)]


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))  # ➞ 3

print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))  # ➞ 4

print(sock_merchant([]))  # ➞ 0
