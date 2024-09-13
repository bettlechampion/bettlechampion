
document.addEventListener('DOMContentLoaded', function() {
    
  // Update countdown every second

  // Function to calculate and update countdown
  function updateCountdown() {
    const countdowns = document.querySelectorAll('.countdown');
    
    countdowns.forEach(function(countdown) {
      const startTime = new Date(countdown.getAttribute('data-start')).getTime();
      const now = new Date().getTime();
      const distance = startTime - now;

      // Time calculations for days, hours, minutes, and seconds
      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((distance % (1000 * 60)) / 1000);

      if (distance > 0) {
        countdown.innerHTML = `<span> ${days}d </span> <span> ${hours}h </span> <span> ${minutes}m </span> <span> ${seconds}s </span>`;
      } else {
        countdown.innerHTML = "Tournament Finished";
      }
    });
  }

  setInterval(updateCountdown, 1000);
});