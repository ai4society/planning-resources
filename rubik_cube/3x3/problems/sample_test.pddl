(define
    (problem cube_test3x3)
    (:domain cube3)
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

        (edge12 W B)
        (edge24 O W)
        (edge34 Y B)
        (edge13 R B)

        (edge15 R W)
        (edge26 W G)
        (edge48 O B)
        (edge37 R Y)

        (edge56 R G)
        (edge68 O Y)
        (edge78 O G)
        (edge57 Y G)
        
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

            (edge12 W B)
            (edge24 O B)
            (edge34 Y B)
            (edge13 R B)

            (edge15 R W)
            (edge26 O W)
            (edge48 O Y)
            (edge37 R Y)

            (edge56 W G)
            (edge68 O G)
            (edge78 Y G)
            (edge57 R G)
 
        )
    )
)