(define
    (problem cube_test)
    (:domain cube)
    (:objects Y W B G O R)
    (:init
        (cube1 R W B)
        (cube2 O W B)
        (cube3 R Y B)
        (cube4 O Y B)
        (cube5 W O G)
        (cube6 Y O G)
        (cube7 W R G)
        (cube8 Y R G)
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