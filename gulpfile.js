var gulp = require('gulp');
var csso = require('gulp-csso');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var bro = require('gulp-bro');
var del = require('del');

var distFolder = 'dist';
var cssDestFolder = distFolder + '/public/css';
var jsDestFolder = distFolder + '/public/js';

gulp.task('clean', function () {
    return del([
        distFolder
    ]);
});

gulp.task('css', function(){
    return gulp.src([
        'public/css/bootstrap.css',
        'public/css/weather.css',
    ])
    .pipe(csso({ comments: false }))
    .pipe(concat('styles.min.css'))
    .pipe(gulp.dest(cssDestFolder))
});

gulp.task('js', function(){
    return gulp.src([
        'public/js/main.js',
    ])
    .pipe(bro())
    .pipe(uglify())
    .pipe(concat('main.min.js'))
    .pipe(gulp.dest(jsDestFolder))
});

gulp.task('build', ['clean'], function(){
    gulp.start('css', 'js');
})
