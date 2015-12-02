
run server with python server.py



Function 1
---------------------------------------------------
create_session()

This function creates a session_data object (python dictionary) that includes all the parameters of one search session:

- session_id - unique identifier
- current_terms - list of terms currently shown to the user (strings). Initialized with the highest ranking terms.
- skipped_terms - list of terms that where shown to the user, but the user clícked "next" - i.e. did not select. Initialized empty.
- clicked_terms - list of terms that the user selected. Initialized empty.
- current_documents - list of documents curretly shown to the user (used for paging.) Each list element is a dictionary with:
{
nct_id=nct_id,
title=title,
url=url # for example https://clinicaltrials.gov/ct2/show/NCT01027715
}

CreateSession returns a dictionary (serialized to json) with 3 elements:

{
"session_id" = session_id,
"current_terms" = current_terms,
"current_documents" = top-20 documents from current_documents session object
}


Web API: Visit localhost:5000/sessions/new to obtain session key



Function 2
---------------------------------------------------
on_next(session_id)

This function is called when the user clicks on the next button

returns a dictionary (serialized to json) with 3 elements:

{
"session_id" = session_id,
"current_terms" = current_terms (strings),
"current_documents" = top-20 documents from current_documents session object
}


Web API: localhost:5000/sessions/{your session key}/next


Function 3
---------------------------------------------------

on_select_term(session_id, term)

This function is called when the user selects a term

returns a dictionary (serialized to json) with 3 elements:

{
"session_id" = session_id,
"current_terms" = current_terms (strings),
"current_documents" = top-20 documents from current_documents session object
}

localhost:5000/sessions/{your session key}/select/{term}
