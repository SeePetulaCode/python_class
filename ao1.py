#
# Name: Petula Pascall
# SSID: 616064
# Assignment #: 1
# Submission Date: 2/15/19
#
# Description of program :
# This program lists my three favorite places in the Los Angeles area .
#


_8 = 1

print('Three great places to visit in the Los Angeles area are:')

print(_8,'California Science Center')
_8 = _8 + 1
print(_8,'Exposition Park Rose Garden')
_8 = _8 + 1
print(_8, 'Los Angeles County Museum of Art', end='\r\n\r\n')


print('------------------------------')

_8 = int('1') # Technically it's a string turned into an integer? ¯\_(ツ)_/¯

places = ['California Science Center', 'Exposition Park Rose Garden', 'Los Angeles County Museum of Art']

print('Three great places to visit in the Los Angeles area are:')

for fave in places:
    print(_8, fave)
    _8 = _8 + int('1')


