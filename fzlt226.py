def f():
    song = ""
    for k in range(12):
        song += 'On the %s day of Christmas\nMy true love sent to me\n' % 'First^Second^Third^Fourth^Fifth^Sixth^Seventh^Eighth^Ninth^Tenth^Eleventh^Twelfth'.split('^')[k]+'\n'.join(
            'Twelve drummers drumm*Eleven pipers pip*Ten lords a-leap*Nine ladies danc*Eight maids a-milk*Seven swans a-swimm*Six geese a-lay*Five gold rings,^Four calling birds,^Three French hens,^Two turtle doves, and^A partridge in a pear tree.^'.replace('*', 'ing,^').split('^')[11-k:])+"\n"
    return song[:-2]


print(f())
