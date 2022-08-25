def rgb(r, g, b):

    def round_decimal(dec):
        if dec > 255:
            return(255)
        elif dec < 0:
            return(0)
        else:
            return(dec)

    def add_zeros(nr):
        if len(str(nr)) <2:
            return('0'+str(nr))
        else:
            return(nr)

    return("".join([add_zeros(hex(int(x))[2:]) for x in [round_decimal(r),round_decimal(g),round_decimal(b)]]).upper())