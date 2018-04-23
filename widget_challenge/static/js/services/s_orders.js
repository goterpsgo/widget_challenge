(function () {
    'use strict';

    angular
        .module('app')
        .factory('OrdersService', Service);

    function Service($http, $q, __env) {
        var factory = {
              get_orders: get_orders
            , get_order: get_order
            , add_order: add_order
            , update_order: update_order
            , delete_order: delete_order
        };

        return factory;

        function get_orders() {
            var deferred = $q.defer();

            $http.get(__env.api_url + ':' + __env.port + '/orders')
                .then(
                    function(response) {
                        deferred.resolve(response.data);
                    }
                    , function(data, status, headers, config) {
                        // deferred.resolve(response.data.response);
                        deferred.resolve(JSON.parse('{"response": {"method": "GET", "result": "error", "status": "' + status + '"}}'));
                    }
                );
            return deferred.promise;
        }

        function get_order(id) {
            var deferred = $q.defer();

            $http.get(__env.api_url + ':' + __env.port + '/orders/' + id)
                .then(
                    function(response) {
                        deferred.resolve(response.data);
                    }
                    , function(data, status, headers, config) {
                        // deferred.resolve(response.data.response);
                        deferred.resolve(JSON.parse('{"response": {"method": "GET", "result": "error", "status": "' + status + '"}}'));
                    }
                );
            return deferred.promise;
        }

        function add_order(form) {
            var deferred = $q.defer();
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                }
            };

            $http.post(__env.api_url + ':' + __env.port + '/orders', form_data, config)
                .then(
                    function(form_data) {
                        deferred.resolve(form_data);
                    }
                    , function(data, status) {
                        deferred.resolve(JSON.parse('{"response": {"method": "POST", "result": "error", "status": "' + status + '"}}'));
                    }
                );
            return deferred.promise;
        }

        function update_order(form_data) {
            var deferred = $q.defer();
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                }
            };

            $http.put(__env.api_url + ':' + __env.port + '/orders/' + form_data.id, form_data, config)
                .then(function(response) {
                    deferred.resolve(response);
                }
                , function(data, status, headers, config) {
                    deferred.resolve(JSON.parse('{"response": {"method": "PUT", "result": "error", "status": "' + status + '"}}'));
                })
            ;
            return deferred.promise;
        }

        function delete_order(id) {
            var deferred = $q.defer();

            $http.delete(__env.api_url + ':' + __env.port + '/orders/' + id)
                .then(function(data, status, headers) {
                    deferred.resolve(data);
                }
                , function(data, status, header, config) {
                    deferred.resolve(JSON.parse('{"response": {"method": "DELETE", "result": "error", "status": "' + status + '"}}'));
                })
            ;
            return deferred.promise;
        }
    }
})();
