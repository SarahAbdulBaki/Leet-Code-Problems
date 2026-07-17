<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px;">

  <!-- Title Section -->
  <h1 style="border-bottom: none; font-size: 24px; font-weight: 600; margin-bottom: 8px; margin-top: 0;">
    860. Lemonade Change
  </h1>

 

  <!-- Problem Description -->
  <div style="font-size: 15px; margin-bottom: 24px;">
    <p style="margin-top: 0; margin-bottom: 12px;">At a lemonade stand, each lemonade costs <code>$5</code>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <code>$5</code>.</p>
    <p style="margin-bottom: 12px;">Note that you do not have any change in hand at first.</p>
    <p style="margin-bottom: 12px;">Given an integer array <code>bills</code> where <code>bills[i]</code> is the bill the <code>i<sup>th</sup></code> customer pays, return <code>true</code> if you can provide every customer with the correct change, or <code>false</code> otherwise.</p>
  </div>

  <!-- Example 1 -->
  <div style="margin-bottom: 20px;">
    <p style="font-weight: 600; font-size: 15px; margin-bottom: 8px;">Example 1:</p>
    <pre style="background-color: rgba(120, 120, 120, 0.05); border-left: 3px solid #00b8a3; padding: 12px; border-radius: 0 4px 4px 0; font-family: monospace; font-size: 13px; white-space: pre-wrap; margin: 0;">
<strong>Input:</strong> bills = [5,5,5,10,20]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.</pre>
  </div>

  <!-- Example 2 -->
  <div style="margin-bottom: 24px;">
    <p style="font-weight: 600; font-size: 15px; margin-bottom: 8px;">Example 2:</p>
    <pre style="background-color: rgba(120, 120, 120, 0.05); border-left: 3px solid #00b8a3; padding: 12px; border-radius: 0 4px 4px 0; font-family: monospace; font-size: 13px; white-space: pre-wrap; margin: 0;">
<strong>Input:</strong> bills = [5,5,10,10,20]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.</pre>
  </div>

  <!-- Constraints -->
  <div style="border-top: 1px solid rgba(120, 120, 120, 0.15); padding-top: 16px;">
    <p style="font-weight: 600; font-size: 15px; margin-top: 0; margin-bottom: 8px;">Constraints:</p>
    <ul style="margin: 0; padding-left: 20px; font-size: 14px;">
      <li style="margin-bottom: 6px;"><code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code></li>
      <li style="margin-bottom: 0;"><code>bills[i]</code> is either <code>5</code>, <code>10</code>, or <code>20</code>.</li>
    </ul>
  </div>

</div>
