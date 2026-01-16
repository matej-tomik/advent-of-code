<h2 >Part 1 Description</h2>
<details closed>
<p>The rolls of paper (<code>@</code>) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.</p>
<p>For example:</p>
<pre><code>..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
</code></pre>
<p>The forklifts can only access a roll of paper if there are <em>fewer than four rolls of paper</em> in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.</p>
<p>In this example, there are <code><em>13</em></code> rolls of paper that can be accessed by a forklift (marked with <code>x</code>):</p>
<pre><code>..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
</code></pre>
<p>Consider your complete diagram of the paper roll locations. <em>How many rolls of paper can be accessed by a forklift?</em></p>
</details>


<h2>Part 2 Description</h2>
<details closed>
<p>Once a roll of paper can be accessed by a forklift, it can be <em>removed</em>. Once a roll of paper is removed, the forklifts might be able to access <em>more</em> rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?</p>
<p>Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted <code><em>@</em></code> to indicate that a roll of paper is about to be removed, and using <code>x</code> to indicate that a roll of paper was just removed:</p>
<pre><code>Initial state:
..<em>@</em><em>@</em>.<em>@</em><em>@</em>@<em>@</em>.
<em>@</em>@@.@.@.@@
@@@@@.<em>@</em>.@@
@.@@@@..@.
<em>@</em>@.@@@@.@<em>@</em>
.@@@@@@@.@
.@.@.@.@@@
<em>@</em>.@@@.@@@@
.@@@@@@@@.
<em>@</em>.<em>@</em>.@@@.<em>@</em>.

Remove 13 rolls of paper:
..xx.xx<em>@</em>x.
x@@.<em>@</em>.<em>@</em>.@<em>@</em>
<em>@</em>@@@@.x.@@
<em>@</em>.@@@@..<em>@</em>.
x@.@@@@.<em>@</em>x
.<em>@</em>@@@@@@.<em>@</em>
.<em>@</em>.@.@.@@@
x.@@@.@@@@
.<em>@</em>@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.<em>@</em>@.x.x.<em>@</em>x
x@@@@...<em>@</em><em>@</em>
x.@@@@..x.
.<em>@</em>.@@@@.x.
.x@@@@@@.x
.x.@.@.@@<em>@</em>
..@@@.@@@@
.x<em>@</em>@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x<em>@</em>.....x.
.<em>@</em>@@@...xx
..@@@@....
.x.@@@@...
..<em>@</em>@@@@@..
...@.@.@@x
..<em>@</em>@@.@@@<em>@</em>
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x<em>@</em>@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@<em>@</em>.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..<em>@</em>@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...<em>@</em>@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x<em>@</em>.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...<em>@</em>@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
</code></pre>
<p>Stop once no more rolls of paper are accessible by a forklift. In this example, a total of <code><em>43</em></code> rolls of paper can be removed.</p>
<p>Start with your original diagram. <em>How many rolls of paper in total can be removed by the Elves and their forklifts?</em></p>
</details>
