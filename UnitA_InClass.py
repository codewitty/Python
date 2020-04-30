# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment A
#
# This program practices integer and float product/division
# and formatting output.

height = 7.1 
width = 2.9 
area = width * height

print ("height: %-30s" % height)
print ("width:  %-30s"  % width)
print ("area:   %-30s" % area)

width = width // 2
height = height // 2
area = width * height

# After division
print ()
print ("After division")
print ("height: %-30s" % height)
print ("width:  %-30s"  % width)
print ("area:   %-30s" % area)

'''
Output:

height: 7.1
width:  2.9
area:   20.59

After division
height: 3.0
width:  1.0
area:   3.0

'''
