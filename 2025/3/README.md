<h2 >Part 1 Description</h2>
<details closed>
<p>There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from <code>1</code> to <code>9</code>. You make a note of their joltage ratings (your puzzle input). For example:</p>
<pre><code>987654321111111
811111111111119
234234234234278
818181911112111
</code></pre>
<p>The batteries are arranged into <em>banks</em>; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on <em>exactly two</em> batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like <code>12345</code> and you turn on batteries <code>2</code> and <code>4</code>, the bank would produce <code>24</code> jolts. (You cannot rearrange batteries.)</p>
<p>You'll need to find the largest possible joltage each bank can produce. In the above example:</p>
<ul>
<li>In <code><em>98</em>7654321111111</code>, you can make the largest joltage possible, <em><code>98</code></em>, by turning on the first two batteries.</li>
<li>In <code><em>8</em>1111111111111<em>9</em></code>, you can make the largest joltage possible by turning on the batteries labeled <code>8</code> and <code>9</code>, producing <em><code>89</code></em> jolts.</li>
<li>In <code>2342342342342<em>78</em></code>, you can make <em><code>78</code></em> by turning on the last two batteries (marked <code>7</code> and <code>8</code>).</li>
<li>In <code>818181<em>9</em>1111<em>2</em>111</code>, the largest joltage you can produce is <em><code>92</code></em>.</li>
</ul>
<p>The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is <code>98</code> + <code>89</code> + <code>78</code> + <code>92</code> = <code><em>357</em></code>.</p>
</details>


<h2>Part 2 Description</h2>
<details closed>
<p>Now, you need to make the largest joltage by turning on <em>exactly twelve</em> batteries within each bank.</p>
<p>The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be <code><em>12</em></code> digits in each bank's joltage output instead of two.</p>
<p>Consider again the example from before:</p>
<pre><code>987654321111111
811111111111119
234234234234278
818181911112111
</code></pre>
<p>Now, the joltages are much larger:</p>
<ul>
<li>In <code><em>987654321111</em>111</code>, the largest joltage can be found by turning on everything except some <code>1</code>s at the end to produce <code><em>987654321111</em></code>.</li>
<li>In the digit sequence <code><em>81111111111</em>111<em>9</em></code>, the largest joltage can be found by turning on everything except some <code>1</code>s, producing <code><em>811111111119</em></code>.</li>
<li>In <code>23<em>4</em>2<em>34234234278</em></code>, the largest joltage can be found by turning on everything except a <code>2</code> battery, a <code>3</code> battery, and another <code>2</code> battery near the start to produce <code><em>434234234278</em></code>.</li>
<li>In <code><em>8</em>1<em>8</em>1<em>8</em>1<em>911112111</em></code>, the joltage <code><em>888911112111</em></code> is produced by turning on everything except some <code>1</code>s near the front.</li>
</ul>
<p>The total output joltage is now much larger: <code>987654321111</code> + <code>811111111119</code> + <code>434234234278</code> + <code>888911112111</code> = <code><em>3121910778619</em></code>.</p>
</details>
