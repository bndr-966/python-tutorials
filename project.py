myContact={"1111111111":{ "amal"},
"2222222222":{"mohamad"},
"3333333333":{"khalid"},
"4444444444":{"Abdullh"},
"5555555555":{"Rwan"},
"6666666666":{"Fasal"},
"7777777777":{"layla"}}


key=input("enter Contact Number : ")

if key in myContact:
    print (myContact[key])



elif not key.isdigit() or len(key) < 10 or len(key) > 10:
    
    print("this is invalid number")    


else:

    print("sorry, the number is not found ")    