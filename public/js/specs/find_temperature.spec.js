var findTemperature = require('../find_temperature.js');

describe("find_temperature function", function() {

    beforeEach(function () {
        document.body.innerHTML = __html__['public/js/specs/fixtures/main'];
    });

    it("shows the current temperature of a given place", function(done) {

        spyOn($, 'get').and.callFake(function(e) {
            return $.Deferred().resolve(
                {
                    'temp' : '130'
                }
            ).promise();
        });

        $('#inputCity').val('Pistoia');
        findTemperature();

        setTimeout(function() {
            expect($('#tempResults').html()).toBe('In Pistoia there are 130°F');
            done();
        }, 1000);
    });

    it("shows an error message if server returns an error code", function(done) {

        spyOn($, 'get').and.callFake(function(e) {
            return $.Deferred().reject(
                {
                    'responseJSON' : {
                        'details':'Error'
                    }
                }
            ).promise();
        });

        $('#inputCity').val('Gotham City');
        findTemperature();

        setTimeout(function() {
            expect($('#tempResults').html()).toBe('Error');
            done();
        }, 1000);
    });

    afterEach(function() {
    });
});
