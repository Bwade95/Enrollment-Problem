import address, student, teacher
from datetime import date

def main():
    students = [[student.Student("Brandon", "Wade", date(1995,7,26), "07979525311", \
        [address.Address("United Kingdom","Hertfordshire","Waltham Cross", \
        "98 Leaforis Road", "EN7 6NF"), address.Address("United Kingdom", "Hertfordshire", "Waltham Cross", "7 Wellers Grove", "EN7 6HU")], \
        False)]]

main()
