import os
import glob
import filecmp
import sys, getopt


def main(argv):
    mode = 'test'

    opts, args = getopt.getopt(argv, '', [])

    # accept param like cf873.a - i.e. module path
    m_path = args[0]
    name = m_path.split('.')[-1]
    tester_dir = os.path.dirname(os.path.realpath(__file__))
    path = tester_dir + '/' + m_path.replace('.', '/')
    script_dir = os.path.dirname(path)
    python_script = path + '.py'
    f_in_mask = path + '*.in'

    if not os.path.isfile(python_script):
        print("Python script", python_script, "is missing")
        exit()

    has_validator = os.path.isfile(script_dir + '/validator.py')
    if has_validator:
        validator_module = m_path[:-len(name)] + "validator"
        validator = __import__(validator_module, globals(), locals(), ["validate"], 0)

    has_solver = os.path.isfile(script_dir + '/solver.py')
    if has_solver:
        solver_module = m_path[:-len(name)] + "solver"

    for f_in in glob.glob(f_in_mask):    
        test_name = os.path.splitext(f_in)[0]
        f_out = test_name + '.out'
        f_ok_out = test_name + '.ok.out'

        if has_solver and not os.path.isfile(f_ok_out):
            print("Generating", f_ok_out, "...")
            fh_in = open(f_in, 'r')
            fh_ok_out = open(f_ok_out, 'w')
            sys_in, sys_out = set_streams(fh_in, fh_ok_out)

            run_problem(solver_module)

            set_streams(sys_in, sys_out)
            fh_in.close()
            fh_ok_out.close()

        fh_in = open(f_in, 'r')
        fh_out = open(f_out, 'w')
        sys_in, sys_out = set_streams(fh_in, fh_out)

        run_problem(m_path)

        set_streams(sys_in, sys_out)
        fh_in.close()
        fh_out.close()

        # compare

        if has_validator:
            res = validator.validate(f_in, f_out)
            print("Validating", f_out, "...", ("OK" if res else "FAIL"))
        else:
            if os.path.isfile(f_ok_out) and os.access(f_ok_out, os.R_OK):
                res = filecmp.cmp(f_out, f_ok_out)
                print("Checking", f_out, "...", ("OK" if res else "FAIL"))
            else:
                print("Checking", f_out, "...", "Permission denied or file does not exist:", f_ok_out)


def set_streams(fh_in, fh_out):
    bak_in = sys.stdin
    bak_out = sys.stdout
    sys.stdin = fh_in
    sys.stdout = fh_out
    return bak_in, bak_out


def run_problem(mod):
    if mod in sys.modules:
        del sys.modules[mod]
    problem = __import__(mod, globals(), locals(), ['main'], 0)
    if 'main' in dir(problem):
        problem.main()


if __name__ == "__main__":
    main(sys.argv[1:])