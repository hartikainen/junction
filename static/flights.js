function get_nearest_airport(lat, lng, callback) {
    var curLoc = new google.maps.LatLng(lat,lng);

    var map = new google.maps.Map(document.getElementById('map'), {
        center: curLoc,
        zoom: 15
    });

    var request = {
        location: curLoc,
        radius: '50000',
        types: ['airport']
    };

    service = new google.maps.places.PlacesService(map);
    service.nearbySearch(request, callback);
    return 0;
}

function handleLocs(results, status) {
    console.log("handleLocs called");
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            var place = results[i];
            // https://www.developer.aero/Airport-API/Try-it-Now
            // doesn't work because cross site.
            // move to backend?
            $.ajax({
                url:"https://airport.api.aero/airport/match/" + window.encodeURIComponent(place.name) + "?user_key=e6f866816ab0b233fc098adeabab8cf8"
            });
            console.log(place.name);
        }
    }
}

$(window).load(function(){
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            get_nearest_airport(position.coords.latitude, position.coords.longitude, handleLocs);
        });
    } else {
        console.log("Location is not available.");
    }
});
