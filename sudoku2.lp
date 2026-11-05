% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Give each cell exactly one number from 1 to 9
1 { sudoku(X,Y,N) : N = 1..9 } 1 :- X = 1..9, Y = 1..9.

% Keep the numbers that are already given in the puzzle
:- initial(X,Y,N), not sudoku(X,Y,N).

% A number cannot appear more than once in the same row
:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 != Y2.

% A number cannot appear more than once in the same column
:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 != X2.

% Number cannot appear more than once in a single subgrid
:- sudoku(X1,Y1,N), sudoku(X2,Y2,N), subgrid(X1,Y1,G), subgrid(X2,Y2,G), X1 != X2.

% Assign each cell to a 3x3 subgrid
subgrid(X,Y,G) :- X = 1..9, Y = 1..9, G = 1 + (((X-1)/3)*3 + (Y-1)/3).

#show sudoku/3.
% 1C only needs to contain statement of form #show sudoku/3  #show subgrid/3.