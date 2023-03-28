-- Create stream
CREATE STREAM stream_bank_marketing (
    age INTEGER,
    job STRING,
    marital STRING,
    education STRING,
    default STRING,
    housing STRING,
    loan STRING,
    contact STRING,
    month STRING,
    day_of_week STRING,
    duration INTEGER,
    campaign INTEGER,
    pdays INTEGER,
    previous INTEGER,
    poutcome STRING, 
    emp_var_rate STRING, 
    cons_price_idx DOUBLE, 
    cons_conf_idx DOUBLE,
    euribor3m DOUBLE,
    nr_employed INTEGER,
    y STRING
)
WITH (kafka_topic='bankmarketing', format='json', partitions=1);

/*Create table (materialized view): to calculate how many customers have
subscribed to deposit offers based on time (months and days*/
CREATE TABLE subsbytime AS
  SELECT
    month,
    day_of_week,
    COUNT(y) AS subscribe
FROM stream_bank_marketing
GROUP BY month, day_of_week;