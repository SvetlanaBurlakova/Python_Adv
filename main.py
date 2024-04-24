# from Seminars.Seminar6 import ex2
from Seminars.Seminar6 import guess_number
from HomeWorks import HW7
from pathlib import Path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HW7.ex7.sort_files(Path('dir'))
    HW7.group_files_rename(Path('dir'), end_file='_file_',digits=3,
                       extention_before='rnd', extention_after='doc',
                       name_range=[3, 6])






