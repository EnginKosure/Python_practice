input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def decode_string(string):
    def decode_char(char):
        return chr((((ord(char) + 2) - 97) % 26) + 97) if char.isalpha() else char
    return "".join(decode_char(char) for char in string)


decode_string(input_string)
