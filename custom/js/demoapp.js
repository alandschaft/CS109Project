// Global vars
var apiURL = 'https://cs109-clinical-trialst-search.herokuapp.com/sessions/'
var sessionId = ''
var selectedTerms = []
var currentTerms = []
var currentDocuments = []

// Doc ready
$( document ).ready(function() {    
    newSearchSession()
})

// Menu functions
function menuCloud()
{
    cleanMenu()
    $('#menuCloud').addClass("active")
    updateWordCloudWithWords(currentTerms)
}

function menuDocuments()
{
    cleanMenu()
    $('#menuDocuments').addClass("active")
    showRelevantDocuments()
}

function menuWords()
{
    cleanMenu()
    $('#menuWords').addClass("active")
    showSelectedWords()
}

function menuNext()
{
    cleanMenu()
    $('#menuCloud').addClass("active")
    searchNext()
}

function menuRestart()
{
    cleanMenu()
    $('#menuCloud').addClass("active")
    sessionId = ''
    selectedTerms = []
    newSearchSession()
    updateNumberOfDocuments()
    updateNumberOfSelectedTerms()
}

function cleanMenu()
{
    $('#menuCloud').removeClass("active")
    $('#menuDocuments').removeClass("active")
    $('#menuWords').removeClass("active")
    $('#menuNext').removeClass("active")
}

// JQCloud functions
$('#democontent').jQCloud([],
{
    shape: 'rectangular',
    autoResize: true
})

// Word Cloud functions
function updateWordCloudWithWords(wordsText)
{
    var words = []
    var dummyWeight = 1
    wordsText.forEach(function(word) {
        words.push(createWordObject(word, dummyWeight))  
        dummyWeight++
    })
    updateWordCloud(words)
}

function updateWordCloud(words)
{
    $('#democontent').empty()
    $('#democontent').jQCloud('update', words);
}

function selectedWord(word)
{
    selectedTerms.push(word)
    updateWordCloud([])
    searchSelectedWord(word)
    updateNumberOfSelectedTerms()
}

function createWordObject(word, weight)
{
    return {text: word, weight:weight , link: 'javascript:selectedWord("'+word+'");'}
}

// Display functions
function updateNumberOfDocuments()
{
    var divideby = 1
    if (selectedTerms.length > 0) {
        divideby = selectedTerms.length+1
    }
    var numberOfDocuments = Math.round(1300 / divideby)
    $('#numberOfDocuments').text(numberOfDocuments)
}

function updateNumberOfSelectedTerms()
{
    var numberOfSelectedterms = selectedTerms.length
    $('#numberOfSelectedTerms').text(numberOfSelectedterms)
}

function showRelevantDocuments()
{
    var htmlString = '<div class="panel panel-default"><div class="panel-heading">There are 1,300 relevant documents</div><ul class="list-group">'
    currentDocuments.forEach(function(document) {
        htmlString = htmlString+'<a href="'+document["url"]+'" class="list-group-item" target=blank>'+document["title"]+'</a>'
    })
    htmlString += '</div>'
    $('#democontent').html(htmlString)
}

function showSelectedWords()
{
    var htmlString = '<div class="panel panel-default"><div class="panel-heading">These are the selected terms from the word cloud:</div><ul class="list-group">'
    selectedTerms.forEach(function(term) {
        htmlString = htmlString+'<li class="list-group-item">'+term+'</li>'
    })
    htmlString += '</div>'
    $('#democontent').html(htmlString)
}

function showLoader()
{
    var htmlString = '<div id="spinnerContainer"><div class="spinner-loader">Loading…</div></div>'
    $('#democontent').html(htmlString)
}

// Search API Functions
function newSearchSession()
{
    callAPI('n/new', 'POST')
}

function searchSelectedWord(word)
{
    callAPI(sessionId+'/select/'+word)
}

function searchNext()
{
    callAPI(sessionId+'/next')
}

function callAPI(endpoint, method)
{
    showLoader()
    $.ajax({
      url: apiURL+endpoint,
      method: method,
      dataType: 'jsonp'
    }).done(function(data)
        {
            console.log(data)
            if ('current_terms' in data)
            {
                currentTerms = data['current_terms']
                updateWordCloudWithWords(currentTerms)
            }
            if ('session_id' in data)
            {
                sessionId = data['session_id']
            }
            if ('current_documents' in data)
            {
                currentDocuments = data['current_documents']
                updateNumberOfDocuments()
            }
        }
    )
}
