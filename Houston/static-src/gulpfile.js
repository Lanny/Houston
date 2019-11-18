var gulp = require('gulp');
var flatten = require('gulp-flatten');
var less = require('gulp-less');
var sourcemaps = require('gulp-sourcemaps');
var path = require('path');
var argv = require('yargs').argv;
var minifyCSS = require('gulp-minify-css');
var requirejsOptimize = require('gulp-requirejs-optimize');
var concat = require('gulp-concat');
var svg = require('gulp-svg-inline-css');

var staticDir = '../static',
  jsDir = path.join(staticDir, 'Houston/js'),
  optimizeModules = ['tracker.js'];
 
gulp.task('icons', function() {
  return gulp.src('assets/svg/*.svg')
    .pipe(svg({
      className: '.icn-%s()'
    }))
    .pipe(concat('icons.less'))
    .pipe(gulp.dest('components/base'));
});

gulp.task('less', gulp.series('icons', function lessTask() {

  var lessStream = less({
      paths: [ path.join(__dirname, 'less') ]
    }).on('error', function(err) {
      console.error(err);
      this.emit('end');
    });

  var stream = gulp.src('./src/combined/combined.less');

  stream = argv.optimizeAssets ? stream : stream.pipe(sourcemaps.init());
  stream = stream.pipe(lessStream);
  stream = argv.optimizeAssets ? stream : stream.pipe(sourcemaps.write());
  stream = stream.pipe(flatten());
  stream = argv.optimizeAssets ? stream.pipe(minifyCSS()) : stream;
  stream = stream.pipe(gulp.dest('../static/Houston/css'));

  return stream;
}));

gulp.task('javascript', function() {
  return gulp.src('./components/**/*.js')
    .pipe(flatten())
    .pipe(gulp.dest(jsDir));
});

gulp.task('optimize-js', gulp.series('javascript', function() {
  var optPaths = optimizeModules.map(function(moduleName) {
    return path.join(jsDir, moduleName);
  });

  return gulp.src(optPaths)
    .pipe(requirejsOptimize())
    .pipe(gulp.dest('../static/js'))
    .pipe(flatten())
    .pipe(gulp.dest('../static/js'));
}));

var generateTasks = [/* 'less' */];
generateTasks.push(argv.optimizeAssets ? 'optimize-js' : 'javascript');
gulp.task('generate', gulp.parallel(generateTasks));

gulp.task('watch', gulp.series('generate', function() {
  gulp.watch([ './components/assets/svg/*.svg' ], ['icons']);
  gulp.watch([ './components/**/*.less' ], ['less']);
  gulp.watch([ './components/**/*.js' ], ['javascript']);
}));
