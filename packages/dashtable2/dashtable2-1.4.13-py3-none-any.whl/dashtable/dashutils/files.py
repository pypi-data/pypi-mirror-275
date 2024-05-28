
import os
from pathlib import Path
import shutil
import contextlib

from .aliases import PathLike


@contextlib.contextmanager
def umask_context(umask: int):
    """sets umask on operation and restores after"""
    old_umask = os.umask(umask)
    try:
        yield
    finally:
        os.umask(old_umask)


#region RM/TOUCH

def _mkdir(path: Path):
    with umask_context(0o002):
        path.mkdir(parents=True, exist_ok=True)


def mkparents(path: PathLike):
    """equals to mkdir -p $(dirname path)"""
    _mkdir(Path(path).parent)


def mkdir_of_file(file_path: PathLike):
    """
    для этого файла создаёт папку, в которой он должен лежать
    """
    mkparents(file_path)


def mkdir(path: PathLike):
    """mkdir with parents"""
    _mkdir(Path(path))


def touch(path: PathLike):
    """makes empty file, makes directories for this file automatically"""
    mkdir_of_file(path)
    Path(path).touch()


def rmdir(path: PathLike):
    """rm dir without errors"""
    shutil.rmtree(path, ignore_errors=True)


def copy_file(source: PathLike, dest: PathLike):
    """performs file copying with target directory auto creation"""
    mkdir_of_file(dest)
    shutil.copyfile(source, dest)


def move_file(source: PathLike, dest: PathLike):
    """performs file moving with target directory auto creation"""
    mkdir_of_file(dest)
    shutil.move(source, dest)


#endregion


def write_text(result_path: PathLike, text: str, encoding: str = 'utf-8'):
    mkdir_of_file(result_path)
    result_tmp = str(result_path) + '.tmp'
    Path(result_tmp).write_text(text, encoding=encoding, errors='ignore')
    if os.path.exists(result_path):
        os.remove(result_path)
    Path(result_tmp).rename(result_path)


def read_text(result_path: PathLike, encoding: str = 'utf-8'):
    return Path(result_path).read_text(encoding=encoding, errors='ignore')


def read_json(path: PathLike):
    import json
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_file(path: PathLike):

    s = Path(path).suffix
    if s == '.json':
        return read_json(path)
    if s == '.txt':
        return read_text(path)

    raise NotImplemented(f"no processing for ext {s} of file {path}")

