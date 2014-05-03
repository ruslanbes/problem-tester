problem-tester
==============

Problem tester is a helper file for contents like Google Code Jam or Codeforces if you are writing your script in Python.

Requirements:
-- Python 2.7
-- Windows
-- Your Python script must get the input values from STDIN ( `a = raw_input()` )

Usage:
Go to the folder where you saved your Python script. For example the folder is C:/.../Round1
Normally the scripts are named A.py, B.py etc.


1. If you have an input **and** output files for the problem A and you want to test if your program returns correct result on that set you should fdo the following:
** Save the input file as C:/.../Round1/A.in
** Save the ouput file as C:/.../Round1/A.correct.out
** Run `python C:/.../problem-tester A`
The tester will generate the A.out and compare A.out with A.correct.out. IMPORTANT: newlines at the end matter, clean them.

2. If you are sure your program is correct and ready to generate an output for the problem A (Google Code Jam), do the following:
-- Download the input file and save it as C:/.../Round1/A-small.in
-- Run `python C:/.../problem-tester A`
-- Take the C:/.../Round1/A-small.out and upload it to the GCG system.

3. If after the contest you got a script from someone else that is, you are sure, is working correctly, and you want to generate a bunch of output files to test your script, do the following:
-- Backup your script somewhere, and reanme the correct script as A.py
-- Run `python C:/.../problem-tester A --correct` - that will walk through all A*.in files and generate appropriate A*.correct.out files
-- Put your script back as A.py
-- Run `python C:/.../problem-tester A`. The script will tell you which files are right and which are wrong


TODO
==============
-- Autodetect os and support Linux. Easy
-- Make it more universal, so that any script could be checked — PHP, Java, C, whatever. Hard, as it often requires setting paths and compiler options.
-- Easier generation of correct files (4 steps are too much)
