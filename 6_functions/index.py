def say_wtf(string):
    print(string + ", wtf?")


say_wtf('setoid')



accum = 0

def inc():
    global accum
    accum += 1
    print(accum)


inc()
inc()
inc()