function Player(firstName, lastName) {

	var self = this;

	self.firstName 	= firstName;
	self.lastName 	= lastName;
}

function loadPlayers() {
	/*var data = JSON.parse("../json/players.json");
	console.log("data");*/

	var input, file, fr;

    if (typeof window.FileReader !== 'function') {
      	alert("The file API isn't supported on this browser yet.");
      	return;
    }

    else {

      fr = new FileReader();
      fr.onload = receivedText;
      fr.readAsText("../json/players.json");
    }

    function receivedText(e) {
      lines = e.target.result;
      var newArr = JSON.parse(lines); 
    }

}

/*function savePlayerFile() {

	var file = new Blob([text], {type: 'text/plain'});


	// savePlayerDetails();
}

function download(text, name, type) {
    var a = document.createElement("a");
    var file = new Blob([text], {type: type});
    a.href = URL.createObjectURL(file);
    document.querySelector("#players").appendChild(a);
    a.download = name;
    a.click();
}

function savePlayerDetails() {
	var playerTest = new Player("Benjamin", "Morvan");

	var object = JSON.parse(JSON.stringify(playerTest));
	console.log(object);

	var object2 = new Player("Benjamin", "Morvan");

	object2 = JSON.stringify(object2);
	console.log(object2);

	download(object2, 'test.json', 'text/plain');


}*/

