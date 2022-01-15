table_rows = []
for i in range(2,11):
    for j in range(1,11):
        table_rows.append(i*j)
print(table_rows) 
print('\n'*2 +'********* Result *********' +'\n'*2) 
for num in range(0,10):
    print(table_rows[num::10])

    #REDO