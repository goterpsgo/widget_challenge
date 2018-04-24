(function () {
    'use strict';

    angular
        .module('app')
        .factory('FinishesService', Service);

    function Service($http, $q, __env) {
        var factory = {
              get_finishes: get_finishes
            , get_finish: get_finish
            , add_finish: add_finish
            , update_finish: update_finish
            , delete_finish: delete_finish
        };

        return factory;

        function get_finishes() {
            var deferred = $q.defer();

            $http.get(__env.api_url + ':' + __env.port + '/finishes/')
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

        function get_finish(id) {
            var deferred = $q.defer();

            $http.get(__env.api_url + ':' + __env.port + '/finishes/' + id + '/')
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

        function add_finish(form_data) {
            var deferred = $q.defer();
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                }
            };

            $http.post(__env.api_url + ':' + __env.port + '/finishes/', form_data, config)
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

        function update_finish(form_data) {
            var deferred = $q.defer();
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                }
            };

            $http.put(__env.api_url + ':' + __env.port + '/finishes/' + form_data.id + '/', form_data, config)
                .then(function(response) {
                    deferred.resolve(response);
                }
                , function(data, status, headers, config) {
                    deferred.resolve(JSON.parse('{"response": {"method": "PUT", "result": "error", "status": "' + status + '"}}'));
                })
            ;
            return deferred.promise;
        }

        function delete_finish(id) {
            var deferred = $q.defer();

            $http.delete(__env.api_url + ':' + __env.port + '/finishes/' + id + '/')
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
