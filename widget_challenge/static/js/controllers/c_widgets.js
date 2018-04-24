'use strict';

angular
    .module('app')
    .controller('widgets_controller', _controller);

function _controller($scope, WidgetsService, CategoriesService, FinishesService, SizesService) {
    $scope.items = [];
    $scope.categories = [];
    $scope.finishes = [];
    $scope.sizes = [];
    $scope.active_item = {};

    _init();

    function _init() {
        get_categories();
        get_finishes();
        get_sizes();
        get_widgets();
    }

    function get_categories() {
        CategoriesService
            .get_categories()
            .then(
                function(categories) {
                    $scope.categories = categories.results;
                }
            );
    }

    function get_finishes() {
        FinishesService
            .get_finishes()
            .then(
                function(finishes) {
                    $scope.finishes = finishes.results;
                }
            );
    }

    function get_sizes() {
        SizesService
            .get_sizes()
            .then(
                function(sizes) {
                    $scope.sizes = sizes.results;
                }
            );
    }

    function get_widgets() {
        WidgetsService
            .get_widgets()
            .then(
                function(widgets) {
                    $scope.items = widgets.results;
                }
            );
    }

    function refresh_page() {
        $scope.active_item = {};
        get_widgets();
    }

    $scope.reset_active_item = function() {
        $scope.active_item = {};
    };

    $scope.submit_form = function() {
        if ($scope.active_item.id != null) {
            WidgetsService
                .update_widget($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
        else {
            WidgetsService
                .add_widget($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
    };

    $scope.delete_item = function(item) {
        WidgetsService
            .delete_widget(item.id)
            .then(
                function(results) {
                    refresh_page();
                }
            )
    };

    $scope.edit_entry = function(item) {
        $scope.active_item = _.clone(item);
        console.log("[105] ", $scope.active_item);
        console.log("[106] ", $scope.active_item.category);
    };
}

