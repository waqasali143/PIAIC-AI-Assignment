EngMarks = int(input("Enter English Mark :"))
UrMarks = int(input("Enter Urdu Mark :"))
MthMarks = int(input("Enter Math Mark :"))
PhyMarks = int(input("Enter Physics Mark :"))
IslMarks = int(input("Enter Islamiat Mark :"))
print()
print(("*"*10,"MARK SHEET","*"*10),"\nSubject","\t Marks ","\t Obtain Marks ",
      "\nEnglish","\t100","\t\t\t",EngMarks,"\nUrdu","\t\t100",
      "\t\t\t",UrMarks,"\nMath","\t\t100","\t\t\t",MthMarks,
      "\nPhysics","\t100","\t\t\t",PhyMarks,"\nIslamiat","\t100","\t\t\t",IslMarks)
print()
TotMarks=500
ObtMarks=(EngMarks + UrMarks + MthMarks + PhyMarks + IslMarks)
print("Total Marks =",TotMarks, "\nObtain Marks =",ObtMarks)
print()
perc=(EngMarks + UrMarks + MthMarks + PhyMarks + IslMarks)/TotMarks*100

print("Percentage is ",perc,"%" )
if ObtMarks<200:
    print("Fail")
else:
    print("Pass")