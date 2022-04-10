(define
    (problem sample_test)
    (:domain cube3)
    (:objects Y W B G O R)
    (:init

(cube1 W B R)
(cube2 Y B R)
(cube3 W G R)
(cube4 Y G R)
(cube5 G W O)
(cube6 B W O)
(cube7 G Y O)
(cube8 B Y O)
(edge12 B R)
(edge13 W R)
(edge15 R Y)
(edge24 O B)
(edge26 B W)
(edge34 G R)
(edge37 G Y)
(edge48 B Y)
(edge56 W O)
(edge57 G O)
(edge68 Y O)
(edge78 G W)


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