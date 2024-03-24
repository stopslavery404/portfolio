

// Function to load JSON data from a file
function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'projects.json', true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == 200) {
            callback(JSON.parse(xobj.responseText));
        }
    };
    xobj.send(null);
}

// Function to display JSON data in HTML
function displayData(data) {
    var jsonDisplay = document.getElementById('jsonDisplay');
    var html = '<pre>' + JSON.stringify(data, null, 4) + '</pre>';
    jsonDisplay.innerHTML = html;
}

// Load JSON data and display it
loadJSON(displayData);
