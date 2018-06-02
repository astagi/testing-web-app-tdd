function TemperatureService() {}

TemperatureService.prototype.getTemperature = function(city) {
    return $.get( "/api/temperature?city=" + city)
};

module.exports = TemperatureService;
