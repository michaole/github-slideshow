---
layout: slide
slide-id: code-animation
title: "Code Animation"
---

<div class="code-window">
  <div class="code-window-header">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-window-title">fibonacci.js</span>
  </div>
  <div class="code-window-body">
    <pre><code data-code-animate data-speed="40">// Calculate the Fibonacci sequence
function fibonacci(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

var results = [];
for (var i = 0; i &lt; 8; i++) {
  results.push(fibonacci(i));
}

console.log(results.join(", "));
// 0, 1, 1, 2, 3, 5, 8, 13</code></pre>
  </div>
</div>
