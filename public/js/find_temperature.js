var TemperatureService = require('./temperature_service.js');


var findTemperature = function (inputEl, outputEl) {
    var service = new TemperatureService();
    outputEl.fadeTo(300, 0, function() {
        var city = inputEl.val();
        service.getTemperature(city)
        .done(function(data) {
            outputEl.fadeTo(300, 1).html(
                'In ' + city + ' there are ' + data['temp'] + '°F'
            );
        })
        .fail(function(data) {
            outputEl.fadeTo(300, 1).html(data.responseJSON['details'])
        })
    })
}

module.exports = findTemperature;
