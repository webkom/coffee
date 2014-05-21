var gulp = require('gulp'),
    bailey = require('gulp-bailey'),
    gutil = require('gulp-util'),
    concat = require('gulp-concat'),
    watch = require('gulp-watch');

gulp.task('libs', function() {
  var libs = [
    './frontend/libs/jquery.min.js',
    './frontend/libs/angular.min.js',
    './frontend/libs/moment.js',
    './frontend/libs/moment.nb.js',
    './frontend/libs/chartjs-directive.js',
  ];

  gulp.src(libs)
    .pipe(concat('libs.js'))
    .pipe(gulp.dest('coffee/static/'));
});

gulp.task('default', ['libs'],function () {
  gulp.src('./frontend/src/**/*.bs')
    .pipe(bailey({bare: true}).on('error', gutil.log))
    .pipe(concat('coffee.js'))
    .pipe(gulp.dest('coffee/static/'));
});

gulp.task('watch', function () {
  gulp.src('./frontend/src/**/*.bs')
    .pipe(watch(function (files) {
      return files.pipe(bailey({bare: true}).on('error', gutil.log))
                  .pipe(concat('coffee.js'))
                  .pipe(gulp.dest('coffee/static/'));
    }));
});
