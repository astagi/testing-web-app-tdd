var findTemperature = require('../find_temperature.js');

console.log('TESTING FIND');

describe("A suite is just a function", function() {
    var a;

    beforeEach(function () {
        document.body.innerHTML = __html__['public/js/specs/fixtures/main'];
    });

    it("and so is a spec", function() {
        a = true;
        findTemperature()
        expect(a).toBe(true);
    });
});
