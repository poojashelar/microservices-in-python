#microservices-in-python:

Problem Statement- Create MCQ Examination Center web app to take quick mcq test using Flask. 
DB Used - sqlite 

Attached more materials : Detailed problem statement,  Application Class Diagram, flowchart etc.

To Setup Environment follow below steps:

- Install Python 3.X
- Create Python Virtual Environments (python -m venv <env_name>  then activate it by running activate.bat)
- Install Python VS Code Extension
- To create MCQ Exam Center Flask web application follow:
    - install flask using - pip install Flask
    - to check whats install - pip list
    - To run the application use cmd : flask --app app run
    - To initialise db use cmd : flask --app app init-db
    - Jinja templating for Dynamic Web Pages (import render_template)
- Use Pip to Freeze Python Dependencies (pip freeze  > requirements.txt )
    - to install dependencies cmd - pip install -r <filename(requirements.txt)>
- Build the docker image using Dockerfile
- Write Docker Compose file (Pending)
-Writing Kubernetes Manifest files for the application(Pending)
-Creating Helm Chart (Pending)
