'use strict';

angular
    .module('app')
    .controller('categories_controller', _controller);

function _controller($scope, CategoriesService) {
    $scope.items = [];
    $scope.active_item = {};

    _init();

    function _init() {
        get_categories();
    }

    function get_categories() {
        CategoriesService
            .get_categories()
            .then(
                function(categories) {
                    $scope.items = categories.results;
                }
            );
    }

    function refresh_page() {
        $scope.active_item = {};
        get_categories();
    }

    $scope.reset_active_item = function() {
        $scope.active_item = {};
    };

    $scope.submit_form = function() {
        if ($scope.active_item.id != null) {
            CategoriesService
                .update_category($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
        else {
            CategoriesService
                .add_category($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
    };

    $scope.delete_item = function(item) {
        CategoriesService
            .delete_category(item.id)
            .then(
                function(results) {
                    refresh_page();
                }
            )
    };

    $scope.edit_entry = function(item) {
        $scope.active_item = _.clone(item);
    };
}

