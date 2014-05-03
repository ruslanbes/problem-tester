import os
import glob
import filecmp
from subprocess import call
import sys, getopt

def main(argv):
    mode = 'test'

    opts, args = getopt.getopt(argv,'', ['correct'])
    for arg in args:
        if arg == '--correct':
            mode = 'correct'

    name = args[0]


    f_in_mask = name + '*.in'
    python_script = name + '.py'
    if not os.path.isfile(python_script):
        print "Python script", python_script, "is missing"
        exit()

    for f_in in glob.glob(f_in_mask):    
        testname = os.path.splitext(f_in)[0]
        if mode == 'correct':
            f_out = testname + '.correct.out'
            f_correct_out = None
        else:
            f_out = testname + '.out'
            f_correct_out = testname + '.correct.out'
        fh_out = open(f_out, 'w')
        cmd = 'type ' + f_in + ' | python ' + python_script 
        #print cmd
        call(cmd, shell=True, stdout=fh_out)
        fh_out.close()

        #compare
        if mode != 'correct' and os.path.isfile(f_correct_out) and os.access(f_correct_out, os.R_OK):
            res = filecmp.cmp(f_out, f_correct_out)
            print "Checking", f_out, "...", ("OK" if res else "FAIL")
        else:
            print "Generated", f_out



if __name__ == "__main__":
   main(sys.argv[1:])