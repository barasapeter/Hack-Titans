
const LIFE_QUOTES = [
  "The greatest glory in living lies not in never falling, but in rising every time we fall.",
  "The way to get started is to quit talking and begin doing.",
  "If life were predictable it would cease to be life, and be without flavor.",
  "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
  "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
];

const SUCCESS_QUOTES = [
  "Success is not final; failure is not fatal: It is the courage to continue that counts.",
  "Success usually comes to those who are too busy to be looking for it.",
  "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
  "Success is stumbling from failure to failure with no loss of enthusiasm.",
  "The road to success and the road to failure are almost exactly the same."
];

// Define the generateQuotes function
function generateQuotes(numQuotes, quoteType) {
  let quotes = quoteType === 'life' ? LIFE_QUOTES : SUCCESS_QUOTES;
  let generatedQuotes = new Set();
  let quoteList = document.getElementById('quote-list');
  quoteList.innerHTML = ''; // Clear the previous quotes

  while (generatedQuotes.size < numQuotes) {
    let randomIndex = Math.floor(Math.random() * quotes.length);
    let randomQuote = quotes[randomIndex];
    if (!generatedQuotes.has(randomQuote)) {
      generatedQuotes.add(randomQuote);
      let quoteItem = document.createElement('li');
      quoteItem.textContent = randomQuote;
      quoteList.appendChild(quoteItem);
    }
  }
}

// Add a click event listener to the generate button
let generateBtn = document.getElementById('generate-btn');
generateBtn.addEventListener('click', (event) => {
  let numQuotes = document.getElementById('num-quotes').value;
  let quoteType = document.getElementById('type-quotes').value;
  generateQuotes(numQuotes, quoteType);
});
