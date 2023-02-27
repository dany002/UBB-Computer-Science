; 15. Write a function that reverses a list together with all its sublists elements, at any level.

; myAppend(l1l2...ln, p1p2...pm) = 
; = p1p2...pm, if n = 0
; = {l1} U myAppend(l2...ln, p1p2...pm), otherwisw

(defun myAppend(l p)
  (cond
    ((null l) p)
    (t (cons (car l) (myAppend (cdr l) p)))
  )
)

; myReverse(l1l2...ln) = 
; = [], if n = 0
; = myAppend(myReverse(l2...ln), list(l1)), otherwise

(defun myReverse(l)
  (cond
    ((null l) nil)
    (t (myAppend (myReverse (cdr l)) (list (car l))))
  )
)

; myReverseMC(l) = 
; = l, if l is an atom
; = myReverseMC(l1) U myReverseMC(l2) U ... U myReverseMC(ln), otherwise (l = l1l2...ln)


(defun myReverseMC(l)
  (cond
    ((atom l) l)
    (t (mapcar #'myReverseMC (myReverse l)))
  )
)

(print ( myReverseMC '(1 2 (3 4 5) 6)))
