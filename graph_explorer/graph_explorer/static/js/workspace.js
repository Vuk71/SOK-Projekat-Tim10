
    // Funkcija za promenu workspace-a
function changeWorkspace(button, workspace) {
    var paragraph = document.getElementById('workspaceNumber');
    paragraph.textContent = "Selected workspace: " + workspace;

    var buttons = document.querySelectorAll('button');
    buttons.forEach(function(btn) {
        btn.classList.remove('selected');
    });

    button.classList.add('selected');

    // Slanje AJAX zahteva za ažuriranje aktivnog workspace-a
    $.ajax({
        url: '/update_active_workspace/', // URL endpoint za ažuriranje aktivnog workspace-a
        type: 'POST',
        data: {
            active_workspace: workspace // Šaljemo ID aktivnog workspace-a
        },
        dataType: 'json',
        success: function(response) {
            console.log(response); // Možemo ispisati odgovor u konzoli radi provere
            // Ovde možete dodati dodatnu logiku ako je potrebno
        },
        error: function(error) {
            console.error('Error:', error); // Ako dođe do greške, ispisujemo je u konzoli
        }
    });
}

$(document).ready(function() {
    // Kreiranje dijaloga
    var dialog = $("#dialog").dialog({
        autoOpen: false,
        modal: true,
        buttons: {
            Ok: function() {
                // Zatvaranje dijaloga

                selectedSource = $('#dataSourceSelect').val()

                if(selectedSource == "default"){
                    alert("Please select a valid data source.");
                }
                else{
                    $(this).dialog("close");
                    $("#dataSourceField").val(selectedSource);

                    param1 = $('#param1').val();
                    $("#param1Field").val(param1);

                    param2 = $('#param2').val();
                    $("#param2Field").val(param2);

                    $("#workspaceForm").submit();
                }


            },
            Cancel: function() {
                // Zatvaranje dijaloga
                $(this).dialog("close");
            }
        }
    });

    // Kada se klikne na dugme "Add Workspace"
    $("#addWorkspaceButton").click(function() {
        // Prikupljanje dostupnih data source-ova iz HTML-a
        var availableDataSources = JSON.parse($('#availableDataSources').val());

        // Kreiranje HTML stringa za opcije dijaloga
        var dialogOptions = "";
        dialogOptions += '<option value="' + "default"+ '">' + "select data source" + '</option>';
        availableDataSources.forEach(function(dataSource) {
            dialogOptions += '<option value="' + dataSource.id + '">' + dataSource.name + '</option>';
        });
        dialogOptions += '<option value="' + "test"+ '">' + "test opcija" + '</option>';

        // Postavljanje opcija u dijalog
        dialog.html('<p>Choose a data source:</p><select id="dataSourceSelect">' + dialogOptions + '</select>');

        // Otvaranje dijaloga
        dialog.dialog("open");

        // Event listener za promene u selektovanju data source-a
        $('#dataSourceSelect').change(function() {
            var selectedDataSource = $(this).val();
            // Ovde možete dodati logiku za dodavanje polja u dijalog
            // Na primer, ako izabrana opcija ima određene atribute ili karakteristike, dodajte odgovarajuća input polja
            // Npr. ako je selectedDataSource === 'neki_id', dodajte input polja u dijalog

            // Uklanjanje prethodno dodatih input polja iz dijaloga
            $('#additionalFields').remove();

            if (selectedDataSource === 'default') {
                // Dodavanje dodatnih input polja u dijalog
            }
            if (selectedDataSource === 'Github Data Source') {
                // Dodavanje dodatnih input polja u dijalog
                dialog.append('<div id="additionalParam1"><input type="text" id="param1" name="someInputField" placeholder="enter git repo"></div>');
                dialog.append('<div id="additionalParam2"><input type="hidden" id="param2" name="someInputField" placeholder="enter git repo"></div>');

            }
        });
    });
});