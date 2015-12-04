// Global vars
var sessionId = ''
var apiURL = 'https://cs109-clinical-trialst-search.herokuapp.com/sessions/'

// Doc ready
$( document ).ready(function() {    
    //words.push(createWordObject('Large', 13))
    //words.push(createWordObject('Medium', 7))
    //words.push(createWordObject('Small', 2))
    newSearchSession()
})

// JQCloud functions
$('#demoapp').jQCloud([],
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
    $('#demoapp').jQCloud('update', words);
}

function selectedWord(word)
{
    updateWordCloud([])
    console.log('word: ' + word)
    searchSelectedWord(word)
}

function createWordObject(word, weight)
{
    return {text: word, weight:weight , link: 'javascript:selectedWord("'+word+'");'}
}


// Search API Functions
function newSearchSession()
{
    $.ajax({
      url: apiURL+'new',
      dataType: 'jsonp'
    }).done(function(data)
        {
            console.log(data)
            if ('current_terms' in data)
            {
                updateWordCloudWithWords(data['current_terms'])
            }
            if ('session_id' in data)
            {
                sessionId = data['session_id']
            }
            if ('current_documents' in data)
            {
                documents = data['current_documents']
                // TODO: Show documents
            }
        }
    )
}

function searchSelectedWord(word)
{
    $.ajax({
      url: apiURL+sessionId+'/select/'+word,
      dataType: 'jsonp'
    }).done(function(data)
        {
            console.log(data)
            if ('current_terms' in data)
            {
                updateWordCloudWithWords(data['current_terms'])
            }
            if ('session_id' in data)
            {
                sessionId = data['session_id']
            }
            if ('current_documents' in data)
            {
                documents = data['current_documents']
                // TODO: Show documents
            }
        }
    )
}
