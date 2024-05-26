

from util import file_util


def test_loop_dir():

    file_util.loop_dir("/tmp", dirProcessFunc=lambda dir, sub_dir: print(f'process dir: dir={dir}, sub_dir={sub_dir}'), fileProcessFunc=lambda dir, file: print(f'process file: dir={dir}, file={file}'))