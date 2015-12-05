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
    console.log('word: ' + word)
    searchSelectedWord(word)
}

function createWordObject(word, weight)
{
    return {text: word, weight:weight , link: 'javascript:selectedWord("'+word+'");'}
}

// Documents functions
function updateNumberOfDocuments()
{
    $('#numberOfDocuments').text("1,300")
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

// Search API Functions
function newSearchSession()
{
    callAPI('new')
}

function searchSelectedWord(word)
{
    callAPI(sessionId+'/select/'+word)
}

function searchNext()
{
    callAPI(sessionId+'/next')
}

function callAPI(endpoint)
{
    $.ajax({
      url: apiURL+endpoint,
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
