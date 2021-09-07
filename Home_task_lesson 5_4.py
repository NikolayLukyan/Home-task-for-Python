our_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("my_text_3.txt", "w", encoding="utf-8") as my_f:
    with open("my_text_4.txt", encoding="utf-8") as my_new:
        my_f.writelines([line.replace(line.split()[0], our_dic.get(line.split()[0])) for line in my_new])
