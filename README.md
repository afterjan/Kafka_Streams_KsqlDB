# Kafka Stream (Streaming Processing)
Stream Processing Data into ksqlDB.

# Prerequisites
1. Java
2. Apache Kafka
3. Confluent
4. Docker

# Steps
1. Create Kafka stacks with Docker Compose.
   ```
   docker-compose up -d
   ```
2. Go to localhost:9021, then create a stream and materialized views in ksqlDB using SQL queries.
3. Run producer.py (ensure to run in the directory that stored the file).
   ``` 
   python producer.py
   ```
   After creating the stream and materialized view, the topics will automatically be created.
   <img width="1440" alt="Topics" src="https://user-images.githubusercontent.com/113230789/228294090-885ca06e-71cf-41e0-a566-5e6277956350.png">
4. The results can be seen directly in the stream or table materialized view by performing a query on ksqlDB as shown in the picture; the results can also be seen in the terminal by running the python consumer file.
   <details>
   <summary>Data in Stream</summary>
   <img width="1442" alt="Data in Stream" src="https://user-images.githubusercontent.com/113230789/228291547-c523af7f-249e-4b09-8699-7ae3acce82dd.png">
   </details>
   <details>
   <summary>Data in table (materialized views)</summary>
   <img width="1441" alt="Data in Table" src="https://user-images.githubusercontent.com/113230789/228292113-9681142d-56a1-4923-b542-a6c0970757b0.png">
   </details>
