@echo off

rem Create deployment directory
mkdir deployment

rem Copy Flask application files
xcopy /s /e flask-server\* deployment\

rem Copy React build files
xcopy /s /e react-client\dist\* deployment\

rem Optionally copy other files (e.g., configuration files, requirements.txt)

rem Optionally perform any additional steps or modifications

echo Deployment directory created successfully.
