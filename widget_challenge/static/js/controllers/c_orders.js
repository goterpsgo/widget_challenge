'use strict';

angular
    .module('app')
    .controller('orders_controller', _controller);

function _controller($scope, WidgetsService, OrdersService, OrderItemsService) {
    $scope.orders = [];
    $scope.active_order = {
        id: null,
        orderitems: []
    };
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
        $scope.orders = []; // clear orders queue before populating with resultset
        // Get orders collection
        OrdersService
            .get_orders()
            .then(
                function(orders) {
                    orders.results.forEach(function(order) {
                        // Get orderitems per order
                        OrdersService
                            .get_orderitems_from_order(order.id)
                            .then(
                                function(orderitems) {
                                    // Get widget names per orderitem
                                    orderitems.results.forEach(function(orderitem) {
                                        var this_widget = _.find($scope.widgets, function(obj) {
                                           return obj.id == parseInt(orderitem.widget);
                                        });
                                        orderitem.widget_name = this_widget.name;
                                    });
                                    // Assign orderitems to order object
                                    order.orderitems = orderitems.results;
                                    // Push order object to global orders queue
                                    $scope.orders.push(order);
                                }
                            )
                    });
                }
            );
    }

    function refresh_page() {
        $scope.active_item = {};
        $scope.active_order = {
            id: null,
            orderitems: []
        };
        get_orders();
    }

    $scope.reset_active_item = function() {
        $scope.active_item = {};
    };

    $scope.reset_active_order = function() {
        $scope.active_order = {
            id: null,
            orderitems: []
        };
    };

    $scope.load_active_order = function(order) {
        $scope.active_order = order;
    };

    $scope.submit_item_to_order = function() {
        // assign widget name to `item`
        var this_widget = _.find($scope.widgets, function(obj) {
           return obj.id == parseInt($scope.active_item.widget);
        });
        $scope.active_item.widget_name = this_widget.name;
        $scope.active_order.orderitems.push($scope.active_item);
        $scope.reset_active_item();
    };

    $scope.add_item_to_order = function(item) {
        $scope.items.push(item);
    };

    $scope.submit_order = function() {
        if ($scope.active_order.id != null) {
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
                .add_order()
                .then(
                    function(order) {
                        var order_id = order.data.id;
                        $scope.active_order.orderitems.forEach (function(item) {
                            delete item.name;   // name was only needed for display purposes
                            item.widget = parseInt(item.widget);
                            item.order = order_id;
                            OrderItemsService
                                .add_orderitem(item)
                                .then(
                                    function(orderitem) {
                                        refresh_page();
                                    }
                                )
                        });
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

