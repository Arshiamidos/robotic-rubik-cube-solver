final=["D'","D'"]+["U","U","U","B'","D","D","B","D","B'","D'","B","U'","U'","U'"]
break_points=[(2,2)]
config={

    (2,2):["R'","D'","D'","R"],

    ("F",(0,2)):["R'","D'","R"],
    ("L",(0,2)):["F'","D","F"],
    ("R",(0,0)):["F","D","F'"],
    
    ("F",(2,2)):["D'","R'","D","R"],
    ("F",(2,0)):["D","F","D","D","F'"],
    ("L",(2,2)):["R'","D","R"],
    ("L",(2,0)):["D"],
    ("R",(2,2)):["D'","D'","R'","D","D","R"],
    ("R",(2,0)):["D","F","D'","F'"],
    ("B",(2,2)):["D'","D'","R'","D","R"],
    ("B",(2,0)):["D","D","R'","D'","D'","R"],

    ("D",(0,0)):["D'","D'"]+final,
    ("D",(0,2)):["D"]+final,
    ("D",(2,0)):["D'"]+final,
    ("D",(2,2)):final,
}