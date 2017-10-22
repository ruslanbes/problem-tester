problem-tester
==============

Problem tester is a helper file for contents like Google Code Jam or Codeforces if you are writing your script in Python.

Requirements
--------------
- Python 3+ (Tested on Python 3.6.3)
- Windows
- Expected source of input: STDIN ( `a = input()` )
- Expected source of input: STDOUT

Features
--------------
- Test if your script produces the same output as in problem statement
- Test if your output is obe of the valid solutions (You will write your own validator for that)
- Compare your solution against the correct solution
- Debuggable in PyCharm or other IDEs

Usage:
==============
TL; DR
See the folder `demo`.

Testing your solution
--------------
1. Copy the `problemtester.py` to the root directory of your contest project. E.g. to `/usr/codeforces` or `/usr/googlecodejam`
2. Create a directory for a round. E.g. `cf_873` for round 873 of Codeforces
3. Create subfolder for a problem (`a`, `b`, `c` ). It's just for convenience.
4. Create a file `a.py` and write your solution
5. Create files `a0.in`, `a1.in` ... with input data
6. Create files `a0.ok.out`, `a1.ok.out` .. with output data. Be sure to add a newline at the end of them
7. Run `python problemtester.py cf_873.a.a` I.e a pass a package name:

Output:
```
Checking /usr/codeforces/cf_873/a/a1.out ... OK
Checking /usr/codeforces/cf_873/a/a2.out ... FAIL
```

Testing your solution with a validator:
--------------
Suppose there can be many correct solutions to a problem. You want to check if your script finds one of them.
1. Write a script `validator.py` in the Problem's directory. Check the sample in the `demo` directory
2. Problemtester will ignore the `.ok.out` files and execute this script to test if your solution is correct.

Output:
```
Validating /usr/codeforces/cf_873/a/a1.out ... OK
Validating /usr/codeforces/cf_873/a/a2.out ... FAIL
```


Testing your solution with a solver:
--------------
Solver is a "correct solution" script. Suppose you want to find bugs in your solution. Or maybe you want to hack a competitor (Codeforces).
1. Put a `solver.py` to the Problem's directory. Solver must use STDIN and STDOUT as the normal solution
2. Problemtester will call it first to generate missing `.ok.out` files, then it will test your solution.


Validator + Solver
--------------
If both are present then `.ok.out` files are generated but are ignored at the moment