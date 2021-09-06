import os
import subprocess
import time

global __fol
global exit_code_msg

__fol = 'cache'
secreat2 = 'dfyetrwfvb23675asf6djmfygi'


class EvalError(Exception):
    ...

def __evaluate(

    code:str,

    ) -> str:

    r"""Will evaluate the given code! and returns the output.
        -
        """
    if 'input' in code or 'getpass' in code:
        raise EvalError('input or getpass is not supported!')
    secreat  = 'fytytuhdbuhabbuyt.niuhyysdadcdsf7$65'
    if os.path.isdir(__fol) == False:
        os.mkdir(__fol)
    with open(f'{__fol}/output.py' , 'w+') as __f:
        __f.write(code.__add__(f'\nprint(f"{secreat2}Process **finished** with exit code 0 in {secreat} seconds :white_check_mark:")'))
    start = time.time()
    return_code = subprocess.getoutput(f'python {__fol.__add__("/output.py")}')

    stop = time.time()
    total_time = str(stop - start)
    __total_time = total_time.split(".")[1][0:3]
    total_time = total_time.split('.')[0].__add__( f'.{__total_time}')

    if tuple(subprocess.getstatusoutput(f'python {__fol.__add__("/output.py")}'))[0] == 1:
        return_code = return_code.__add__(f"\n\n{secreat2}Process **crashed** with exit code -1 in {secreat} seconds :x:")
    exit_stats = (return_code.replace(secreat , total_time))
    os.remove(__fol.__add__('/output.py'))
    os.removedirs(__fol)
    return exit_stats


def evaluate(code:str) -> str:
    raw_output = __evaluate(code=code)
    exit_stats_msg = raw_output.split(secreat2)[-1]
    output = raw_output.replace(

        raw_output.split(secreat2)[-1],
        ''
        ).replace(
        secreat2,
        ''
        )
    return f'```\n{output}\n```\n{exit_stats_msg}'