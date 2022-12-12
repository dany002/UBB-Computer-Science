;11. Return the level (and coresponded list of nodes) with maximum number of nodes for a tree of type (2).
;The level of the root element is 0.

; get_left(l1..ln) = { null, n = 0
;                    { l2, if l2 is list 
;                    { null, otherwise

(defun get_left(tree)
    (cond 
        ((null tree) nil)
        ((listp (cadr tree)) (cadr tree))
        (t nil)
    )
)

; get_right(l1...ln) = get_left(l2...ln)

(defun get_right(tree)
    (get_left (cdr tree))
)


;get_nodes_from_level(l1...ln, lvl) = { null, if n = 0
;                                     { [l1], if lvl = 0
;                                     { append(get_nodes_from_level(get_left(l1...ln), lvl-1), get_nodes_from_level(get_right(l1...ln),lvl-1)) , if lvl > 0


(defun get_nodes_from_level(tree lvl)
    (cond
        ((null tree) nil)
        ((eq lvl 0) (list (car tree)))
        ((> lvl 0) (append (get_nodes_from_level (get_left tree) (- lvl 1)) (get_nodes_from_level (get_right tree) (- lvl 1))))
    )
)

; get_number_of_levels(l1...ln) = { null, if n = 0
;                                 { 1 + max(get_number_of_levels(get_left(l1...ln)), get_number_of_levels(get_right(l1...ln))), otherwise.

(defun get_number_of_levels (tree)
    (cond
        ((null tree) 0)
        (t (+ 1(max (get_number_of_levels (get_left tree)) (get_number_of_levels (get_right tree)))))
    )
)

; count_nodes(l1...ln, lvls) = { max(length(get_nodes_from_level(l1...ln, lvls)), count_nodes(l1...ln, lvls-1))  , if lvls > 0
;                              { 0, otherwise

(defun count_nodes (tree lvls)
    (cond
        ((< 0 lvls) (max (length (get_nodes_from_level tree lvls)) (count_nodes tree (- lvls 1))))
        (t 0)
    )
)

; wrapper(l1...ln, lev, levels) = { [get_nodes_from_level(l1...ln, levels), levels]    ,if levels > 0 and length(get_nodes_from_level(l1...ln, levels)) = lev
;                                 { wrapper(l1...ln, lev, levels - 1), otherwise


(defun wrapper (tree lev levls)
    (cond
        ((and (< 0 levls) (eq (length (get_nodes_from_level tree levls)) lev)) (list (get_nodes_from_level tree levls) levls))
        (t (wrapper tree lev (- levls 1)))
    )
)

(defun solution (tree)
    (wrapper tree (count_nodes tree (get_number_of_levels tree)) (get_number_of_levels tree))
)

(print (solution '(1 (2 (4) (5)) (3 (6)))))

