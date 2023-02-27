; 11.
; a) Determine the least common multiple of the numerical values of a nonlinear list.

; _lcm(a,b) = { a not number && b not number => nil
;             { a not number -> b
;             { b not number -> a
;             { (a*b)/gcd(a/b)

(defun _lcm (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        (T (/ (* a b) (_gcd a b)))
    )
)

; gcd(a,b) = { a not number && b not number -> nil
;            { a not number -> b
;            { b not number -> a
;            { a, if b = 0
;            { gcd(b,a%b), otherwise

(defun _gcd (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        ((equal b 0) a)
        (T (_gcd b (mod a b)))
    )
)

; list_gcd(l1...ln) = { l1, if l1 is atom and n = 1
;                     { lcm(list_gcd(l1),list_gcd(l2...ln)), if l1 is list
;                     { lcm(l1,list_gcd(l2...ln)), otherwise
; !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! TERMINAT list_gcd -> Modelul matematic !
(defun list_gcd (l)
    (cond
        ((and (atom (car l)) (null (cdr l))) (car l))
        ((listp (car l)) (_lcm (list_gcd (car l)) (list_gcd (cdr l))))
        (T (_lcm (car l) (list_gcd (cdr l))))
    )
)

(print (list_gcd '(24 ( 16 (12 A B)) 72)))
;=> 144


; b) Write a function to test if a linear list of numbers has a "mountain" aspect (a list has a "mountain"
; aspect if the items increase to a certain point and then decreases.
;  Eg. (10 18 29 17 11 10). The list must have at least 3 atoms to fullfil this criteria.

; _mountain(l1...ln, decreasing ) = 
;                     { true, if n = 1 && decreasing == nil
;                     { nil, l1 < l2 && decreasing == nil
;                     { _mountain(l2...ln, nil), if l1 > l2 and decreasing = true
;                     { true, mountain(l2...ln, decreasing)

(defun _mountain (l decreasing)
	(cond
		((= (list-length l) 1) (if decreasing nil T))
		((and (< (car l) (cadr l)) (not decreasing)) nil)
		((and (> (car l) (cadr l)) decreasing) (_mountain (cdr l) nil))
		(T (_mountain (cdr l) decreasing))
	)
)

; mountain(l1...ln) = { nil, n < 3
;                     { mountain(l1...ln, T)

(defun mountain (l)
	(if (< (list-length l) 3)
		nil
		(_mountain l T)
	)
)

(print (mountain '(10 18 29 17 11 10)))
; => T

(print (mountain '(10 18 29 17 11 29 10)))
;=> nil



; c) Remove all occurrences of a maximum numerical element from a nonlinear list.


; max_nb(a, b) = { a, a > b
;                { b, otherwise
(defun max_nb (a b)
    (if (> a b) a b)
)

; max_num(l1...ln) = { -1, if n = 0
;                    { l1, if n = 1 && l1 is number
;                    { max_nb(l1,max_num(l2...ln)), if l1 is number
;                    { max_nb(max_nb(l1,max_num(l2...ln))), if l1 is list
;                    { max_num(l2...ln), otherwise

(defun max_num (l)
    (cond
        ((null l) -1)
        ((and (null (cdr l)) (numberp (car l))) (car l))
        ((numberp (car l)) (max_nb (car l) (max_num (cdr l))))
        ((listp (car l)) (max_nb (max_num (car l)) (max_num (cdr l))))
        (t (max_num (cdr l)))
     )
)

(print (max_num '(1 2 (3 (a) (1 3)) 4 5)))

; => 5
; REMOVE THE MAXIMUM NUMBER DONT PRINT IT !!!!
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;remove_max(l1...ln, elem) = { [], if n = 0
;                            { remove_max(l2...ln, elem), if l1 = elem
;                            { l1 U remove_max(l2...ln, elem), otherwise


(defun remove_max(l elem)
  (cond
    ((null l) ())
    ((EQ (car l) elem) (remove_max ( cdr l ) elem))
    (T (cons (car l) (remove_max (cdr l) elem)))
  )
)

(print (remove_max '(1 2 (3 (a) (1 3)) 4 5) (max_num '(1 2 (3 (a) (1 3)) 4 5))))
;(print (remove_max '(1 2 (3 (a) (1 3)) 4 5) 5))



; d) Write a function which returns the product of numerical even atoms from a list, to any level.

; productL(l1..ln) =
;               { 1 if n =0
;               { l1 if n = 1 and l1 is even
;             = { l1 * productL(l2..ln) if l1 is number and even
;             = { productL(l1) * productL(l2..ln) if l1 is list
(defun productL (l)
    (cond
        ((null l) 1)
        ((and (= (length l) 1) ( = ( mod (car l) 2 ) 0)) (car l))
        ((and (numberp (car l)) (= (mod (car l) 2) 0)) (* (car l) (productL (cdr l))))
        ((listp (car l)) (* (productL (car l)) (productL (cdr l))))
        (t (productL (cdr l)))
    )
)

(print (productL '(1 2 3 (4 5 6) 7)))
(print ( productL '(6 2 3 15 4)))
;=> 48

; l2 -> ex 15
