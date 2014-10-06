/*global ff */
(function() {
    'use strict';

    var results = ff.results;

    if (!results.longitude || !results.latitude) {
        return false;
    }

    var mapOptions = {
        center: new google.maps.LatLng(results.latitude, results.longitude),
        scrollwheel: false,
        zoom: 10
    };
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var infowindow;

    if (results.listing) {
        results.listing.forEach(function(property) {
            var marker = new google.maps.Marker({
                anchorPoint: new google.maps.Point(16, 45),
                icon: '/static/img/green-home-icon.png',
                map: map,
                position: new google.maps.LatLng(property.latitude, property.longitude),
                visible: true
            });

            google.maps.event.addListener(marker, 'click', function() {
                if (infowindow) {
                    infowindow.close();
                }
                var template = _.template($('#property-template').html());
                infowindow = new google.maps.InfoWindow({
                    pixelOffset: new google.maps.Size(-16, -85),
                    content: template({property: property})
                });
                infowindow.open(map, marker);
            });
        });
    }

})();