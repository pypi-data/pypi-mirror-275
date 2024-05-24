

'''
	import vegan_bits_2
	bits_path = vegan_bits_2.sequences ()
'''


#----
#
import pathlib
from os.path import dirname, join, normpath
import sys
#
#----


def sequences ():
	this_directory_path = str (pathlib.Path (__file__).parent.resolve ())
	sequences_path = str (normpath (join (this_directory_path, "sequences")))

	return sequences_path
	