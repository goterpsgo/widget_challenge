'use strict';

angular
    .module('app')
    .controller('sizes_controller', _controller);

function _controller($scope, SizesService) {
    $scope.items = [];
    $scope.active_item = {};

    _init();

    function _init() {
        get_sizes();
    }

    function get_sizes() {
        SizesService
            .get_sizes()
            .then(
                function(sizes) {
                    $scope.items = sizes.results;
                }
            );
    }

    function refresh_page() {
        $scope.active_item = {};
        get_sizes();
    }

    $scope.reset_active_item = function() {
        $scope.active_item = {};
    };

    $scope.submit_form = function() {
        if ($scope.active_item.id != null) {
            SizesService
                .update_size($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
        else {
            SizesService
                .add_size($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
    };

    $scope.delete_item = function(item) {
        SizesService
            .delete_size(item.id)
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

