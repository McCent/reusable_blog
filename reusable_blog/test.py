def computepay():
    if h>40:
    	p=(40*r)+(h-40)*(r*1.5)
    else:
    	p=h*r
    return p

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)



print "Pay ", computepay()