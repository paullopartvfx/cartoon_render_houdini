# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-08-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************


"""
0. CONNECT the decorator "print_process" with all sleeping functions.
   Print START and END before and after.

   START *******
   main_function
   END *********


1. Print the processing time of all sleeping functions.
END - 00:00:00


2. PRINT the name of the sleeping function in the decorator.
   How can you get the information inside it?

START - long_sleeping

"""


import time
from time import strftime, gmtime


#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args):
        print("START - {} -".format(func.__name__))

        start = time.time()

        func(*args)

        end = time.time()
        cook_time = round(end - start, 2)

        def time_format(input_ms):
            if input_ms is not None:
                seconds = int(input_ms)
                
                h = seconds // 3600 % 24
                m = seconds % 3600 // 60
                s = seconds % 3600 % 60
                ms = int(input_ms % 1 * 100)
                
                return "{:02d}:{:02d}:{:02d}".format(m, s, ms)
 

        print("END - {} - Min:Sec:Rest".format(time_format(cook_time)))
    return wrapper


#*********************************************************************
# FUNC
@print_process
def short_sleeping(name):

    time.sleep(0.15)
    print(name)

@print_process
def mid_sleeping():
    time.sleep(2.25)

@print_process
def long_sleeping():
    time.sleep(4)

short_sleeping("so sleepy")

mid_sleeping()

long_sleeping()

