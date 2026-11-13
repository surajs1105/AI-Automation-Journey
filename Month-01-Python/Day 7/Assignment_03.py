phy = float(input("Enter your physics marks: "))
chemistry = float(input("Enter your chemistry marks: "))    
math = float(input("Enter your math marks: "))
biology = float(input("Enter your biology marks: "))
english = float(input("Enter your english marks: "))  
total_marks = phy + chemistry + math + biology + english
percentage = (total_marks / 500) * 100  

if phy >= 40 and chemistry >= 40 and math >= 40 and biology >= 40 and english >= 40:
    print(f"Total Marks: {total_marks}\nPercentage: {percentage:.2f}%\nResult: Pass") 

else:
    print(f"Total Marks: {total_marks}\nPercentage: {percentage:.2f}%\nResult: Fail")
