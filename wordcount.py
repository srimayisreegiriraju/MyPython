def wordcount(filename):
	wordcounter=0
	f=open(filename,'r')
	for lines in f:
		f1=lines.split()
		wordcounter=wordcounter+len(f1)
	f.close()
	print "number of words", wordcounter

x=raw_input("enter the filename:")
wordcount(x)
