read_lines(Lines):-
  open('inputs/first.txt',read,Stream),
  read_file(Stream,Lines),
  close(Stream).

read_file(Stream,[]) :-
  at_end_of_stream(Stream).

read_file(Stream,[X|L]) :-
  \+ at_end_of_stream(Stream),
  read(Stream,X),
  read_file(Stream,L).


first_star(RESULT) :-
  read_lines(L),
  member(Y, L),
  member(X, L),
  2020 is X+Y,
  RESULT is X*Y.

second_star(RESULT) :-
  read_lines(L),
  member(Y, L),
  member(X, L),
  member(Z, L),
  2020 is X+Y+Z,
  RESULT is X*Y.
