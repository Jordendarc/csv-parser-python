import csv

file_csv = open('4912756030399420.csv', newline='')
reader = csv.reader(file_csv)
replacer = ",[]\"\""
first_list = []
duplicate_list = []
duplicate_amount = []
final_list = []
final_amount = []

for row in file_csv:
    if ',' in row:
        broken = row.partition(",")
        for i in range(0, len(broken)-1):
            line = broken[i]
            for y in replacer:
                line = line.replace(y,"")
            line = line.upper()
            first_list.append(line)
            # print(line)
    else:
        for p in replacer:
            row = row.replace(p,"")
        row = row.upper()
        first_list.append(row)
        # print(row)

for b in range(0, len(first_list)-1):
    if first_list[b] not in duplicate_list:
        duplicate_list.append(first_list[b])
        duplicate_amount.append(1)
    else:
        duplicate_amount[duplicate_list.index(first_list[b])] = duplicate_amount[duplicate_list.index(first_list[b])]+1

for b in range(0, len(duplicate_list)-1):
    if duplicate_amount[b] > 1:
        final_list.append(duplicate_list[b])
        final_amount.append(duplicate_amount[b])

print("There are a total of ", len(final_list))

new_csv = open('new_csv.csv', 'w')
writer = csv.writer(new_csv, delimiter=',', lineterminator='\n')

for b in range(0, len(final_list)-1):
    writer.writerow([final_list[b], final_amount[b]])

file_csv.close()
