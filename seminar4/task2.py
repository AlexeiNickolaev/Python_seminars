# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def test_text(text):
    Uni_list = set()
    for i in text:
        # print(f'{i} = {ord(i)}')
        Uni_list.add(ord(i))
    return sorted(list(Uni_list), reverse=True)


text = 'HihiХихи'
print(test_text(text))
