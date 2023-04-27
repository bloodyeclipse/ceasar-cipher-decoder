import string
 
 text= input ("Please  enter your text:")
 ROT =int(input("Please enter your ROT Key (put -1 for ATBASH):
"))
Flag = ""

for ch text:
  if ROT == -1:
     if ch.isalpha():
        flag +=
 string.ascii'_letters[25-(string.ascii_letters.index(ch))]
       else:
          flag += ch
       else:
         if ch.isalpha():
            flag +=
  string.ascii_letters[((string.ascii_letters.index(ch)+ ROT) % 26)]
             else:
               flag += ch
               
   print(f"your flag is {flag}")
           
