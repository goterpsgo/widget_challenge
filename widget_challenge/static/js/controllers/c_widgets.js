'use strict';

angular
    .module('app')
    .controller('widgets_controller', _controller);

function _controller($scope, __env, WidgetsService) {
    $scope.results = [];

    _init();

    function _init() {
        get_widgets();
    }

    function get_widgets() {
        WidgetsService
            .get_widgets()
            .then(
                function(widgets) {
                    $scope.results = widgets.results;
                    console.log($scope.results);
                }
            );
    }
}

