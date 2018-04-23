'use strict';

angular
    .module('app')
    .controller('orders_controller', _controller);

function _controller($scope, __env, OrdersService) {
    $scope.results = [];

    _init();

    function _init() {
        get_orders();
    }

    function get_orders() {
        OrdersService
            .get_orders()
            .then(
                function(orders) {
                    $scope.results = orders.results;
                    console.log($scope.results);
                }
            );
    }
}

