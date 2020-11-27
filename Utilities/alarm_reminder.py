import time
import winsound
from win10toast import ToastNotifier

def timer ( message, minutes ):
    notificator = ToastNotifier()
    notificator.show_toast( "Alarm", 
                            f"Alarm will go off in {minutes} minutes...",
                            duration=50 ) 
    time.sleep( minutes * 60 )
    notificator.show_toast( f"Alarm", message, duration=50 )

    #Alarm sound
    frequency = 2000 #Hz
    duration = 1000 # 1 sec
    winsound.Beep( frequency, duration )

if __name__ == "__main__":
    print("\n Enter something to be displayed about: ")
    message = input( ">> ")
    print(" \n Enter minutes for the alarm: ")
    minutes = int( input( ">>" ) )
    timer( message, minutes )
