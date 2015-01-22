#! /usr/bin/env python

import sys
import optparse
import os
sys.path.append(os.path.abspath("./"))
import decreasoner

def usage() :
	print "Usage: python %s [-o <output_file>] <input_file>" % os.path.basename(sys.argv[0])

def main() :
	open('.lock', 'w').close()
   
	# Option Parser
	parser = optparse.OptionParser()
	parser.add_option("-o","--output",action="store",type="string",dest="outputFilename")
	(options, args) = parser.parse_args()

	# Make sure we have our mandatory argument (file)
	if len(args) != 1 : 
		print 'You must specify one file to process.'
		usage()
		os.remove('.lock')
		sys.exit(1)

	# Process
	print "The file to process is",args[0]
	if options.outputFilename :
		print "You used the --output option with value",options.outputFilename
		decreasoner.decreasoner().run(args[0],options.outputFilename)
	else :
		decreasoner.decreasoner().run(args[0],args[0]+'.res')

	os.remove('.lock')
	#sys.exit(0)

if __name__ == "__main__" :
	main()
	
