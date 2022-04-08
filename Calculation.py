def EndGrade(Note, Credits):
    print("Before the new exam" + "\n ")
    print((2.7*5*2+2.7*6+3.3*5+3.7*5+3.0*6+3*8)/(26+6+8))
    print("\n")
    print("After the new exam" + "\n ")
    print(((2.7*5*2+2.7*6+3.3*5+3.7*5+2.3*6+2*6+1.7*10)+Note*Credits)/(26+6+Credits+6+10))

EndGrade(2.3,5)