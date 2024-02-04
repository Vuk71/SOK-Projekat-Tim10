$(document).ready(function() {
    // Kreiranje dijaloga
    var dialog = $("#dialog").dialog({
        autoOpen: false,
        modal: true,
        buttons: {
            Ok: function() {
                // Zatvaranje dijaloga
                $(this).dialog("close");
                $("#workspaceForm").submit();
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
                dialog.append('<div id="additionalFields"><input type="text" id="someInputField" name="someInputField" placeholder="Enter something"></div>');
            }
            if (selectedDataSource === 'test') {
                // Dodavanje dodatnih input polja u dijalog
                dialog.append('<div id="additionalFields"><input type="text" id="someInputField" name="someInputField" placeholder="Enter something"></div>');

            }
            if (selectedDataSource === 'Github Data Source') {
                // Dodavanje dodatnih input polja u dijalog
                dialog.append('<div id="additionalFields"><input type="text" id="someInputField" name="someInputField" placeholder="Enter something else"></div>');

            }
        });
    });
});

    // Funkcija za promenu workspace-a
function changeWorkspace(button, workspace) {
    var paragraph = document.getElementById('workspaceNumber');
    paragraph.textContent = "Selected workspace: " + workspace;

    var buttons = document.querySelectorAll('button');
    buttons.forEach(function(btn) {
        btn.classList.remove('selected');
    });

    button.classList.add('selected');
}