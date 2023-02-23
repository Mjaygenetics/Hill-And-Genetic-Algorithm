# Hill-And-Genetic-Algorithm
A solution to the nxn queens problem using a hill climbing approach as well as a genetic algorithm approach
<h2>Board.py</h2>
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
