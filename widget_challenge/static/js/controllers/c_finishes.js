'use strict';

angular
    .module('app')
    .controller('finishes_controller', _controller);

function _controller($scope, FinishesService) {
    $scope.items = [];
    $scope.active_item = {};

    _init();

    function _init() {
        get_finishes();
    }

    function get_finishes() {
        FinishesService
            .get_finishes()
            .then(
                function(finishes) {
                    $scope.items = finishes.results;
                }
            );
    }

    function refresh_page() {
        $scope.active_item = {};
        get_finishes();
    }

    $scope.reset_active_item = function() {
        $scope.active_item = {};
    };

    $scope.submit_form = function() {
        if ($scope.active_item.id != null) {
            FinishesService
                .update_finish($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
        else {
            FinishesService
                .add_finish($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
    };

    $scope.delete_item = function(item) {
        FinishesService
            .delete_finish(item.id)
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

