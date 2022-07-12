# Test
Flask Testing

### Requirement
 GIT Hub, GIT CLI, VS Code, Flask, Heroku

 conda create -p venv python==3.7 -y
 conda activate venv/

 Heroku
 App name: mlregress
 Mail: ashish.ivanka@gmail.com
 API key
 5420b389-b4e1-4094-9f51-9329f0060e3b

 Build docker image
 docker build -t<image_name>:<tagname> .
 > image name for docker must be lowercase

 To list docker image
 '''
 docker images
 Image ID= b07611c87e36
 '''
b
 Run docker image
 '''
 docker run -p 5000:5000 -e PORT =5000 b07611c87e36
 '''
 To check docker running
 '''
 docker ps
 docker ps <container id>
 '''