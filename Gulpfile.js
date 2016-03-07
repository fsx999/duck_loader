var gulp = require('gulp');

gulp.task('copy', function() {

  return gulp.src(['./node_modules/bootstrap/dist/**/**.*', './node_modules/jquery/dist/**/**.*'], {
      base: './node_modules'
    })
    .pipe(gulp.dest('./static'))
  ;
});


gulp.task('default', ['copy'], function() {

});
