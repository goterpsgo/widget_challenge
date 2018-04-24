(function () {
    'use strict';

    var env = {};

    // Import variables if present (from env.js)
    if(window){
        Object.assign(env, window.__env);
    }

    var routerApp = angular
        .module('app', ['ui.router'])
        .constant('__env', env) // environmental parameters for configuring client-side resources
        .constant('_', window._)    // registering lodash with AngularJS
        .config(function($stateProvider) {

        $stateProvider
            .state('home', {
                url: '/home',
                templateUrl: '/static/html/view_widgets.html',
                controller: 'widgets_controller'
            })
            .state('widgets', {
                url: '/widgets',
                templateUrl: '/static/html/view_widgets.html',
                controller: 'widgets_controller'
            })
            .state('finishes', {
                url: '/finishes',
                templateUrl: '/static/html/view_finishes.html',
                controller: 'finishes_controller'
            })
            .state('sizes', {
                url: '/sizes',
                templateUrl: '/static/html/view_sizes.html',
                controller: 'sizes_controller'
            })
            .state('categories', {
                url: '/categories',
                templateUrl: '/static/html/view_categories.html',
                controller: 'categories_controller'
            })
            .state('orders', {
                url: '/orders',
                templateUrl: '/static/html/view_orders.html',
                controller: 'orders_controller'
            })
    })
    ;
})();