# Built-in class attributes
class Student:

    def __init__( self, name, id, age ):
        self.name = name
        self.id = id
        self.age = age
    
    def display_details( self ):
        print( f"Name:{ self.name }, ID:{ self.id }, AGE:{self.age}")

s = Student( "Babar", 1, 70 )
print( s.__doc__ )
print( s.__dict__ )
print( s.__module__)