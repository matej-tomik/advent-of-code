<h2 >Part 1 Description</h2>
<details closed>
<p>The database operates on <em>ingredient IDs</em>. It consists of a list of <em>fresh ingredient ID ranges</em>, a blank line, and a list of <em>available ingredient IDs</em>. For example:</p>
<pre><code>3-5
10-14
16-20
12-18

1
5
8
11
17
32
</code></pre>
<p>The fresh ID ranges are <em>inclusive</em>: the range <code>3-5</code> means that ingredient IDs <code>3</code>, <code>4</code>, and <code>5</code> are all <em>fresh</em>. The ranges can also <em>overlap</em>; an ingredient ID is fresh if it is in <em>any</em> range.</p>
<p>The Elves are trying to determine which of the <em>available ingredient IDs</em> are <em>fresh</em>. In this example, this is done as follows:</p>
<ul>
<li>Ingredient ID <code>1</code> is spoiled because it does not fall into any range.</li>
<li>Ingredient ID <code>5</code> is <em>fresh</em> because it falls into range <code>3-5</code>.</li>
<li>Ingredient ID <code>8</code> is spoiled.</li>
<li>Ingredient ID <code>11</code> is <em>fresh</em> because it falls into range <code>10-14</code>.</li>
<li>Ingredient ID <code>17</code> is <em>fresh</em> because it falls into range <code>16-20</code> as well as range <code>12-18</code>.</li>
<li>Ingredient ID <code>32</code> is spoiled.</li>
</ul>
<p>So, in this example, <em><code>3</code></em> of the available ingredient IDs are fresh.</p>
<p>Process the database file from the new inventory management system. <em>How many of the available ingredient IDs are fresh?</em></p>
</details>


<h2>Part 2 Description</h2>
<details closed>
<p>Elves would like to know <em>all</em> of the IDs that the <em>fresh ingredient ID ranges</em> consider to be <em>fresh</em>. An ingredient ID is still considered fresh if it is in any range.</p>
<p>Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:</p>
<pre><code>3-5
10-14
16-20
12-18
</code></pre>
<p>The ingredient IDs that these ranges consider to be fresh are <code>3</code>, <code>4</code>, <code>5</code>, <code>10</code>, <code>11</code>, <code>12</code>, <code>13</code>, <code>14</code>, <code>15</code>, <code>16</code>, <code>17</code>, <code>18</code>, <code>19</code>, and <code>20</code>. So, in this example, the fresh ingredient ID ranges consider a total of <em><code>14</code></em> ingredient IDs to be fresh.</p>
<p>Process the database file again. <em>How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?</em></p>
</details>
