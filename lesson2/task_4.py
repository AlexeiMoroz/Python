#������������ ������ ������ �� ���������� ����, ���������� ���������.
#������� ������ ����� � ����� ������. ������ ����� �������������.
#���� ����� �������, �������� ������ ������ 10 ���� � �����.

words = input("input some words")
splitted_words = words.split()
strNum = 0
for el in splitted_words:
    strNum += 1
    print (f"{strNum}. {el[:10]}")