goal=(1,3)
redirect_possible=[(4,6),(4,8),(1,3),(1,5),(4,0)]
mut_points={
    (1,5):[ "D", "B", "D'", "B'", "D'", "L'", "D", "L"],
    (4,0):[ "D", "B", "D'", "B'", "D'", "L'", "D", "L"],
    (4,8):[ "D", "R", "D'", "R'", "D'", "B'", "D", "B"],
    (1,3):[ "D", "R", "D'", "R'", "D'", "B'", "D", "B"],
}
mut=["D","L","D'","L'","D'","F'","D","F"]+\
    ["D","B","D'","B'","D'","L'","D","L"]+\
    ["D","R","D'","R'","D'","B'","D","B"]+\
    ["D","F","D'","F'","D'","R'","D","R"]

final=["B'" ,"D" ,"B" ,"D" ,"R" ,"D'", "R'"]
d_link_mut={
    (3,4):["D","D"]+final,
    (4,3):["D'"]+final,
    (4,5):["D"]+final,
    (5,4):[]+final,  
}
surf=["D", "R", "D'", "R'", "D'", "B'", "D", "B"]
middle_corner={
    (2,4):[]+surf,
    (5,1):["D'"]+surf,
    (5,7):["D"]+surf,
    (8,4):["D","D"]+surf,
}