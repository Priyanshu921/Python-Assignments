detail=input("Enter the name of the students along with marks").split(',')
theory=int(detail[1])+int(detail[2])+int(detail[3])+int(detail[4])+int(detail[5])
practical=int(detail[6])+int(detail[7])+int(detail[8])
print(detail[0],'obtained',theory,'out of 500 in theory and ',practical,'out of 90 in practical and successfully passed the exam with',round((float(theory+practical)*100/590),2),'% agrregate, Many Congratulations to',detail[0])
