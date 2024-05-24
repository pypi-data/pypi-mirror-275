from sys import getsizeof
from logging import basicConfig, WARNING, INFO, info
from sys import stdout
from threading import get_ident
from functools import wraps
from time import time
from typing import Callable
from dis import Bytecode
from collections import Counter


def function_calls(func: Callable) -> list:
    """Lists the number of calls of a function to help profile what needs to be optimized first

    Args:
        func (Callable): a function call

    Returns:
        list: _description_
    """
    funcs: list = []
    bytecode: Bytecode = Bytecode(func)
    instrs: list = list(reversed([instr for instr in bytecode]))
    for (ix, instr) in enumerate(instrs):
        if instr.opname == "CALL_FUNCTION" or instr.opname == "CALL_FUNCTION_EX" or instr.opname == "CALL_FUNCTION_KW":
            load_func_instr = instrs[ix + instr.arg + 1]
            funcs.append(load_func_instr.argval)
    return Counter([funcname for (_, funcname) in enumerate(reversed(funcs), 1)]).most_common()


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(
            'func:%r args:[%r, %r] took: %2.4f sec' % (
                f.__name__, args, kw, te-ts
            )
        )
        return result
    return wrap


def logs_config(
    file_path: str | None = None,
    verbose: bool = None
) -> None:
    if file_path:
        basicConfig(
            format='%(asctime)s %(message)s',
            datefmt='[%m/%d/%Y %I:%M:%S %p]',
            encoding='utf-8',
            level=INFO if verbose else WARNING,
            filename=file_path,
        )
    else:
        basicConfig(
            stream=stdout,
            format='%(asctime)s %(message)s',
            datefmt='[%m/%d/%Y %I:%M:%S %p]',
            encoding='utf-8',
            level=INFO if verbose else WARNING,
        )


def error_manager(max_tries: int = 1) -> object:
    def funcwrapper(func) -> object:
        def argswrapper(*args, **kwargs) -> object:
            x: object = None
            for i in range(max_tries):
                try:
                    x = func(*args, **kwargs)
                    break
                except Exception as e:
                    print(f"Error at try {i}/{max_tries}. {type(e)}:{e}")
            return x
        return argswrapper
    return funcwrapper


def logs_manager(message: str = "") -> object:
    def funcwrapper(func) -> object:
        def argswrapper(*args, **kwargs) -> object:
            info(f'Job {message} on thread {get_ident()} started.')
            return func(*args, **kwargs)
        info(f'Job {message} on thread {get_ident()} ended.')
        return argswrapper
    return funcwrapper


def get_memory_usage(obj: object, seen: set = set()) -> int:
    """Gets recursively the size of an object

    Args:
        obj (object): the object we want to compute memory size.
        seen (set, optional): Keeps ids of already computed objects. Defaults to empty set.

    Returns:
        int: size of the object in bytes
    """

    size: int = getsizeof(obj)

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum([get_memory_usage(v, seen) for v in obj.values()])
        size += sum([get_memory_usage(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_memory_usage(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_memory_usage(i, seen) for i in obj])

    return size
