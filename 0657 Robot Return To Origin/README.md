<h1>657. Robot Return to Origin</h1>

<p>There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.</p>

<p>You are given a string <code>moves</code> that represents the move sequence of the robot where <code>moves[i]</code> represents its i<sup>th</sup> move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).</p>

<p>Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.</p>

<p>Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.</p>
 
<h3>Example 1:</h3>
<pre><code><strong>Input:</strong> moves = "UD"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.</code></pre>

<h3>Example 2:</h3>
<pre><code><strong>Input:</strong> moves = "LL"
<strong>Output:</strong> false
<strong>Explanation:</strong> The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.</code></pre>
 
<h3>Constraints:</h3>
<ul>
    <li><code>1 &lt;= moves.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>moves</code> only contains the characters 'U', 'D', 'L' and 'R'.</li>
</ul>
