module.exports = function(grunt) {

  // load all grunt tasks
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  grunt.initConfig({
    open : {
      dev: {
        path: 'http://localhost:1919'
      }
    },

    connect: {
      server: {
        options: {
          port: 1919,
          base: '../_build',
          livereload: true
        }
      }
    },
    copy: {
      fonts: {
        files: [
          // includes files within path
          {expand: true, flatten: true, src: ['bower_components/font-awesome/fonts/*'], dest: 'sphinx_zenoss_theme/static/fonts/', filter: 'isFile'}
        ]
      }
    },

    sass: {
      dev: {
        options: {
          style: 'expanded',
          loadPath: ['bower_components/bourbon/dist', 'bower_components/neat/app/assets/stylesheets', 'bower_components/font-awesome/scss', 'bower_components/wyrm/sass']
        },
        files: [{
          expand: true,
          cwd: 'sass',
          src: ['*.sass'],
          dest: 'sphinx_zenoss_theme/static/css',
          ext: '.css'
        }]
      },
      build: {
        options: {
          style: 'compressed',
          loadPath: ['bower_components/bourbon/dist', 'bower_components/neat/app/assets/stylesheets', 'bower_components/font-awesome/scss', 'bower_components/wyrm/sass']
        },
        files: [{
          expand: true,
          cwd: 'sass',
          src: ['*.sass'],
          dest: 'sphinx_zenoss_theme/static/css',
          ext: '.css'
        }]
      }
    },

    exec: {
      bower_update: {
        cmd: 'bower update'
      },
      build_sphinx: {
        cmd: 'sphinx-build .. ../_build'
      }
    },
    clean: {
      options: { force: true },
      build: ["../_build"],
      fonts: ["sphinx_zenoss_theme/static/fonts"]
    },

    watch: {
      /* Compile sass changes into theme directory */
      sass: {
        files: ['sass/*.sass', 'bower_components/**/*.sass'],
        tasks: ['sass:dev']
      },
      /* Changes in theme dir rebuild sphinx */
      sphinx: {
        files: ['sphinx_zenoss_theme/**/*', '../**/*.rst', '../**/*.py'],
        tasks: ['clean:build','exec:build_sphinx']
      },
      /* live-reload the demo_docs if sphinx re-builds */
      livereload: {
        files: ['../_build/**/*'],
        options: { livereload: true }
      }
    }

  });

  grunt.loadNpmTasks('grunt-exec');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-open');

  grunt.registerTask('fonts', ['clean:fonts','copy:fonts']);
  grunt.registerTask('default', ['exec:bower_update','clean:build','sass:dev','exec:build_sphinx','connect','open','watch']);
  grunt.registerTask('build', ['exec:bower_update','clean:build','sass:build','exec:build_sphinx']);
}

