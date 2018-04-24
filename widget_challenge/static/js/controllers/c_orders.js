'use strict';

angular
    .module('app')
    .controller('orders_controller', _controller);

function _controller($scope, WidgetsService, OrdersService, OrderItemsService) {
    $scope.items = [];
    $scope.widgets = [];
    $scope.active_item = {};

    _init();

    function _init() {
        get_widgets();
        get_orders();
    }

    function get_widgets() {
        WidgetsService
            .get_widgets()
            .then(
                function(widgets) {
                    $scope.widgets = widgets.results;
                }
            );
    }

    function get_orders() {
        OrdersService
            .get_orders()
            .then(
                function(orders) {
                    $scope.items = orders.results;
                    console.log("[35] ", $scope.items);
                }
            );
    }

    function refresh_page() {
        $scope.active_item = {};
        get_orders();
    }

    $scope.reset_active_item = function() {
        $scope.active_item = {};
    };

    $scope.add_item_to_order = function(item) {
        $scope.items.push(item);
        console.log("[51] ", item);
        console.log("[51] ", $scope.items);
    };

    $scope.submit_form = function() {
        if ($scope.active_item.id != null) {
            OrdersService
                .update_order($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
        else {
            OrdersService
                .add_order($scope.active_item)
                .then(
                    function(results) {
                        refresh_page();
                    }
                )
        }
    };

    $scope.delete_item = function(item) {
        OrdersService
            .delete_order(item.id)
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

