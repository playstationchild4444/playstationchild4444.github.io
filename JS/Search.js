function searchgames() {
    var input = document.getElementById('searchBar');
    var filter = input.value.toUpperCase();
    var games = document.getElementsByClassName('game-link');
    var i, txtValue;

    for (i = 0; i < games.length; i++) {
        txtValue = games[i].textContent || games[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            games[i].style.display = "";
        } else {
            games[i].style.display = "none";
        }
    }
}
