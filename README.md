# learn-microservices
### create a virtual environment in python first

https://docs.python.org/3/library/venv.html

### install virtual environment
sudo apt-get install python3-venv

sudo python3 -m venv work1

### activate the virtual environment

source work1/bin/activate

### install packages from requirements file

sudo pip3 install -r requirements.txt

### learn some basics

#12-factor to develop a microservice
https://www.12factor.net/

#12-factor summary:

    Stored in a single codebase, tracked in a version control system: one codebase, many deployments
    Has explicitly declared and isolated external dependencies
    Has deployment-specific configuration stored in environment variables, and not in the code
    Treats backing services (for example, data stores, message queues, and so on) as attached or replaceable resources
    Built in distinct stages (build, release, run) with strict separation among them (no knock-on effects or cycles)
    Runs as one or more stateless processes that share nothing, and assumes process memory is transient
    Is completely self-contained and provides a service endpoint on well-defined (environment determined) host and port
    Managed and scaled through process instances (horizontal scaling)
    Disposable with minimal startup, graceful shutdown, and toleration for abrupt process termination
    Designed for continuous development and deployment with minimal difference between the app in development and the app in production
    Treats logs as event streams: the outer or hosting environment deals with processing and routing log files
    Keeps one-off admin scripts with the app to ensure the admin scripts run with the same environment as the app itself

https://martinfowler.com/articles/microservices.html

https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

### principles of API design

https://medium.com/adobetech/three-principles-of-api-first-design-fa6666d9f694

### learn something about API documentation, using swagger

https://swagger.io/docs/specification/about/
https://connexion.readthedocs.io/en/latest/

#### and writing a YAML file. An Open API Specification file can be written either in JSON or YAML. YAML is preferred since it is far more easy to write and read than JSON

https://apihandyman.io/writing-openapi-swagger-specification-tutorial-part-1-introduction/

### Tutorial on API using python:
https://realpython.com/api-integration-in-python/
