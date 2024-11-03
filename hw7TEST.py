# hw7TEST.py

>>> from hw7 import *

##### Volume #####

# set and get

>>> v = Volume()
>>> v.set(5.3)
>>> v
Volume(5.3)
>>> v.get()
5.3
>>> v.get()==5.3 # return not print
True
>>> v.set(13.2)
>>> v
Volume(11)
>>> v.set(-1.2)
>>> v
Volume(0)


# __init__, __repr__, up, down

>>> v = Volume(4.5) # set Volume with value
>>> v
Volume(4.5)
>>> v.up(1.4)
>>> v
Volume(5.9)
>>> v.up(6) # should max out at 11
>>> v
Volume(11)
>>> v.down(3.5)
>>> v
Volume(7.5)
>>> v.down(10) # minimum must be 0
>>> v
Volume(0)

# default arguments for __init__

>>> v = Volume() # Volume defaults to 0
>>> v
Volume(0)


# can compare Volumes using == 

>>> # comparisons
>>> v = Volume(5)
>>> v.up(1.1)
>>> v == Volume(6.1)
True
>>> Volume(3.1) == Volume(3.2)
False

# constructor cannot set the Volume greater
# than 11 or less than 0

>>> v = Volume(20)
>>> v
Volume(11)
>>> v = Volume(-1)
>>> v
Volume(0)
>>>

# more thorough checks of clamping

>>> v = Volume()
>>> [ (val*.5,v.set(val*.5),str(v)) for val in range(-3,30,4)] # set
[(-1.5, None, 'Volume(0)'), (0.5, None, 'Volume(0.5)'), (2.5, None, 'Volume(2.5)'), (4.5, None, 'Volume(4.5)'), (6.5, None, 'Volume(6.5)'), (8.5, None, 'Volume(8.5)'), (10.5, None, 'Volume(10.5)'), (12.5, None, 'Volume(11)'), (14.5, None, 'Volume(11)')]
>>> [ (val*.5,Volume(val*.5)) for val in range(-3,30,4)] # constructor
[(-1.5, Volume(0)), (0.5, Volume(0.5)), (2.5, Volume(2.5)), (4.5, Volume(4.5)), (6.5, Volume(6.5)), (8.5, Volume(8.5)), (10.5, Volume(10.5)), (12.5, Volume(11)), (14.5, Volume(11))]
>>> v = Volume(5)
>>> [ (v.up(.75), str(v)) for i in range(10) ]  # up
[(None, 'Volume(5.75)'), (None, 'Volume(6.5)'), (None, 'Volume(7.25)'), (None, 'Volume(8.0)'), (None, 'Volume(8.75)'), (None, 'Volume(9.5)'), (None, 'Volume(10.25)'), (None, 'Volume(11.0)'), (None, 'Volume(11)'), (None, 'Volume(11)')]
>>> v = Volume(5)
>>> [ (v.down(.75), str(v)) for i in range(10) ] # down
[(None, 'Volume(4.25)'), (None, 'Volume(3.5)'), (None, 'Volume(2.75)'), (None, 'Volume(2.0)'), (None, 'Volume(1.25)'), (None, 'Volume(0.5)'), (None, 'Volume(0)'), (None, 'Volume(0)'), (None, 'Volume(0)'), (None, 'Volume(0)')]
>>> 

##### partyVolume #####

>>> partyVolume('party1.txt')
Volume(6.35)
>>> partyVolume('party2.txt')
Volume(3.75)
>>> partyVolume('party3.txt')
Volume(0.75)

# make sure return not print

>>> partyVolume('party1.txt')==Volume(6.35) # return not print
True
>>> partyVolume('party2.txt')==Volume(3.75)
True
>>> partyVolume('party3.txt')==Volume(0.75)
True








