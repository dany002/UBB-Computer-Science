% Model matematic:
% nrPrim(n, div) =
% 	true, n < 3 && n > 1
% 	true, n % div != 0 and div >= n / 2
% 	nrPrim(n, div + 1), n % div != 0 and div < n / 2
% 	false, otherwise

% nrPrim(N:number, Div:number)
% flow model: nrPrim(i, i)

nrPrim(N, _) :- 
    N > 1,
    N =< 3.
nrPrim(N, Div) :- N mod Div =\= 0,
    Div >= N / 2, !.
nrPrim(N, Div) :- N mod Div =\= 0,
    NDiv is Div + 1,
    nrPrim(N, NDiv).


%Model matematic:
% remove_non_primes(l1...ln) =
%	[], n = 0
%	l1 + remove_non_primes(l2...ln), if l1 is prime ( nrPrim(l1,2) = True )
%	remove_non_primes(l2...ln), if l1 is not prime ( nrPrim(l1,2) = False ) / Otherwise.

%remove_non_primes(L: list, R: list)
%flow model: remove_non_primes(i,o)

remove_non_primes([],[]):-
    !.
remove_non_primes([H|T], [H|R]) :-
    nrPrim(H, 2),!,
    remove_non_primes(T,R).
remove_non_primes([_|T], R) :-
    remove_non_primes(T, R).
