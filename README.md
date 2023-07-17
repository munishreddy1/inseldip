# Master_thesis
Development of an API for collecting data from PLC and storing it in a database

The API first builds a connection with the server using its URL and retrieves the data using TCP/IP protocol and the GET method. The retrieved data will be processed based on the Digital twin requirements and then stored in the PostgreSQL database with the help of the psycopg2 library. 

Also, the docker image was built and deployed in the industrial rev pi. I used official postgreSQL and pgadmin docker images and configured them. 

A custom docker overlay network was created to establish seamless communication between multiple nodes as the database container is running on the server and API on rev pi IIOT.
