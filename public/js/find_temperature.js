var TemperatureService = require('./temperature_service.js');


var findTemperature = function () {
    var service = new TemperatureService();
    $('#tempResults').fadeTo(300, 0, function() {
        var city = $('#inputCity').val();
        service.getTemperature(city)
        .done(function(data) {
            $('#tempResults').fadeTo(300, 1).html(
                'In ' + city + ' there are ' + data['temp'] + '°F'
            );
        })
        .fail(function(data) {
            $('#tempResults').fadeTo(300, 1).html(data.responseJSON['details'])
        })
    })
}

module.exports = findTemperature;
