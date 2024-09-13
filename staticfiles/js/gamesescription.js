let popupInterval = setInterval(showPopup, 30000); // Show every 2 seconds
    
// Function to show the popup
function showPopup() {
    document.getElementById('join-popup').style.display = 'flex';
}

// Function to close the popup
function closePopup() {
    document.getElementById('join-popup').style.display = 'none';
}

// Optional: Auto-hide popup after 5 seconds
setTimeout(function() {
    clearInterval(popupInterval); // Stop showing after some time (optional)
}, 120000); 