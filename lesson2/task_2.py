#��� ������ ����������� ����� �������� �������� ���������.
#���������� ������������ �������� � ��������� 0 � 1, 2 � 3 � �. �.
#��� �������� ���������� ��������� ��������� ��������� �� ���� �����.
#��� ���������� ������ ��������� ����� ������������ ������� input().

el_list = list()
i = 0
while i < 5:
    new_el = input("input next element of list")
    el_list.append(new_el)
    i += 1

print(el_list)

for el in el_list:
    el_index = el_list.index(el)
    if el_index == len(el_list)-1:
        break
    elif el_index % 2 == 0:
        el_list[el_index], el_list[el_index + 1] = el_list[el_index + 1], el_list[el_index]
        continue

print(el_list)
