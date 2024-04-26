"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
from pathlib import Path

EXTENTIONS = {'txt':'text', 'doc': 'text','jpg': 'picture', 'png': 'picture'}

def sort_files(directory:Path):
    for r in directory.iterdir():
        if r.is_file():
            file, extention = r.name, r.suffix
            if extention[1:] in EXTENTIONS:
                new_dir = EXTENTIONS[extention[1:]]
                if not Path(new_dir).is_dir() or not Path(new_dir):
                    Path(new_dir).mkdir()
                Path.replace(r, (Path.cwd() / new_dir / file))


if __name__ == '__main__':
    sort_files(Path('dir'))
