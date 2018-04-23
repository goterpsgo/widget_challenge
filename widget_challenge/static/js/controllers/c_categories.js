'use strict';

angular
    .module('app')
    .controller('categories_controller', _controller);

function _controller($scope, __env, CategoriesService) {
    $scope.results = [];

    _init();

    function _init() {
        get_categories();
    }

    function get_categories() {
        CategoriesService
            .get_categories()
            .then(
                function(categories) {
                    $scope.results = categories.results;
                    console.log($scope.results);
                }
            );
    }
}

