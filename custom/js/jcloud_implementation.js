// Global vars
var session = ''
var apiURL = 'https://cs109-clinical-trialst-search.herokuapp.com/sessions/new'

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

// Word Object functions
function createWordObject(word, weight)
{
    return {text: word, weight:weight , link: 'javascript:selectedWord("'+word+'");'}
}

function selectedWord(word)
{
    console.log('word: ' + word)
}

// Search API Functions
function newSearchSession()
{
     console.log('newSearchSession')
     apiCall()
}

// Network Calls functions
function apiCall()
{
    $.ajax({
      url: apiURL,
      dataType: 'json'
    }).done(function(data)
        {
            condole.log(data)
        }
    )

}