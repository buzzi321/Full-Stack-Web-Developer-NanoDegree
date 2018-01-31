
var locations = [
    {
        name: 'Warner Bros. VIP Studio Tour',
        lat: 34.152068,
        long: -118.336710
    },
    {
        name: 'Universal Studios Hollywood',
        lat: 34.137886,
        long: -118.352867
    },
    {
        name: 'Los Angeles Zoo & Botanical Gardens',
        lat: 34.149043,
        long: -118.284050
    },
    {
        name: 'Griffith Observatory',
        lat: 34.118423,
        long: -118.300427
    },
    {
        name: 'Hollywood Sign',
        lat: 34.134132,
        long: -118.321550
    }

];
var map;
function LocationViewModel() {
    var self = this;
    this.buttonText = ko.observable('Hide Markers');
    this.searchFilter = ko.observable("");
    this.showMarkers = ko.observable("true");
    this.markers = [];

    fsclientid = "O25EDZV2T5WZYMXWBGTNMKY3OM0VJJJ43CDHNX1FP11XDB5H";
    fsclientsecret = "Y141NHUTQ0U5YNX0M2EX2SY0CHUEWOX4WXYVPBH4HPP4UHSR";
    this.populateInfoWindow = function(marker, infowindow) {
        if (infowindow.marker != marker) {
            infowindow.setContent('');
            infowindow.marker = marker;
        // Foursquare API Code
            var apiUrl = 'https://api.foursquare.com/v2/venues/search?ll=' +
                marker.lat + ',' + marker.lng + '&client_id=' + fsclientid +
                '&client_secret=' + fsclientsecret + '&query=' + marker.title +
                '&v=20170708' + '&m=foursquare';
            // Foursquare API
            $.getJSON(apiUrl).done(function(marker) {
                var response = marker.response.venues[0];



                var content = '<div id="iw-container">' +
                    '<div class="iw-title">' + response.name +'</div>' +
                    '<div class="iw-subTitle">' + response.categories[0].shortName + '</div>' +
                    '<div class="iw-content">' +
                    '<div class="iw-subTitle">Address:</div>' +
                    '<p>' + response.location.formattedAddress[0] + '<br>'+
                    response.location.formattedAddress[1] + '<br>'+
                    response.location.formattedAddress[2] + '<br>'+
                    '</div>' +
                    '<div class="iw-bottom-gradient"></div>' +
                    '</div>';

                infowindow.setContent( content);
            }).fail(function() {
                // Send alert
                alert(
                    "There was an issue loading the Foursquare API. Please refresh your page to try again."
                );
            });


            infowindow.open(map, marker);

            infowindow.addListener('closeclick', function() {
                infowindow.marker = null;
            });
        }
    };

//Code for Show/Hide Button
    self.toggleMarkers = function(){
        if (self.showMarkers){
            for (var j = 0; j < this.markers.length; j++ ) {
                self.markers[j].setVisible(false);

            }
            self.myInfoWindow.close();
            self.showMarkers = false;
        }
        else {
            for (var k = 0; k < this.markers.length; k++ ) {
                self.markers[k].setVisible(true);
            }
            self.showMarkers = true;
        }
        self.buttonText(self.showMarkers === false ? 'Show Markers' : 'Hide Markers');
    };






    this.fillMarkers = function() {

        self.showMarkers = true;
        for (var m = 0; m < self.markers.length; m++ ) {
            self.markers[m].setVisible(true);
        }
        self.buttonText(self.showMarkers === false ? 'Show Markers' : 'Hide Markers');
        self.populateInfoWindow(this, self.myInfoWindow);
        this.setAnimation(google.maps.Animation.BOUNCE);
        setTimeout((function() {
            this.setAnimation(null);
        }).bind(this), 1400);
    };
// Initialize the Map
    this.initMap = function() {
        var latlng = new google.maps.LatLng(34.0522, -118.2437);
        var mapSheet = document.getElementById('map');
        var mapOptions = {
            center: latlng,
            zoom: 11
        };
        map = new google.maps.Map(mapSheet, mapOptions);
        this.myInfoWindow = new google.maps.InfoWindow();
        for (var l = 0; l < locations.length; l++) {
            this.markerTitle = locations[l].name;
            this.markerLat = locations[l].lat;
            this.markerLng = locations[l].long;
            // Google Maps marker setup
            this.marker = new google.maps.Marker({
                map: map,
                position: {
                    lat: this.markerLat,
                    lng: this.markerLng
                },
                title: this.markerTitle,
                lat: this.markerLat,
                lng: this.markerLng,
                animation: google.maps.Animation.DROP
            });
            this.marker.setMap(map);
            this.markers.push(self.marker);
            this.marker.addListener('click', self.fillMarkers);
        }

    };

    self.initMap();
    this.myFilteredLocations = ko.computed(function() {
        var results = [];
        self.myInfoWindow.close();
        for (var i = 0; i < this.markers.length; i++) {
            var markerLocation = this.markers[i];
            if (markerLocation.title.toLowerCase().includes(this.searchFilter()
                    .toLowerCase())) {
                results.push(markerLocation);
                this.markers[i].setMap(map);
                this.markers[i].setVisible(true);
                self.showMarkers = true;
            } else {
                this.markers[i].setMap(map);
                this.markers[i].setVisible(false);
            }

            self.buttonText(self.showMarkers === false ? 'Show Markers' : 'Hide Markers');
        }
        return results;
    }, this);
}


function intApp() {
    ko.applyBindings(new LocationViewModel());


}


function gm_authFailure() {
    alert('Google Api Error....Please try later...');
}
