from comby import Comby

def rewriting():
    comby = Comby()

    file_name = input("Введите имя файла, в котором хотите поменять участок кода:\n")
    with open(file_name, 'r', encoding='utf-8') as f:
        source_old = f.read()

    label = input("Введите заголовок блока, в котором хотите поменять участок кода:\n")
    match_target = input("Введите участок кода, который хотите поменять:\n")
    rewrite_target = input("Введите новый участок кода:\n")

    match = ("%s{:[2]%s:[3]}" % (label, match_target))[1:]
    rewrite = ("%s{:[2]%s:[3]}" % (label, rewrite_target))[1:]
    source_new = comby.rewrite(source_old, match, rewrite)

    improved_file = open('new_' + file_name, "w")
    improved_file.write(source_new)
    improved_file.close()

    return source_new

print(rewriting())