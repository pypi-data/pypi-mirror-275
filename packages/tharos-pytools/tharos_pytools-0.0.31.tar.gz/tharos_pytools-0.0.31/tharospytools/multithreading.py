"Tools to handle multithreading"
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from typing import Callable
from collections.abc import Iterable
from functools import partial
try:
    from resource import setrlimit, getrlimit, RLIMIT_AS
    from psutil import virtual_memory
except ImportError:
    mem_status: bool = False
    print(OSError('W - Could not use memorylock on this platform'))
else:
    mem_status: bool = True


def futures_collector(
    func: Callable,
        argslist: list,
        kwargslist: list[dict] | None = None,
        num_processes: int = cpu_count(),
        memory: float | None = None
) -> list:
    """
    Spawns len(arglist) instances of func and executes them at num_processes instances at time.

    * func : a function
    * argslist (list): a list of tuples, arguments of each func
    * kwargslist (list[dict]) a list of dicts, kwargs for each func
    * num_processes (int) : max number of concurrent instances.
        Default : number of available logic cores
    * memory (float|None) : ratio of memory to be used, ranging from .05 to .95. Will not work if *resource* is incompatible.
    """
    def limit_memory(ratio: float = 0.8) -> None:
        """Defines a lock over used memory

        Args:
            ratio (float, optional): Ranging from .05 to .95, maximum ratio of memory to be used by the Python process. Defaults to 0.8.
        """
        if ratio > .95:
            ratio = .95
        elif ratio < .05:
            ratio = .05
        try:
            memory_lock = int(virtual_memory().total * ratio)
            _, hard = getrlimit(RLIMIT_AS)
            setrlimit(RLIMIT_AS, (memory_lock, hard))
        except ModuleNotFoundError as exc:
            raise OSError(
                "Module resource is either non-installed or environnement is incompatible. Aborting.") from exc

    if memory is not None and mem_status:
        limit_memory(memory)
    if kwargslist is None or len(kwargslist) == len(argslist):
        with ThreadPoolExecutor(max_workers=num_processes) as executor:
            futures = [
                executor.submit(
                    func,
                    *args if isinstance(args, Iterable) else args
                ) if kwargslist is None else
                executor.submit(
                    func,
                    *args if isinstance(args, Iterable) else args,
                    **kwargslist[i]
                ) for i, args in enumerate(argslist)
            ]
        return [f.result() for f in futures]
    else:
        raise ValueError(
            f"""Positionnal argument list length ({len(argslist)})
            does not match keywords argument list length ({len(kwargslist)}).""")


def objects_collector(
    obj: object,
        kwargslist: list[dict],
        num_processes: int = cpu_count(),
        memory: float | None = None
) -> list:
    """
    Spawns len(arglist) instances of func and executes them at num_processes instances at time.

    * obj : a type
    * argslist (list): a list of tuples, arguments of each func
    * kwargslist (list[dict]) a list of dicts, kwargs for each func
    * num_processes (int) : max number of concurrent instances.
        Default : number of available logic cores
    * memory (float|None) : ratio of memory to be used, ranging from .05 to .95. Will not work if *resource* is incompatible.
    """
    def limit_memory(ratio: float = 0.8) -> None:
        """Defines a lock over used memory

        Args:
            ratio (float, optional): Ranging from .05 to .95, maximum ratio of memory to be used by the Python process. Defaults to 0.8.
        """
        if ratio > .95:
            ratio = .95
        elif ratio < .05:
            ratio = .05
        try:
            memory_lock = int(virtual_memory().total * ratio)
            _, hard = getrlimit(RLIMIT_AS)
            setrlimit(RLIMIT_AS, (memory_lock, hard))
        except ModuleNotFoundError as exc:
            raise OSError(
                "Module resource is either non-installed or environnement is incompatible. Aborting.") from exc

    if memory is not None and mem_status:
        limit_memory(memory)

    with ThreadPoolExecutor(max_workers=num_processes) as executor:
        futures = [
            executor.submit(
                partial,
                obj.__init__,
                *kwargs
            ) for kwargs in kwargslist
        ]
    return [f.result() for f in futures]


class Test():

    def __init__(self, x: int) -> None:
        self.a = x


if __name__ == "__main__":
    liste = objects_collector(
        Test,
        kwargslist=[[i] for i in range(3)],
    )
    for obj in liste:
        print(obj.x)
