<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 700px; margin: 20px auto; padding: 20px; border: 1px solid #e1e4e8; border-radius: 8px; line-height: 1.6; color: #24292e;">
  
  <!-- Title & Difficulty -->
  <h1 style="margin-top: 0; font-size: 24px; border-bottom: 1px solid #eaecef; padding-bottom: 8px;">
    <a href="https://leetcode.com/problems/roman-to-integer/" target="_blank" style="color: #0366d6; text-decoration: none;">13. Roman to Integer</a>
  </h1>
  <p style="margin: 10px 0;"><strong>Difficulty:</strong> <span style="background-color: #e7f4e4; color: #2cbb5d; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 14px;">Easy</span></p>
  
  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Problem Description -->
  <h2>Problem Description</h2>
  <p>Roman numerals are represented by seven different symbols: <code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>
  
  <table style="border-collapse: collapse; width: 100%; max-width: 300px; margin: 15px 0; text-align: left;">
    <thead>
      <tr style="border-bottom: 2px solid #eaecef;">
        <th style="padding: 8px;">Symbol</th>
        <th style="padding: 8px;">Value</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">I</td>
        <td style="padding: 8px;">1</td>
      </tr>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">V</td>
        <td style="padding: 8px;">5</td>
      </tr>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">X</td>
        <td style="padding: 8px;">10</td>
      </tr>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">L</td>
        <td style="padding: 8px;">50</td>
      </tr>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">C</td>
        <td style="padding: 8px;">100</td>
      </tr>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">D</td>
        <td style="padding: 8px;">500</td>
      </tr>
      <tr style="border-bottom: 1px solid #eaecef;">
        <td style="padding: 8px; font-family: monospace;">M</td>
        <td style="padding: 8px;">1000</td>
      </tr>
    </tbody>
  </table>

  <p>For example, <code>2</code> is written as <code>II</code> in Roman numeral, just two ones added together. <code>12</code> is written as <code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>
  <p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>.</p>
  
  <p>There are six instances where subtraction is used:</p>
  <ul>
    <li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.</li>
    <li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.</li>
    <li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
  </ul>
  <p>Given a roman numeral, convert it to an integer.</p>

  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Examples -->
  <h2>Examples</h2>

  <!-- Example 1 -->
  <div style="margin-bottom: 20px;">
    <h4 style="margin-bottom: 5px;">Example 1:</h4>
    <pre style="background-color: #f6f8fa; padding: 12px; border-radius: 6px; font-family: monospace; overflow-x: auto; margin: 0;"><strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.</pre>
  </div>

  <!-- Example 2 -->
  <div style="margin-bottom: 20px;">
    <h4 style="margin-bottom: 5px;">Example 2:</h4>
    <pre style="background-color: #f6f8fa; padding: 12px; border-radius: 6px; font-family: monospace; overflow-x: auto; margin: 0;"><strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V = 5, III = 3.</pre>
  </div>

  <!-- Example 3 -->
  <div style="margin-bottom: 20px;">
    <h4 style="margin-bottom: 5px;">Example 3:</h4>
    <pre style="background-color: #f6f8fa; padding: 12px; border-radius: 6px; font-family: monospace; overflow-x: auto; margin: 0;"><strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90, and IV = 4.</pre>
  </div>

  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Constraints -->
  <h2>Constraints</h2>
  <ul>
    <li>1 &le; <code>s.length</code> &le; 15</li>
    <li><code>s</code> contains only the characters (<code>'I'</code>, <code>'V'</code>, <code>'X'</code>, <code>'L'</code>, <code>'C'</code>, <code>'D'</code>, <code>'M'</code>).</li>
    <li>It is guaranteed that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.</li>
  </ul>

</div>
