
## Stand alone clinical trials search server (static data)

to run use:

python search_server.py

### Main files:
* search_server.py - Implement web stuff: flusk, serialization to json, simple session storage
* core/actions.py - Implement the requests that the server supports: initializing new session, selecting term and requesting the next terms
* core/lib.py - Implement the core algorithms: term selection and documents selection
* static directory - implements simple HTML web application that can be used to test the service
* data directory - the data used by the service
