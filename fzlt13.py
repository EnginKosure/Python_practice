def reverse(string):

    if len(string) <= 1:
        return string
    return reverse(string[1:])+string[0]


print(reverse("hello"))  # olleh


def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])


print(sum([5, 7, 3, 8, 10]))
