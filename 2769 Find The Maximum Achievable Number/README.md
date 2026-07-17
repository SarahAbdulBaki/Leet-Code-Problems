<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px;">

  <!-- Title Section -->
  <h1 style="border-bottom: none; font-size: 24px; font-weight: 600; margin-bottom: 8px; margin-top: 0;">
    2769. Find the Maximum Achievable Number
  </h1>

  <!-- Problem Description -->
  <div style="font-size: 15px; margin-bottom: 24px;">
    <p style="margin-top: 0; margin-bottom: 12px;">Given two integers, <code>num</code> and <code>t</code>. A number <code>x</code> is achievable if it can become equal to <code>num</code> after applying the following operation at most <code>t</code> times:</p>
    <p style="margin-bottom: 12px; padding-left: 15px; border-left: 2px solid rgba(120, 120, 120, 0.3);">Increase or decrease <code>x</code> by 1, and simultaneously increase or decrease <code>num</code> by 1.</p>
    <p style="margin-bottom: 12px;">Return the <em>maximum possible value</em> of <code>x</code>.</p>
  </div>

  <!-- Example 1 -->
  <div style="margin-bottom: 20px;">
    <p style="font-weight: 600; font-size: 15px; margin-bottom: 8px;">Example 1:</p>
    <pre style="background-color: rgba(120, 120, 120, 0.05); border-left: 3px solid #00b8a3; padding: 12px; border-radius: 0 4px 4px 0; font-family: monospace; font-size: 13px; white-space: pre-wrap; margin: 0;">
<strong>Input:</strong> num = 4, t = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
Apply the following operation once to make the maximum achievable number equal to num:
Decrease the maximum achievable number by 1, and increase num by 1.</pre>
  </div>

  <!-- Example 2 -->
  <div style="margin-bottom: 24px;">
    <p style="font-weight: 600; font-size: 15px; margin-bottom: 8px;">Example 2:</p>
    <pre style="background-color: rgba(120, 120, 120, 0.05); border-left: 3px solid #00b8a3; padding: 12px; border-radius: 0 4px 4px 0; font-family: monospace; font-size: 13px; white-space: pre-wrap; margin: 0;">
<strong>Input:</strong> num = 3, t = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
Apply the following operation twice to make the maximum achievable number equal to num:
Decrease the maximum achievable number by 1, and increase num by 1.</pre>
  </div>

  <!-- Constraints -->
  <div style="border-top: 1px solid rgba(120, 120, 120, 0.15); padding-top: 16px;">
    <p style="font-weight: 600; font-size: 15px; margin-top: 0; margin-bottom: 8px;">Constraints:</p>
    <ul style="margin: 0; padding-left: 20px; font-size: 14px;">
      <li style="margin-bottom: 0;"><code>1 &lt;= num, t &lt;= 50</code></li>
    </ul>
  </div>

</div>
