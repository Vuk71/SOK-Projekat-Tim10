// JavaScript code for application logic and user interactions
// ...

function clean() {
    $.ajax({
        url: '/clean/', // URL endpoint za ažuriranje aktivnog workspace-a
        type: 'POST',
        dataType: 'json',
        success: function(response) {
            console.log(response); // Ispisujemo odgovor u konzoli radi provere

            if (response.success) {
                // Ako je uspešno, izvršite redirekciju na novu stranicu
                window.location.href = '';
            } else {
                console.error('Error: Response does not indicate success');
            }
        },
        error: function(error) {
            console.error('Error:', error); // Ako dođe do greške, ispisujemo je u konzoli
        }
    });
}

function filter() {
    filterQuery = document.getElementById('filterInput').value;

    $.ajax({
        url: '/filter/', // URL endpoint za ažuriranje aktivnog workspace-a
        type: 'POST',
        data: {
            query: filterQuery
        },
        dataType: 'json',
        success: function(response) {
            console.log(response); // Ispisujemo odgovor u konzoli radi provere

            if (response.success) {
                // Ako je uspešno, izvršite redirekciju na novu stranicu
                document.getElementById("filterInput").value = "";
                window.location.href = '';
            } else {
                console.error('Error: Response does not indicate success');
            }
        },
        error: function(error) {
            console.error('Error:', error); // Ako dođe do greške, ispisujemo je u konzoli
        }
    });
}

function search() {
    searchQuery = document.getElementById('searchInput').value;

    $.ajax({
        url: '/search/', // URL endpoint za ažuriranje aktivnog workspace-a
        type: 'POST',
        data: {
            query: searchQuery
        },
        dataType: 'json',
        success: function(response) {
            console.log(response); // Ispisujemo odgovor u konzoli radi provere

            if (response.success) {
                // Ako je uspešno, izvršite redirekciju na novu stranicu
                document.getElementById("searchInput").value = "";
                window.location.href = '';
            } else {
                console.error('Error: Response does not indicate success');
            }
        },
        error: function(error) {
            console.error('Error:', error); // Ako dođe do greške, ispisujemo je u konzoli
        }
    });
}