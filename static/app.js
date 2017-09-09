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
				console.log("Pushing to players array");
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

function GolfCourseListViewModel() {

	// ViewModel
    var self 			= this;
    self.golfCourses 	= ko.observableArray([]);

    self.newGolfCourseName 	= ko.observable();
    self.newGolfCourseSlope = ko.observable();
    self.newGolfCourseSss 	= ko.observable();

    self.golfCourseHandicapHoles = ko.observableArray([]);

    

    self.newGolfCourseHandicapHole1 = ko.observable();
    self.newGolfCourseHandicapHole2 = ko.observable();
    self.newGolfCourseHandicapHole3 = ko.observable();
    self.newGolfCourseHandicapHole4 = ko.observable();
    self.newGolfCourseHandicapHole5 = ko.observable();
    self.newGolfCourseHandicapHole6 = ko.observable();
    self.newGolfCourseHandicapHole7 = ko.observable();
    self.newGolfCourseHandicapHole8 = ko.observable();
    self.newGolfCourseHandicapHole9 = ko.observable();
    self.newGolfCourseHandicapHole10 = ko.observable();
    self.newGolfCourseHandicapHole11 = ko.observable();
    self.newGolfCourseHandicapHole12 = ko.observable();
    self.newGolfCourseHandicapHole13 = ko.observable();
    self.newGolfCourseHandicapHole14 = ko.observable();
    self.newGolfCourseHandicapHole15 = ko.observable();
    self.newGolfCourseHandicapHole16 = ko.observable();
    self.newGolfCourseHandicapHole17 = ko.observable();
    self.newGolfCourseHandicapHole18 = ko.observable();

    var t = [
    	self.newGolfCourseHandicapHole1,
    	self.newGolfCourseHandicapHole2,
    	self.newGolfCourseHandicapHole3,
    	self.newGolfCourseHandicapHole4,
    	self.newGolfCourseHandicapHole5,
    	self.newGolfCourseHandicapHole6,
    	self.newGolfCourseHandicapHole7,
    	self.newGolfCourseHandicapHole8,
    	self.newGolfCourseHandicapHole9,
    	self.newGolfCourseHandicapHole10,
    	self.newGolfCourseHandicapHole11,
    	self.newGolfCourseHandicapHole12,
    	self.newGolfCourseHandicapHole13,
    	self.newGolfCourseHandicapHole14,
    	self.newGolfCourseHandicapHole15,
    	self.newGolfCourseHandicapHole16,
    	self.newGolfCourseHandicapHole17,
    	self.newGolfCourseHandicapHole18
    ];
    self.golfCourseHandicapHoles(t);

    self.generateHandicaps = function() {
    	var select = document.createElement("SELECT");
    	for (var i = 1; i < 19; i++) {
    		var option = document.createElement("OPTION");
    		option.value 	= i;
    		option.text 	= i;
    		option.selected = (i == 1);
    		select.appendChild(option);
    	};
    }

// Apply bindings
ko.applyBindings(new PlayerListViewModel());