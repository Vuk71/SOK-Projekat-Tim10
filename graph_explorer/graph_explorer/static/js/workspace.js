
    // Funkcija za promenu workspace-a
function changeWorkspace(button, workspace) {

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
            console.log(response); // Ispisujemo odgovor u konzoli radi provere

        // Ažuriramo podatke na stranici
            $('#dataParagraph').text(response.data);
        },
        error: function(error) {
            console.error('Error:', error); // Ako dođe do greške, ispisujemo je u konzoli
        }
    });
}

$(document).ready(function() {

    $('#workspaceForm').submit(function(event) {

        event.preventDefault(); // Spriječava podnošenje forme putem uobičajenog postupka



        var selectedWorkspace = $('.selected').text().replace('Workspace ', ''); // Dohvaća odabrani workspace

        var paragraph = $('#workspaceNumber');
        paragraph.text("Selected workspace: " + selectedWorkspace);

        // Serijalizirajte podatke iz forme
        var formData = $(this).serialize();

        // Dodajte dodatne parametre, ako je potrebno
        formData += '&active_workspace=' + selectedWorkspace;

        // Slanje AJAX zahteva za ažuriranje aktivnog workspace-a
        $.ajax({
            url: '/add_workspace/', // URL endpoint za ažuriranje aktivnog workspace-a
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function(response) {
                console.log(response); // Ispisujemo odgovor u konzoli radi provere

                // Ažuriramo podatke na stranici
                $('#dataParagraph').text(response.data);

                var buttons = document.querySelectorAll('.button');

                var newWorkspace = buttons[buttons.length - 2];

                newWorkspace.classList.add('selected');
            },
            error: function(error) {
                console.error('Error:', error); // Ako dođe do greške, ispisujemo je u konzoli
            }
        });

        return false; // Spriječava preusmjeravanje na drugu stranicu

    });


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

                    param3 = $('#param3').val();
                    $("#param3Field").val(param3);

                    param4 = $('#param4').val();
                    $("#param4Field").val(param4);

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
            $('.additionalFields').remove();

            if (selectedDataSource === 'default') {
                // Dodavanje dodatnih input polja u dijalog
            }
            if (selectedDataSource === 'Github Data Source') {
                // Dodavanje dodatnih input polja u dijalog
                dialog.append('<div class="additionalFields"><input type="text" id="param1" name="git repo" placeholder="enter git repo"></div>');
            }
            if (selectedDataSource === 'Instagram Data Source') {
                // Dodavanje dodatnih input polja u dijalog
                dialog.append('<div class="additionalFields"><input type="text" id="param1" name="instagram profile" placeholder="instagram profile"></div>');
                dialog.append('<div class="additionalFields"><input type="text" id="param2" name="width" placeholder="enter width (default 5)"></div>');
                dialog.append('<div class="additionalFields"><input type="text" id="param3" name="username" placeholder="enter username (optional)"></div>');
                dialog.append('<div class="additionalFields"><input type="text" id="param4" name="password" placeholder="enter password (optional)"></div>');
            }
            if (selectedDataSource == 'JSON Parser Data Source') {
                dialog.append('<div class="additionalFields"><input type="text" id="param1" name="json file path" placeholder="enter json file path"></div>');
            }
        });
    });
});
