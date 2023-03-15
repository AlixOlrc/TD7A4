# TD7A4

In order to use this docker image and docker-compose, please follow the following steps :

**Without using docker-compose**

  Building the Flask app with the Dockerfile : (In the repository) run 
  > docker build -t app .
  
  Then run the image : 
  > docker run -p 5000:5000 -v /my_app/text.txt app
  
  Now you can display your text file in your browser : localhost:5000
  
**Using docker-compose**

  Simply run the following command in your repository : 
  > docker-compose up
  
  You can now display your text file in your browser : localhost:5000
