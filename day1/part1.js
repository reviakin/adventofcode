document.body.textContent
  .split("\n")
  .filter(Boolean)
  .map(Number)
  .filter((x, _, xs) => xs.find((y) => y === 2020 - x))
  .reduce((a, b) => a * b);
