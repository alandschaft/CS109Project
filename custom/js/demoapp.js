// Global vars
var apiURL = 'https://cs109-clinical-trialst-search.herokuapp.com/sessions/'
var sessionId = ''
var selectedTerms = []
var currentTerms = []
var currentDocuments = []
var numCandidateDocs = '0'

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
function updateWordCloudWithWords(terms)
{
    words = []
    terms.forEach(function(term) {
        words.push(createWordObject(term['text'], term['score']))  
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
function updateNumberOfDocuments(numberOfDocuments)
{
    $('#numberOfDocuments').text(numberOfDocuments)
}

function updateNumberOfSelectedTerms()
{
    var numberOfSelectedterms = selectedTerms.length
    $('#numberOfSelectedTerms').text(numberOfSelectedterms)
}

function showRelevantDocuments()
{
    var htmlString = '<div class="panel panel-default"><div class="panel-heading">There are '+numCandidateDocs+' relevant documents</div><ul class="list-group">'
    currentDocuments.forEach(function(document) {
        htmlString = htmlString+'<a href="'+document["url"]+'" class="list-group-item" target=blank>'+document["nct_id"]+': '+document["title"]+'</a>'
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
    callAPI('new', {})
}

function searchSelectedWord(word)
{
    callAPI(sessionId+'/select_term', {term:word})
}

function searchNext()
{
    callAPI(sessionId+'/next')
}

function callAPI(endpoint, data)
{
    var url = apiURL+endpoint
    console.log(url)
    showLoader()
    $.ajax({
      url: url,
      dataType: 'JSONP',
      data: data
    }).done(function(data)
        {
            console.log(data)
            var response
            if(typeof data =='object')
            {
                response = data
            }
            else 
            {
                response = JSON.parse(data)
            }
            
            
            if ('ui_terms' in response)
            {
                currentTerms = response['ui_terms']
                updateWordCloudWithWords(currentTerms)
            }
            if ('session_id' in response)
            {
                sessionId = response['session_id']
            }
            if ('ui_docs' in response)
            {
                currentDocuments = response['ui_docs']
            }
            if ('N_candidate_docs' in response)
            {
                numCandidateDocs = response['N_candidate_docs']
                updateNumberOfDocuments(numCandidateDocs)
            }
        }
    )
}
