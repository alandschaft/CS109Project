var searchApp = angular.module('searchApp',[]);

searchApp.controller('MainCtrl',
    function($scope, $http) {
        $scope.sessionId = 'n';
        $scope.clickReset = function() {
            $http.get('/sessions/' + $scope.sessionId + '/new').then(function(res) {
                console.log(res);
                $scope.sessionId = res.data.session_id;
                $scope.uiTerms = res.data.ui_terms;
                $scope.uiDocs = res.data.ui_docs;
                $scope.selectedTerms = res.data.selected_terms;
                $scope.NCandidates = res.data.N_candidate_docs;
        });};

        $scope.clickReset(); // init session

        $scope.clickNext = function() {
            $http.get('/sessions/' + $scope.sessionId + '/next').then(function(res) {
                $scope.uiTerms = res.data.ui_terms;
                $scope.uiDocs = res.data.ui_docs;
                $scope.selectedTerms = res.data.selected_terms;
                $scope.NCandidates = res.data.N_candidate_docs;
        });};

        $scope.clickTerm = function(_term) {
            $http.get('/sessions/' + $scope.sessionId + '/select_term', {params: {term: _term.text}}).then(function(res) {
                $scope.uiTerms = res.data.ui_terms;
                $scope.uiDocs = res.data.ui_docs;
                $scope.selectedTerms = res.data.selected_terms;
                $scope.NCandidates = res.data.N_candidate_docs;
        });};

    });
