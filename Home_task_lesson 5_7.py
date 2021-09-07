import json

with open('my_first.json', 'w', encoding='utf-8') as w_file:
    with open('text_7.txt', encoding='utf-8') as my_best:
        prof = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_best}
        result = [prof, {'The average profit': round(sum([int(i) for i in prof.values() if int(i) > 0]) /
                                                     len([int(i) for i in prof.values() if int(i) > 0]))}]
    json.dump(result, w_file, ensure_ascii=False, indent=4)
