#����������� ��������� ��������, �������������� ����� ����� ����������� �����, ������� �� ����������.
#� ������������ ����� ����������� ����� ������� ��������.
#���� � �������� ���������� �������� � ����������� ����������,
#�� ����� ������� � ��� �� ��������� ������ ������������ ����� ���.

rating_list = [7, 5, 3, 3, 2]
new_rating = int(input("input new rating"))
rating_position = 0

while True:
        try:
            rating_position = rating_list.index(new_rating, rating_position)
        except ValueError:
            if rating_position == 0:
                rating_position = len(rating_list)
                for el in rating_list:
                    if el < new_rating:
                        rating_position = rating_list.index(el)
                        break
            break
        else:
            rating_position += 1

rating_list.insert(rating_position, new_rating)
print(rating_list)
