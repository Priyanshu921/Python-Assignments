def main():
    try:
        hours=int(input("Enter the number of hours worked:-"))
        pay=float(input("Enter the hourly pay:-"))
        gross_pay=hours*pay
        print('Gross Pay :${}'.format(gross_pay,'.2f'),sep='')
    except ValueError:
        print('ERROR:Hour Worked and Hourly Pay must')
        print('be valid numbers')
main()
