var gulp = require('gulp');
var flatten = require('gulp-flatten');
var less = require('gulp-sources-less');
var sourcemaps = require('gulp-sourcemaps');
var path = require('path');
var argv = require('yargs').argv;
var minifyCSS = require('gulp-minify-css');
var requirejsOptimize = require('gulp-requirejs-optimize');
var concat = require('gulp-concat');
var svg = require('gulp-svg-inline-css');

var staticDir = '../static',
  jsDir = path.join(staticDir, 'Houston/js'),
  optimizeModules = [];
 
gulp.task('icons', function() {
  return gulp.src('assets/svg/*.svg')
    .pipe(svg({
      className: '.icn-%s()'
    }))
    .pipe(concat('icons.less'))
    .pipe(gulp.dest('components/base'));
});

gulp.task('less', ['icons'], function() {

  var lessStream = less({
      paths: [ path.join(__dirname, 'less') ]
    }).on('error', function(err) {
      console.error(err);
      this.emit('end');
    });

  var stream = gulp.src('./src/combined/combined.less');

  stream = argv.optimize ? stream : stream.pipe(sourcemaps.init());
  stream = stream.pipe(lessStream);
  stream = argv.optimize ? stream : stream.pipe(sourcemaps.write());
  stream = stream.pipe(flatten());
  stream = argv.optimize ? stream.pipe(minifyCSS()) : stream;
  stream = stream.pipe(gulp.dest('../static/Houston/css'));

  return stream;
});

gulp.task('javascript', function() {
  return gulp.src('./components/**/*.js')
    .pipe(flatten())
    .pipe(gulp.dest(jsDir));
});

gulp.task('optimize-js', ['javascript'], function() {
  var optPaths = optimizeModules.map(function(moduleName) {
    return path.join(jsDir, moduleName);
  });

  return gulp.src(optPaths)
    .pipe(requirejsOptimize())
    .pipe(gulp.dest('../static/js'))
    .pipe(flatten())
    .pipe(gulp.dest('../static/js'));
});

var generateTasks = ['less'];
generateTasks.push(argv.optimize ? 'optimize-js' : 'javascript');
gulp.task('generate', generateTasks);

gulp.task('watch', ['generate'], function() {
  gulp.watch([ './components/assets/svg/*.svg' ], ['icons']);
  gulp.watch([ './components/**/*.less' ], ['less']);
  gulp.watch([ './components/**/*.js' ], ['javascript']);
});
