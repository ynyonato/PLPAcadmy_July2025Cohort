document.addEventListener("DOMContentLoaded", () => {

  // Variables and DOM elements
  let darkMode = false;

  const darkModeBtn = document.getElementById("toggleDarkModeBtn");
  const card = document.querySelector(".card");
  const popup = document.getElementById("popup");
  const popupCloseBtn = document.getElementById("popupCloseBtn");

  const startBtn = document.getElementById("startBtn");
  const status = document.getElementById("statusMsg");
  const showPopupBtn = document.getElementById("showPopupBtn");

  // Function to toggle dark/light mode
  function toggleDarkMode() {
    darkMode = !darkMode;
    document.body.classList.toggle("dark-mode", darkMode);
    return darkMode;
  }

  // Function to flip the card
  function flipCard(cardElement) {
    cardElement.classList.toggle("flipped");
  }

  // Show popup with loading animation running for 3 seconds
  function showPopup(message) {
    popup.classList.add("show");
    status.textContent = message;
    startBtn.classList.add("loading");

    // Stop loading animation after 3 seconds
    setTimeout(() => {
      startBtn.classList.remove("loading");
      status.textContent = '😊😊😊😊     😊😊😊😊😊    😊😊😊😊';

    }, 3000);
  }

  // Event Listeners
  darkModeBtn.addEventListener("click", () => {
    const isDark = toggleDarkMode();
    console.log("Dark mode is ON:", isDark);
  });

  card.addEventListener("click", () => {
    flipCard(card);
  });

  showPopupBtn.addEventListener("click", () => {
    showPopup("Loading the show ...");
  });

  popupCloseBtn.addEventListener("click", () => {
    popup.classList.remove("show");
    startBtn.classList.remove("loading");
    status.textContent = "";
  });

  // Example log for square of 5
  function square(num) {
    return num * num;
  }
  console.log("Square of 5 is", square(5));
});
