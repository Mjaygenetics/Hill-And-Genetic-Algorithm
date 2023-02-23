# Hill-And-Genetic-Algorithm
A solution to the nxn queens problem using a hill climbing approach as well as a genetic algorithm approach
<h2>board.py</h2>
<h4>Python code that is used to create a board of nxn queen (1 = queen, 0 = empty space). Source code by Kate Nguyen.</h4>
<h5>get_fitness</h5>
<p>Returns the amount of queens that are in attacking positions</p>
<h5>show_map</h5>
<p>Prints out the map where 1's are queens and 0's are empty spaces</p>
<h5>flip</h5>
<p>Changes the 1's in a board to 0's and 0's to 1's</p>
<h2>hill.py</h2>
<h4>Python code that takes a board and calculates a global maximum solution to the nxn queens problem using local search</h4>
<h5>findQueen</h5>
<p>Searches a row in a board for a 1 value (queen)</p>
<h5>displayBoard</h5>
<p>Prints out the map where 1's remain as 1's but 0's are changed to ' - '</p>
<h5>localSearch</h5>
<p>Changes the position of a queen in each row and checks for the least attacking positions, loops n times until a global maximum is found</p>
<h2>genetic.py</h2>
<h5>findQueen</h5>
<p>Searches a row in a board for a 1 value (queen)</p>
<h5>nullBoard</h5>
<p>Creates a board object of size nxn where every index is 0</p>
<h5>findQueen</h5>
<p>Searches a row in a board for a 1 value (queen)</p>
<h5>conflictTotal</h5>
<p>Returns the total amount of attacking positions of a board object</p>
<h5>initialization</h5>
<p>Creates 8 boards and transfers each queen position in each board to a number that is added to a string</p>
<h5>selection</h5>
<p>Performs a random selection on each board string returned from initialization and returns a list of values corresponding to the random selection</p>
<h5>crossover</h5>
<p>Selects a random point in a board string and swaps components with another board string</p>
<h5>mutation</h5>
<p>Selects a random index in the board string and changes its value to a number between 0 and n</p>
<h5>specimens</h5>
<p>Converts the board strings back to a board and returns the board with the least amount of queens in attacking positions</p>
<h5>naturalSelection</h5>
<p>Loops the process of initialization, selection, crossover, mutation, and specimens until a board with 0 fitness (global maximum) is found</p>
<h5>displayBoard</h5>
<p>Prints out the map where 1's remain as 1's but 0's are changed to ' - '</p>
