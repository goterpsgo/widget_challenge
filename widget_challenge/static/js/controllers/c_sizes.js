'use strict';

angular
    .module('app')
    .controller('sizes_controller', _controller);

function _controller($scope, __env, SizesService) {
    $scope.results = [];

    _init();

    function _init() {
        get_sizes();
    }

    function get_sizes() {
        SizesService
            .get_sizes()
            .then(
                function(sizes) {
                    $scope.results = sizes.results;
                    console.log($scope.results);
                }
            );
    }
}

