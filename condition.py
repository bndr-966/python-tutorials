print('wellcome in my sampile project : ')

book_num={
'0581025151':{'Falah'},
'0500268893':{'Bander'},
'0553601466':{'Fahad'},
'0500615718':{'Mesfer'},
'0507630926':{'my number'}
}

enter=input('Please chose the process. create,' \
' read name, read number, update, or delete? ')

def create(number,name):
    if len(number)!=10 or not number.isdigit:
        print('this number is not corect')
        # return
    else:
        book_num[number]={name}
        print(book_num)
        # return

if (enter=='create'):
    input_num=input('enter any number you want add: ')
    input_name=input('enter any name you want add: ')
    create(input_num,input_name)
    # print(book_num)
