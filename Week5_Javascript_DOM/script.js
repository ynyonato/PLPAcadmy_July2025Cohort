// Javascript code for the assignment
// Part 1: Take user name and update header
const userName = prompt("What is your name?");
if (userName) {
  const header = document.querySelector(".page-header h1");
  header.textContent = `Welcome, ${userName}!`;
}

// Part 2: Functions
// Toggle visibility between article4 and article2
function toggleArticleVisibility() {
  const article2 = document.querySelector(".article2");
  const article4 = document.querySelector(".article4");
  if (article2.style.display === "none") {
    article2.style.display = "block";
    article4.style.display = "none";
  } else {
    article2.style.display = "none";
    article4.style.display = "block";
  }
}

// Change color of article titles to red
function changeTitlesColor() {
  const titles = document.querySelectorAll(".article h2");
  titles.forEach(title => {
    title.style.color = "red";
  });
}

// Part 3: Loop through all articles and display title and order in console
function logArticleTitles() {
  const articles = document.querySelectorAll(".article");
  articles.forEach((article, index) => {
    const title = article.querySelector("h2").textContent;
    console.log(`Article ${index + 1}: ${title}`);
  });
}

logArticleTitles();

// Part 4: When clicking "Articles" on nav bar, add paragraph to last article (.article4)
const navArticlesLink = document.querySelector(".nav-bar a:nth-child(2)");
navArticlesLink.addEventListener("click", event => {
  event.preventDefault();  // Prevent default navigation if any
  const article4 = document.querySelector(".article4");
  const newPara = document.createElement("p");
  newPara.textContent = "A new paragraph of my journey is being added.";
  article4.appendChild(newPara);
});
