(define
    (domain cube)
    (:requirements :strips :adl :typing :conditional-effects )
    (:predicates
        (cube1 ?x ?y ?z)
        (cube2 ?x ?y ?z)
        (cube3 ?x ?y ?z)
        (cube4 ?x ?y ?z)
        (cube5 ?x ?y ?z)
        (cube6 ?x ?y ?z)
        (cube7 ?x ?y ?z)
        (cube8 ?x ?y ?z)
    )

    (:action U
    :parameters ()
    :precondition (and)
    :effect
        (and
            (forall (?x ?y ?z) (when (cube5 ?x ?y ?z) (and (not (cube5 ?x ?y ?z)) (cube7 ?y ?x ?z))))
            (forall (?x ?y ?z) (when (cube7 ?x ?y ?z) (and (not (cube7 ?x ?y ?z)) (cube8 ?y ?x ?z))))
            (forall (?x ?y ?z) (when (cube8 ?x ?y ?z) (and (not (cube8 ?x ?y ?z)) (cube6 ?y ?x ?z))))
            (forall (?x ?y ?z) (when (cube6 ?x ?y ?z) (and (not (cube6 ?x ?y ?z)) (cube5 ?y ?x ?z))))
        )
    )

    (:action Urev
    :parameters ()
    :precondition (and)
    :effect
        (and
            (forall (?x ?y ?z) (when (cube5 ?x ?y ?z) (and (not (cube5 ?x ?y ?z)) (cube6 ?y ?x ?z))))
            (forall (?x ?y ?z) (when (cube6 ?x ?y ?z) (and (not (cube6 ?x ?y ?z)) (cube8 ?y ?x ?z))))
            (forall (?x ?y ?z) (when (cube8 ?x ?y ?z) (and (not (cube8 ?x ?y ?z)) (cube7 ?y ?x ?z))))
            (forall (?x ?y ?z) (when (cube7 ?x ?y ?z) (and (not (cube7 ?x ?y ?z)) (cube5 ?y ?x ?z))))
            
        )
    )

    ; (:action D
    ; :parameters ()
    ; :precondition (and)
    ; :effect
    ;     (and
    ;         (forall (?x ?y ?z) (when (cube1 ?x ?y ?z) (and (not (cube1 ?x ?y ?z)) (cube3 ?y ?x ?z))))
    ;         (forall (?x ?y ?z) (when (cube3 ?x ?y ?z) (and (not (cube3 ?x ?y ?z)) (cube4 ?y ?x ?z))))
    ;         (forall (?x ?y ?z) (when (cube4 ?x ?y ?z) (and (not (cube4 ?x ?y ?z)) (cube2 ?y ?x ?z))))
    ;         (forall (?x ?y ?z) (when (cube2 ?x ?y ?z) (and (not (cube2 ?x ?y ?z)) (cube1 ?y ?x ?z))))
    ;     )
    ; )

    ; (:action Drev
    ; :parameters ()
    ; :precondition (and)
    ; :effect
    ;     (and
    ;         (forall (?x ?y ?z) (when (cube1 ?x ?y ?z) (and (not (cube1 ?x ?y ?z)) (cube2 ?y ?x ?z))))
    ;         (forall (?x ?y ?z) (when (cube3 ?x ?y ?z) (and (not (cube3 ?x ?y ?z)) (cube1 ?y ?x ?z))))
    ;         (forall (?x ?y ?z) (when (cube4 ?x ?y ?z) (and (not (cube4 ?x ?y ?z)) (cube3 ?y ?x ?z))))
    ;         (forall (?x ?y ?z) (when (cube2 ?x ?y ?z) (and (not (cube2 ?x ?y ?z)) (cube4 ?y ?x ?z))))
    ;     )
    ; )

    (:action R
    :parameters ()
    :precondition (and)
    :effect
        (and
            (forall (?x ?y ?z) (when (cube2 ?x ?y ?z) (and (not (cube2 ?x ?y ?z)) (cube6 ?x ?z ?y))))
            (forall (?x ?y ?z) (when (cube6 ?x ?y ?z) (and (not (cube6 ?x ?y ?z)) (cube8 ?x ?z ?y))))
            (forall (?x ?y ?z) (when (cube8 ?x ?y ?z) (and (not (cube8 ?x ?y ?z)) (cube4 ?x ?z ?y))))
            (forall (?x ?y ?z) (when (cube4 ?x ?y ?z) (and (not (cube4 ?x ?y ?z)) (cube2 ?x ?z ?y))))
        )
    )

    (:action Rrev
    :parameters ()
    :precondition (and)
    :effect
        (and
            (forall (?x ?y ?z) (when (cube2 ?x ?y ?z) (and (not (cube2 ?x ?y ?z)) (cube4 ?x ?z ?y))))
            (forall (?x ?y ?z) (when (cube4 ?x ?y ?z) (and (not (cube4 ?x ?y ?z)) (cube8 ?x ?z ?y))))
            (forall (?x ?y ?z) (when (cube8 ?x ?y ?z) (and (not (cube8 ?x ?y ?z)) (cube6 ?x ?z ?y))))
            (forall (?x ?y ?z) (when (cube6 ?x ?y ?z) (and (not (cube6 ?x ?y ?z)) (cube2 ?x ?z ?y))))
        )
    )

    ; (:action L
    ; :parameters ()
    ; :precondition (and)
    ; :effect
    ;     (and
    ;         (forall (?x ?y ?z) (when (cube1 ?x ?y ?z) (and (not (cube1 ?x ?y ?z)) (cube5 ?x ?z ?y))))
    ;         (forall (?x ?y ?z) (when (cube5 ?x ?y ?z) (and (not (cube5 ?x ?y ?z)) (cube7 ?x ?z ?y))))
    ;         (forall (?x ?y ?z) (when (cube7 ?x ?y ?z) (and (not (cube7 ?x ?y ?z)) (cube3 ?x ?z ?y))))
    ;         (forall (?x ?y ?z) (when (cube3 ?x ?y ?z) (and (not (cube3 ?x ?y ?z)) (cube1 ?x ?z ?y))))
    ;     )
    ; )

    ; (:action Lrev
    ; :parameters ()
    ; :precondition (and)
    ; :effect
    ;     (and
    ;         (forall (?x ?y ?z) (when (cube1 ?x ?y ?z) (and (not (cube1 ?x ?y ?z)) (cube3 ?x ?z ?y))))
    ;         (forall (?x ?y ?z) (when (cube5 ?x ?y ?z) (and (not (cube5 ?x ?y ?z)) (cube1 ?x ?z ?y))))
    ;         (forall (?x ?y ?z) (when (cube7 ?x ?y ?z) (and (not (cube7 ?x ?y ?z)) (cube5 ?x ?z ?y))))
    ;         (forall (?x ?y ?z) (when (cube3 ?x ?y ?z) (and (not (cube3 ?x ?y ?z)) (cube7 ?x ?z ?y))))
    ;     )
    ; )

    (:action F
    :parameters ()
    :precondition (and)
    :effect
        (and
            (forall (?x ?y ?z) (when (cube1 ?x ?y ?z) (and (not (cube1 ?x ?y ?z)) (cube5 ?z ?y ?x) )))
            (forall (?x ?y ?z) (when (cube5 ?x ?y ?z) (and (not (cube5 ?x ?y ?z)) (cube6 ?z ?y ?x) )))
            (forall (?x ?y ?z) (when (cube6 ?x ?y ?z) (and (not (cube6 ?x ?y ?z)) (cube2 ?z ?y ?x) )))
            (forall (?x ?y ?z) (when (cube2 ?x ?y ?z) (and (not (cube2 ?x ?y ?z)) (cube1 ?z ?y ?x) )))
        )
    )

    (:action Frev
    :parameters ()
    :precondition (and)
    :effect
        (and
            (forall (?x ?y ?z) (when (cube1 ?x ?y ?z) (and (not (cube1 ?x ?y ?z)) (cube2 ?z ?y ?x) )))
            (forall (?x ?y ?z) (when (cube2 ?x ?y ?z) (and (not (cube2 ?x ?y ?z)) (cube6 ?z ?y ?x) )))
            (forall (?x ?y ?z) (when (cube6 ?x ?y ?z) (and (not (cube6 ?x ?y ?z)) (cube5 ?z ?y ?x) )))
            (forall (?x ?y ?z) (when (cube5 ?x ?y ?z) (and (not (cube5 ?x ?y ?z)) (cube1 ?z ?y ?x) )))
        )
    )

    ; (:action B
    ; :parameters ()
    ; :precondition (and)
    ; :effect
    ;     (and
    ;         (forall (?x ?y ?z) (when (cube3 ?x ?y ?z) (and (not (cube3 ?x ?y ?z)) (cube7 ?z ?y ?x) )))
    ;         (forall (?x ?y ?z) (when (cube7 ?x ?y ?z) (and (not (cube7 ?x ?y ?z)) (cube8 ?z ?y ?x) )))
    ;         (forall (?x ?y ?z) (when (cube8 ?x ?y ?z) (and (not (cube8 ?x ?y ?z)) (cube4 ?z ?y ?x) )))
    ;         (forall (?x ?y ?z) (when (cube4 ?x ?y ?z) (and (not (cube4 ?x ?y ?z)) (cube3 ?z ?y ?x) )))
    ;     )
    ; )

    ; (:action Brev
    ; :parameters ()
    ; :precondition (and)
    ; :effect
    ;     (and
    ;         (forall (?x ?y ?z) (when (cube3 ?x ?y ?z) (and (not (cube3 ?x ?y ?z)) (cube4 ?z ?y ?x) )))
    ;         (forall (?x ?y ?z) (when (cube7 ?x ?y ?z) (and (not (cube7 ?x ?y ?z)) (cube3 ?z ?y ?x) )))
    ;         (forall (?x ?y ?z) (when (cube8 ?x ?y ?z) (and (not (cube8 ?x ?y ?z)) (cube7 ?z ?y ?x) )))
    ;         (forall (?x ?y ?z) (when (cube4 ?x ?y ?z) (and (not (cube4 ?x ?y ?z)) (cube8 ?z ?y ?x) )))
    ;     )
    ; )

)