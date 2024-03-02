from datetime import datetime
import math
# from math import math
# from math import math as m

def main():

    def dateNow():
        return datetime.now()
    # print(dateNow())

    def formattedDate():
        now = datetime.now()

        year = now.year
        day = now.day
        month = now.month
        hour = now.hour
        minute = now.minute
        sec = now.second
        mili = now.microsecond # This can be good for a generated formatted password
        
        return f'Today is {day} of {month}, {year}.'
    print(formattedDate())
    
    def mathing():
        # Square Root
        sqrt = math.sqrt(16)
        pi = math.pi
        area_of_circle = math.pi * 5 ** 2 # area of a circle with a radius of 5
        exponents = math.pow(4, 2) # 4 to the power of 2
        return exponents

    # print(mathing())
        

if __name__ == "__main__":
    main()