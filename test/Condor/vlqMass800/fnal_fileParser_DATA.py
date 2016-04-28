import re, math, os, sys

def usage() :
    print "[usage]  ./fileParser.py SAMPLE=BKG/Data/Signal ENTRY=number of samples  NFILE=number of files PATH=path to skimmed files"
    sys.exit(0)

nParameters=len(sys.argv)
SAMPLE=""
PATH=""
NFILE=0
ENTRY=0

s="\n".join(sys.argv)


if not ("SAMPLE" in s and "PATH" in s and "NFILE" in s and "ENTRY" in s):
    usage()


for i in range(1, nParameters):
    opt=sys.argv[i]
    if "SAMPLE=" in opt:
        SAMPLE=opt[7:]
    elif "PATH=" in opt:
        PATH=opt[5:]
    elif "NFILE=" in opt:
        NFILE=opt[6:]
    elif "ENTRY=" in opt:
	ENTRY=opt[6:]	
    else:
        print "User has supplied an invalid parameter " , opt
        sys.exit(0)



for n_file in range (1, int(NFILE)+1):
    inputfile = open('dummy_os2lana_DATA.py')
    outputfile = open(str(SAMPLE)+'/'+str(SAMPLE)+'_'+str(n_file)+'.py', 'w')
    for line in inputfile:
	line = line.replace('nsample' , str(ENTRY) )
	line = line.replace('njob' ,	str(n_file) )
#        line = line.replace('path_to_sample','file:'+str(PATH)+'/root_skim_file_'+str(n_file)+'.root')
#	line = line.replace('path_to_sample','root://cms-xrd-global.cern.ch/'+str(PATH)+'/B2GEDMNtuple_'+str(n_file)+'.root')
	line = line.replace('path_to_sample','root://eoscms.cern.ch/'+str(PATH)+'/B2GEDMNtuple_'+str(n_file)+'.root')
        line = line.replace('output',str(SAMPLE)+'_'+str(n_file)+'.root')
        outputfile.writelines(line)
    inputfile.close()
    outputfile.close()
