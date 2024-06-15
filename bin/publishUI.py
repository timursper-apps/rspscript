import publish

print("Введите название файла (file.rsp)")
fileName = input()
print("Введите директорию, где находится файл (dir/rasp/rasp.rsp)")
dirFile = input()
publish.upload(fileName, dirFile)