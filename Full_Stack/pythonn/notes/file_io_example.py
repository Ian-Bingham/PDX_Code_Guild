# # file_io_example.py 6/22/18
#
# # Old convention to open files
# # Must explicitly call open and close
# file = open("sample.txt")
# 
# # text = file.read()
# # print(text)
#
# file.seek(0)
# text_lines = file.readlines()
# for line in text_lines:
#     print(line, end='')
#
# file.close()
#
# # New convention to open files
# # Both opens and closes the file
# with open("sample.txt") as file:
#     text = file.read()
#     file.seek(0)
#     text_lines = file.readlines()
#
# print(text)
# print(text_lines)
#
# # write to a file then read it back
# with open("sample.txt", 'a') as f:
#     f.write("Some words")
#
# with open("sample.txt") as f:
#     print(f.read())
#
# def list_creator(list_items, type='ul'):
#     lst = ''
#     for item in list_items:
#         lst += '<li>{}</li>'.format(item)
#     return '<{type}>{lst}</{type}>'.format(type=type, lst=lst)
#
# items = ['cats', 'dogs', 'ferret']
#
# with open('new.html', 'w') as f:
#     f.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body>{}</body></html>'.format(list_creator(items, 'ol')))
