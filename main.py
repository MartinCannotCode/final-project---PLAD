import SW1_no1
import SW1_no2
import SW1_no3
import SW1_no4
import SW2_no1
import SW2_no2
import SW2_no3
import SW2_no4

no1 = 1
no2 = 2
no3 = 3
no4 = 4
no5 = 5
no6 = 6
no7 = 7
no8 = 8
quit = 9

def main():
    choice = 0
    while choice != quit:   
        menu()
        choice = int(input(""))
        if choice == no1:
            SW1_no1.one()
        elif choice == no2:
            SW1_no2.two()
        elif choice == no3:
            SW1_no3.three()
        elif choice == no4:
            SW1_no4.four()
        elif choice == no5:
            SW2_no1.five()
        elif choice == no6:
            SW2_no2.six()
        elif choice == no7:
            SW2_no3.seven()
        elif choice == no8:
            SW2_no4.eight()
        elif choice == quit:
            print("Quitting the program.")
        else:
            print("Invalid selection. Just enter numbers 1-9.")
        

     
    
def menu():
     print("My program can execute any problem code you choose below.")
     print("1. Problem no.1 from seatwork#1")
     print("2. Problem no.2 from seatwork#1")
     print("3. Problem no.3 from seatwork#1")
     print("4. Problem no.4 from seatwork#1")
     print("5. Problem no.1 from seatwork#2")
     print("6. Problem no.2 from seatwork#2")
     print("7. Problem no.3 from seatwork#2")
     print("8. Problem no.4 from seatwork#2")
     print("9. Quit the program")
     print("Just enter your choice(1-9): ")
     
main()