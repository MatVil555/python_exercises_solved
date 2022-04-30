from Utils import EvenStream
from decimal import *

# Task 11--
def calculate_cost(duration_in_seconds):
    #minute_rate = 1.45
    #duration_in_seconds=duration_in_seconds*1.0
    minute_rate = Decimal(1.45)
    duration_in_seconds=Decimal(duration_in_seconds)
    cost = minute_rate * duration_in_seconds / Decimal(60)
    output=float(cost)
    return output


# Task 12--
def print_from_stream(n, stream=EvenStream()):
    stream=stream if stream.current==-1 or stream.current==-2 else EvenStream()
    #sometimes it was not calling neither Eve nor Odd, so stream.current was not formatting any more,
    # the previous ternary operator checks that stream.current is back to -1 or -2
    output = []
    for i in range(n):
        a=stream.get_next()
        output.append(a)
    return output
