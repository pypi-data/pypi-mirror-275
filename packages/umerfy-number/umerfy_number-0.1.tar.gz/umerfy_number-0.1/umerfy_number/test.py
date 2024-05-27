def number_conv(number):
    number=str(number)
    suffex="L"
    if len(number)==3:
        return number
    elif len(number)>=4 and len(number)<=6:
       suffex="K"
       if len(number)==4:
            return number[0]+suffex
       elif len(number)==5:
          return number[0:2] + suffex
       elif len(number)==6:
          return number[0:3] + suffex
    elif len(number)>= 7 and len(number)<=9:
        suffex="M"
        if len(number)==7:
              return number[0] + suffex
        elif len(number)==8:
            return number[0:2] + suffex
        elif len(number)==9:
             return number[0:3] + suffex
        elif len(number)==10:
             return number[0:4] + suffex