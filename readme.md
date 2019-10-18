## Mockr
    A RESTful Mock Server Generator in Python.

### Why "Mockr"?
    1. It is not a fast to write a mock server, and let the 
        mobile or Web App Team to start building the product while API is not yet
        baked. So let them work on the mock Request-Response while you build a Real one.
    2. `Mockr` generates a Fully Functional Web Server with 
        a `workable` Documentation.
    3. I know, there are other alternative in the market Like Apiary or other,
        but I want to build of my own.
    4. I need to spin up mock server several times to try new projects as
        in their prototyping phase.
    5. It is always fun to build things that actually works.
    6. Yes, I actually use this in my Daily Pet Projects.


### How to install
    It is in pure Python, so no extra batteries are needed but for a Simple one.
    You need to install `Flask` via PIP. 
    
First Clone this Repository.
```bash
    git clone <this_repository>
    
```
Go to the Project Root Directory and Type 
```python
python setup.py install

```
#### Or You can simply use pip

``` python
pip install git+https://github.com/sabbiramin113008/mockr.git

```

The package should be installed on your system.

### How To Use

`Mockr` is also a install-able CLI app that can be run from any where.
 To Generate a mock RESTful Python Flask WEb Server, we need one thing.
 
 #### Write a `mock.json` File
 You need to have a API description file named `mock.json` that contains
 details about the Routes, their HTTP verbs ( GET, POST, PUT, DELETE etc),
 the Request Header ( if any), Request Body and Request Params or Query 
 Parameters. Also routes must contain the Response Object with Response
 Status Code, Response Body etc. A sample `mock.json` file can be found in the 
 `examples` Folder in this Repository.
 
#### Generating Python Web Server
 Open up the Terminal in the directory where you put your `mock.json`
 File.
 
 Now type 
 ```python
mockr generate
```
Now You will be prompted to Enter the Location of the `mock.json` File.

```bash
λ mockr generate
Enter The Mock Dir Name: F:\projektus\py\mocker\examples
```

A `server.py` and a `db.json` file will be generated.

### Starting the Mock Server
As it is about Mock Serving, we can use Python to spin up the server. 
N.B. Use Production Grade Server Tools Like NGINX or Gunicorn if used in Production.

Simply type 
```python
python server.py
```
A Server will be Launched in the Localhost at PORT: 8000

Open up any browser and Go to `localhost:8000/docs`. You will find a decent 
API documentation up there. 

For Checking the API Responses, Use any HTTP Client like Insomnia or Postman. 

### Compitability
Actually I tested this generator to generate mock servers in Windows Environment (Windows 10 Actually.)
So, I dont't have result what would happen on MacOS or Linux. 

