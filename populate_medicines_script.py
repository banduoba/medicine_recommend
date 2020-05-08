# 添加和读取数据到数据库中
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicine.settings")

django.setup()
from user.models import Medicine, Tags

print('here')
Medicine.objects.all().delete()
Tags.objects.all().delete()


def populate_user():
    for category_dir in os.listdir('medicine_data'):
        if category_dir == '.DS_Store':
            continue
        tag, created = Tags.objects.get_or_create(name=category_dir)
        file_path = os.path.join('medicine_data', category_dir)
        if file_path == 'medicine_data/.DS_Store':
            continue
        for file in os.listdir(file_path):

            if file.endswith('.txt'):
                book_name = file.split('.')[0]
                print(file)
                book_description = open(os.path.join(file_path, file), 'r', encoding='gb18030').read()
                book_picture = book_name + '.jpg'
                print(book_name)
                medicine, _ = Medicine.objects.get_or_create(name=book_name, intro=book_description, pic=book_picture)
                medicine.tags.add(tag)


if __name__ == '__main__':
    populate_user()
