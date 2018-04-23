'use strict';

angular
    .module('app')
    .controller('finishes_controller', _controller);

function _controller($scope, __env, FinishesService) {
    $scope.results = [];

    _init();

    function _init() {
        get_finishes();
    }

    function get_finishes() {
        FinishesService
            .get_finishes()
            .then(
                function(finishes) {
                    $scope.results = finishes.results;
                    console.log($scope.results);
                }
            );
    }
}

