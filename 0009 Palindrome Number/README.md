<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 700px; margin: 20px auto; padding: 20px; border: 1px solid #e1e4e8; border-radius: 8px; line-height: 1.6; color: #24292e;">
  
  <!-- Title & Difficulty -->
  <h1 style="margin-top: 0; font-size: 24px; border-bottom: 1px solid #eaecef; padding-bottom: 8px;">
    <a href="https://leetcode.com/problems/palindrome-number/" target="_blank" style="color: #0366d6; text-decoration: none;">9. Palindrome Number</a>
  </h1>
  <p style="margin: 10px 0;"><strong>Difficulty:</strong> <span style="background-color: #e7f4e4; color: #2cbb5d; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 14px;">Easy</span></p>
  
  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Problem Description -->
  <h2>Problem Description</h2>
  <p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a <strong>palindrome</strong>, and <code>false</code> otherwise.</p>
  <p>An integer is a <strong>palindrome</strong> when it reads the same forward and backward.</p>
  <ul>
    <li>For example, <code>121</code> is a palindrome while <code>123</code> is not.</li>
  </ul>

  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Examples -->
  <h2>Examples</h2>

  <!-- Example 1 -->
  <div style="margin-bottom: 20px;">
    <h4 style="margin-bottom: 5px;">Example 1:</h4>
    <pre style="background-color: #f6f8fa; padding: 12px; border-radius: 6px; font-family: monospace; overflow-x: auto; margin: 0;"><strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.</pre>
  </div>

  <!-- Example 2 -->
  <div style="margin-bottom: 20px;">
    <h4 style="margin-bottom: 5px;">Example 2:</h4>
    <pre style="background-color: #f6f8fa; padding: 12px; border-radius: 6px; font-family: monospace; overflow-x: auto; margin: 0;"><strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.</pre>
  </div>

  <!-- Example 3 -->
  <div style="margin-bottom: 20px;">
    <h4 style="margin-bottom: 5px;">Example 3:</h4>
    <pre style="background-color: #f6f8fa; padding: 12px; border-radius: 6px; font-family: monospace; overflow-x: auto; margin: 0;"><strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.</pre>
  </div>

  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Constraints -->
  <h2>Constraints</h2>
  <ul>
    <li>-2<sup>31</sup> &le; <code>x</code> &le; 2<sup>31</sup> - 1</li>
  </ul>

  <hr style="border: 0; height: 1px; background: #eaecef; margin: 20px 0;" />

  <!-- Follow-up -->
  <h2>Follow-up</h2>
  <p>Can you solve it without converting the integer to a string?</p>

</div>
