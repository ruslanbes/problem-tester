@echo off
del a1.correct.out
del a2.correct.out
del a1.out
del a2.out
python ../problem-tester.py a --correct
echo -----
python ../problem-tester.py a
