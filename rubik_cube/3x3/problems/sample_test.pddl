(define
    (problem sample_test)
    (:domain cube3)
    (:objects Y W B G O R)
    (:init

(cube1 O G Y)
(cube2 O W B)
(cube3 G Y R)
(cube4 B Y R)
(cube5 B Y O)
(cube6 B R W)
(cube7 G W R)
(cube8 W O G)
(edge12 Y B)
(edge13 O Y)
(edge15 W B)
(edge24 G O)
(edge26 O B)
(edge34 Y R)
(edge37 Y G)
(edge48 W O)
(edge56 R W)
(edge57 R B)
(edge68 W G)
(edge78 G R)


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