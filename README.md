## Project # 2
## Advanced Cryptography

In this project we want to program Time-Memory Tradeoff attack (as discussed in class, see Martin Hellman's paper):

    Pre-computation: Precompute a table using SHA256 as the underlying function we aim to invert, this includes selection of the random starting points, computation of the chains, and sorting the table (SP_i, EP_i) for i=1..N, w.r.t. to the endpoints EP_i.
    Online Attack: Given a hash finds its pre-image by repeatedly using the table. You are encouraged to use the distinguished point technique to speed up the checks. 

To keep your implementation simple you do not have to implement Rainbow tables, i.e. instead you may use the same function across your chains and ignore overlaps in the chains.

Since we cannot really precompute a significant portion of the space for 256 bit output of the SHA256 function we create a new function f to invert by taking a small number, e.g. first k bits of the output of SHA256, i.e. fk(x) = SHA(x) mod 2k.

There are three parameters we wish to invert: 

a) 16-bits (toy problem) fix the function f to the first 2 bytes of the SHA256 output (truncate the remaining bits).

b) 20-bits (this is getting interesting) fix the function f to the first 20 bits of the SHA256 output (truncate the remaining bits).

c) 24-bits (requires some effort) fix the function f to the first 3 bytes of the SHA256 output (truncate the remaining bits).

You may use any programing language but you are encouraged to use Python which has libraries for SHA256 and built-in support for sorting (an alternative is to use EP's in dictionary object and then just check if an entry for the EP exists in the dictionary).

Turn in your code along with an example for each of the three cases i.e. pick random output y (of the right size) and compute input x using the table you have precomputed such that f(x) = y. 
