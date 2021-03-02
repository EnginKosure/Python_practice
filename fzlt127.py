def sum_complex(nums):
    z = sum(complex(num.replace('i', 'j')) for num in nums)
    a, b = z.real, z.imag
    s = str(z).replace('j', 'i').replace('1i', 'i')
    return s[1:-1] if a and b else str(int(a)) if not b else s


def sum_complex2(data):
    res = sum([complex(i.replace("i", "j")) for i in data])
    x = (int(res.real) == 0)*" " or int(res.real)
    y = (int(res.imag) == 0)*" " or (int(res.imag) == -1) * \
        "-i" or (int(res.imag) == 1)*"i" or f"{int(res.imag):+}i"
    r = f"{x}{y}"
    return (r.replace(" ", ""))


sum_complex(["3+4i"])
