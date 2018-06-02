module.exports = function(config) {
    config.set({
        basePath: '.',
        frameworks: ['jasmine', 'browserify'],
        browsers: ['Chrome',],

        preprocessors: {
            'public/js/*.js': [ 'browserify' ],
            'public/js/specs/*.js': [ 'browserify' ],
            'public/js/specs/fixtures/*.html' : ['html2js']
        },
        files: [
            'public/js/specs/fixtures/*.html',
            'https://code.jquery.com/jquery-3.2.1.min.js',
            'public/js/*.js',
            'public/js/specs/*.js',
        ],
        plugins: [
            'karma-jasmine',
            'karma-browserify',
            'karma-coverage',
            'karma-html2js-preprocessor',
            'karma-chrome-launcher'
        ],

        browserify: {
            transform: ['browserify-istanbul']
        },

        reporters: ['progress', 'coverage'],

        coverageReporter: {
            type : 'html',
            dir : '.fecoverage/'
        },

        html2JsPreprocessor: {
            // strip this from the file path
            stripPrefix: 'public/',

            // prepend this to the file path
            prependPrefix: 'served/',

            // or define a custom transform function
            processPath: function(filePath) {
              // Drop the file extension
              return filePath.replace(/\.html$/, '');
            }
        },
        watch: false,
        singleRun: true
    });
};
