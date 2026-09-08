# [(12011, 12013)]
#     12012: (5 digits long so the max dupe could only be 4)

#     [1] -- does 0 == 1..2..3..4..5?
#      0
#     [12] -- does 0,1 == 2,3? 
#      01
#     [120] -- 5 < 3*2 (digits in this sequence), no compare needed
#      012
#     [1201] -- 5 < 4*2, no compare needed
#      0123
#     [12012]-- 5 < 5*2, no compare needed (can last sequence always be ignored?)
#      01234
