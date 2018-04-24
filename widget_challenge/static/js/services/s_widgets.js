(function () {
    'use strict';

    angular
        .module('app')
        .factory('WidgetsService', Service);

    function Service($http, $q, __env) {
        var factory = {
              get_widgets: get_widgets
            , get_widget: get_widget
            , add_widget: add_widget
            , update_widget: update_widget
            , delete_widget: delete_widget
        };

        return factory;

        function get_widgets() {
            var deferred = $q.defer();

            $http.get(__env.api_url + ':' + __env.port + '/widgets/')
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

        function get_widget(id) {
            var deferred = $q.defer();

            $http.get(__env.api_url + ':' + __env.port + '/widgets/' + id + '/')
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

        function add_widget(form) {
            var deferred = $q.defer();
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                }
            };

            $http.post(__env.api_url + ':' + __env.port + '/widgets/', form_data, config)
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

        function update_widget(form_data) {
            var deferred = $q.defer();
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                }
            };

            $http.put(__env.api_url + ':' + __env.port + '/widgets/' + form_data.id + '/', form_data, config)
                .then(function(response) {
                    deferred.resolve(response);
                }
                , function(data, status, headers, config) {
                    deferred.resolve(JSON.parse('{"response": {"method": "PUT", "result": "error", "status": "' + status + '"}}'));
                })
            ;
            return deferred.promise;
        }

        function delete_widget(id) {
            var deferred = $q.defer();

            $http.delete(__env.api_url + ':' + __env.port + '/widgets/' + id + '/')
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
