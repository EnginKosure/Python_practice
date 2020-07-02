def no_duplicate_letters(phrase):
    for i in phrase.split():
        if len(set(i)) != len(i):
            return False
    return True


print(no_duplicate_letters("Fortune favours the bold."))
print(no_duplicate_letters(
    "You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap."))
print(no_duplicate_letters("An apple a day keeps the doctor away."))
