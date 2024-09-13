    // JavaScript to toggle content based on dropdown selection
    document.getElementById('game-selector').addEventListener('change', function() {
        // Hide all content sections
        var contents = document.querySelectorAll('.tournament-content');
        contents.forEach(function(content) {
          content.classList.remove('active');
        });
  
        // Show the selected content
        var selectedGame = this.value;
        if (selectedGame) {
          document.getElementById(selectedGame).classList.add('active');
        }
      });