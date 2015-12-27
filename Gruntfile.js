module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        responsive_images: {
          dev: {
            sizes: [{
                name: 'small',
                width: 480,
              }, {
                name: 'medium',
                width: 640,
              }, {
                name: 'large',
                width: 960,
            }],
            files: [{
              expand: true,
              src: ['img/*.{jpg,gif,png}'],
              dest: 'dist/'
            }]
          }  
        },
    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-responsive-images');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['responsive_images']);

};
