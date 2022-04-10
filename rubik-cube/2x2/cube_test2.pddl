(define
    (problem cube_test)
    (:domain cube)
    (:objects Y W B G O R)
    (:init
        (cube1 B O Y)
        (cube2 G R W)
        (cube3 O G W)
        (cube4 Y O G)
        (cube5 R B W)
        (cube6 W O B)
        (cube7 R Y G)
        (cube8 Y B R)
    )
    (:goal
        (and
            (cube1 R W B)
            (cube2 O W B)
            (cube3 R Y B)
            (cube4 O Y B)
            (cube5 R W G)
            (cube6 O W G)
            (cube7 R Y G)
            (cube8 O Y G)
        )
    )
)