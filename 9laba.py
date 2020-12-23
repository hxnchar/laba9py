def getString():
    myStr = input("Input your string!")
    return myStr

def sortString(myStr):
    return ''.join(sorted(myStr))

def output(myStr):
    count=0
    string = str(myStr)
    for i in range(0,len(myStr)):##0...len
        count += 1
        if i==len(myStr)-1:
            print(f"{string[i]}: {count}")
        elif string[i] != string[i+1]:
                print(f"{string[i]}: {count}")
                count = 0

myStr = getString()
print(f"Отсортировано по алфавиту {sortString(myStr)}, длина строки - {len(myStr)}")
output(sortString(myStr))