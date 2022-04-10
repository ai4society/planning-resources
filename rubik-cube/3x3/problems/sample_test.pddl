(define
    (problem sample_test)
    (:domain cube3)
    (:objects Y W B G O R)
    (:init

(cube1 G Y O)
(cube2 B Y O)
(cube3 R G Y)
(cube4 O W G)
(cube5 Y B R)
(cube6 W B R)
(cube7 R G W)
(cube8 O W B)
(edge12 Y O)
(edge13 R Y)
(edge15 B W)
(edge24 O G)
(edge26 G W)
(edge34 Y B)
(edge37 R G)
(edge48 O W)
(edge56 B R)
(edge57 R W)
(edge68 O B)
(edge78 Y G)


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