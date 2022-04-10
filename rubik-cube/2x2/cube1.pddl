(define
    (problem cube1)
    (:domain cube)
    (:objects Y W B G O R)
    (:init
        (cube1 Y R B)
        (cube2 O B Y)
        (cube3 B O W)
        (cube4 R G W)
        (cube5 O Y G)
        (cube6 B R W)
        (cube7 O W G)
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