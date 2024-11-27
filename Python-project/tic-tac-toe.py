L=[]
for i in range(3):
    A = input().split(" ")
    L.append(A)
if L[0][0]=="O" and L[0][1]=="O" and L[0][2]=="O" :
    print("Abhinav Wins")
elif L[1][0]=="O" and L[1][1]=="O" and L[1][2]=="O" :
    print("Abhinav Wins")
elif L[2][0]=="O" and L[2][1]=="O" and L[2][2]=="O" :
    print("Abhinav Wins")
elif L[0][0]=="O" and L[1][0]=="O" and L[2][0]=="O" :
    print("Abhinav Wins")
elif L[0][1]=="O" and L[1][1]=="O" and L[2][1]=="O" :
    print("Abhinav Wins")
elif L[0][2]=="O" and L[1][2]=="O" and L[2][2]=="O" :
    print("Abhinav Wins")
elif L[0][0]=="O" and L[1][1]=="O" and L[2][2]=="O" :
    print("Abhinav Wins")
elif L[0][2]=="O" and L[1][1]=="O" and L[2][0]=="O" :
    print("Abhinav Wins")
elif L[0][1]=="X" and L[0][1]=="X" and L[0][2]=="X" :
    print("Anjali Wins")
elif L[1][0]=="X" and L[1][1]=="X" and L[1][2]=="X" :
    print("Anjali Wins")
elif L[2][0]=="X" and L[2][1]=="X" and L[2][2]=="X" :
    print("Anjali Wins")
elif L[0][0]=="X" and L[1][0]=="X" and L[2][0]=="X" :
    print("Anjali Wins")
elif L[0][1]=="X" and L[1][1]=="X" and L[2][1]=="X" :
    print("Anjali Wins")
elif L[0][2]=="X" and L[0][2]=="X" and L[0][2]=="X" :
    print("Anjali Wins")
elif L[0][0]=="X" and L[1][1]=="X" and L[2][2]=="X" :
    print("Anjali Wins")
elif L[0][2]=="X" and L[1][1]=="X" and L[2][0]=="X" :
    print("Anjali Wins")
else:
    print("Tie")