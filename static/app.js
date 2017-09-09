// ********** EXAMPLE ********** //

function Task(data) {
    /*this.id = ko.observable(data.id);
    this.title = ko.observable(data.title);
    this.description = ko.observable(data.description);*/
}

function TaskListViewModel() {
    /*var self = this;
    self.tasks = ko.observableArray([]);
    self.newTaskTitle = ko.observable();
    self.newTaskDesc = ko.observable();

    self.addTask = function() {
	self.save();
	self.newTaskTitle("");
	self.newTaskDesc("");
    };

    $.getJSON('/tasks', function(taskModels) {
	var t = $.map(taskModels.tasks, function(item) {
	    return new Task(item);
	});
	self.tasks(t);
    });

    self.save = function() {
	return $.ajax({
	    url: '/tasks/new',
	    contentType: 'application/json',
	    type: 'POST',
	    data: JSON.stringify({
		'title': self.newTaskTitle(),
		'description': self.newTaskDesc()
	    }),
	    success: function(data) {
		console.log("Pushing to tasks array");
		self.tasks.push(new Task({ title: data.title, description: data.description, id: data.id}));
		return;
	    },
	    error: function() {
		return console.log("Failed");
	    }
	});
    };*/
}

// ko.applyBindings(new TaskListViewModel());

// ********** MODEL ********** //

function Player(data) {

    this.firstName 	= ko.observable(data.firstName);
    this.lastName 	= ko.observable(data.lastName);
    this.sex 		= ko.observable(data.sex);
    this.stableford = ko.observable(data.stableford);

}

function PlayerListViewModel() {

	// ViewModel
    var self 				= this;
    self.players 			= ko.observableArray([]);
    /*self.newPlayer = {
    	firstName 	: ko.observable(),
    	lastName 	: ko.observable(),
    	sex 		: ko.observable(),
    	stableford 	: ko.observable()
    };*/
    self.newPlayerFirstName = ko.observable();
    self.newPlayerLastName = ko.observable();
    self.newPlayerSex = ko.observable();
    self.newPlayerStableford = ko.observable();

    // Add player
    self.addPlayer = function() {
		console.log("add caca");
    	// Ajax request
		self.save();

		/*self.newPlayer.firstName("");
		self.newPlayer.lastName("");
		self.newPlayer.sex("");
		self.newPlayer.stableford("");*/

		self.newPlayerFirstName("");
	    self.newPlayerLastName("");
	    self.newPlayerSex("");
	    self.newPlayerStableford("");


    };

    // Get players
    $.getJSON('/players', function(playerListModel) {
		var t = $.map(playerListModel.players, function(item) {
		    return new Player(item);
		});
		self.players(t);
    });

    self.save = function() {
		return $.ajax({
		    url			: '/players/new',
		    contentType	: 'application/json',
		    type 		: 'POST',
		    /*data 		: JSON.stringify({
				'player': self.newPlayerFirstName()
		    }),*/
			data : JSON.stringify({
				'firstName': self.newPlayerFirstName(),
				'lastName': self.newPlayerLastName(),
				'sex': self.newPlayerSex(),
				'stableford': self.newPlayerStableford()
			}),
		    success: function(data) {
				console.log("Pushing to tasks array");
				self.players.push(new Player({
					firstname	: data.firstName,
					lastname	: data.lastName,
					sex			: data.sex,
					stableford	: data.stableford
				}));
				return;
		    },
		    error: function() {
				return console.log("Failed");
		    }
		});
    };

}

// Apply bindings
ko.applyBindings(new PlayerListViewModel());