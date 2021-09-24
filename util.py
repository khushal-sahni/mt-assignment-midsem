from wxconv import WXC


def wx_converter(word):
    con = WXC(order='utf2wx')
    return con.convert(word)