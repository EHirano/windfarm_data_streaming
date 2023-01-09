# windfarm_data_streaming
This project simulates IoT data from sensors installed in a wind farm. The data is ingested into AWS using Kinesis Data Stream and Kinesis Data Firehose and stored in an S3 bucket. Then, a Glue Crawler creates a Glue Catalog that is used by a Glue Job to transfer the data to another S3 bucket, which can be then queried using Athena.
