Anotações sobre o curso e vídeos: EDUREKA HADOOP CERTIFICATION TRAINING

**HADOOP ECOSYSTEM:** #Hadoop alone doesn't solve all the problems - other tools are necessary.

**HDFS -> Hadoop Distributed File System**
- Stores different types of large data sets (i.e. structured, unstructed and semi structured data)
- HDFS creates a level of abstraction over the resources, from where we can see the whole HDFS as a single unit
- Stores data across various nodes and maintains the log file about the stored data (metadata)
- HDFS has two core components, i.e. NameNode (manages the entire cluster) and DataNode (slave machines that actually store the data)

**YARN -> Yet Another Resource Negotiator**
- Performs all your processing activities by allocating resources and scheduling tasks
- Two services: ResourceManager and NodeManager
- ResourceManager: Manages resources and schedule applications running on top of YARN
- NodeManager: Manages containers and monitors resource utilization in each container

**MapReduce -> Data processing using programming**
- Core component in a Hadoop Ecosystem for processing
- Helps in writing applications that processes large data sets using distributed and parallel algorithms
- In a MapRecude program, Map() and Reduce() are two functions
- Map function performs actions like filtering, grouping and sorting
- Reduce function aggregates and summarizes the result produced by map function

**PIG, HIVE -> Data Processing Services using Query (SQL-like)**
- PIG has two parts: Pig Latin, the language and the pig runtime, for the execution environment
- 1 line of pig latin = aprox. 100 lines of Map-Reduce job
- The compiler internally converts pig latin to Map Reduce
- It gives you a platform for building data flow for ETL (Extract, Transform and Load)

- PIG first loads the data, then performs various functions like grouping, filtering, joining, sorting, etc. and finally dumps the data on the screen or stores in HDFS

- HIVE is a data warehousing component which analyses data sets in a distributed environment using SQL-like interface
- The query language of Hive is called Hive Query Language (HQL)
- 2 basic components: Hive Command Line and JDBC/ODBC driver
- Supports user functions UDF) to accomplish specific needs

**Mahout, Spark MLlib -> Machine Learning**
- Provides an environment for creating machine learning applications
- It performs collaborative filtering, clustering and classification
- Provides a command line to invoke various algorithms
- It has a predefined set of library which already contains different inbuilt algorithms for different use cases
- (Can be used to create recommendation engines and clusters of data)

**(Apache) Spark -> In-memory Data Processing**
- A leading tool in Hadoop Ecosystem
- A framework for real time data analytics in a distributed computing environment
- Written in Scala and originally developed at the University of California, Barkeley
- Executes in-memory computations to increase speed of data processing over Map-Reduce
- Almost 100x faster than Hadoop for large scale data processing by exploiting in-memory computations
- (Connect to HDFS and leverage it)

**(Apache) HBase -> NoSQL Database**
- An open source, non-relational distributed database (a NoSQL database)
- Supports all typed of data and that is why it's capable of handling anything and everything
- Modelled after Google's BigTable
- Provides a fault tolerant way of storing sparse data
- Written in Java, and its applications can be written in REST, Avro and Thrift APIs

**Apache Drill -> SQL on Hadoop**
- An open-source application which works with distributed environment to analyze large data sets
- Follows the ANSI SQL
- Supports different kinds of NoSQL databases and file systems
- For example: Azure Blob Storage, Google Cloud Storage, HBase, MongoDB, MapR-DB HDFS, MapR-FS, Amazon S3, Swift, NAS and local files
- Combines a variety of data stores just by using a single query
- (You can connect to, for example, three databases at once, execute one query and extract the result from all the three databases to use for your application)

**(Apache) Oozie -> Job Scheduling**
- Oozie is a job shceduler in Hadoop Ecosystem
- Two kinds of Oozie jobs:
- Oozie Workflow: Sequential set of actions to be executed
- Oozie Coordinator: Oozie jobs which are triggered when the data is made available to it or even triggered based on time

**Flume, Sqoop -> Data Ingesting Services**
- Flume ingests unstructured and semi-structured data into HDFS
- Helps in collecting, aggregating and moving large amount of data sets
- Helps to ingest online streaming data from various sources like network, traffic, social media, email massages, log files etc. in HDFS

- (Apache) Sqoop is another data ingesting service
- Sqoop can import as well as export structured data from RDBMS
- Flume only ingests unstructured data or semi-structured data into HDFS

**Solr & Lucene -> Searching & Indexing**
- Two services which are used for searching and indexing in Hadoop Ecosystem
- Apache Lucene is based on Java, which also helps in spell checking
- Apache Lucene is the engine while Apache Solr is a complete application built around Lucene
- Sorl uses Apache Lucene Java search library for searching and indexing

**Zookeeper -> Managing Cluster**
- An open-source server which enables highly reliable distributed coordination
- Apache Zookeeper coordinates with various Hadoop services in a distributed environment
- Performs synchronization, configuration maintenance, grouping and naming

**(Apache) Ambari -> Cluster provision, Monitoring and Maintainance**
- Software for provisioning, managing and monitoring Apache Hadoop clusters
- Gives us step by step process for installing Hadoop services
- Handles configuration of Hadoop services
- Provides a central management service for starting, stopping and re-configuring Hadoop services
- Monitors health and status of the Hadoop cluster
_____________________________________________________________________________________________________________________________________________________________________________

**HADOOP ARCHITECTURE:**

*1. Hadoop Components*
	Hadoop 2.x Core Components:
		      |
Storage:			Processing:
-> HDFS	|			| YARN(MapReduce/MRv2) <-
	NameNode > Master < ResourceManager
	DataNote > Slave < NodeManager

*2. DFS - Distributed File System*
NameNode:
- Master daemon
- Maintains and Manages DataNodes
- Records metadata e.g.location of blocks stored, the size of the files, permissions, hierarchy, etc
- Receives heartbeat and block report from all the DataNodes

DataNode (Commodity Hardware):
- Slave daemons
- Stores actual data
- Serves read and write requests from the clients

*3. Hadoop Services*

*4. Blocks in Hadoop*
- Each file is stored on HDFS as blocks
- The default size of each block is 128MB in Apache Hadoop 2.x (64MG in Apache Hadoop 1.x)
>How many blocks will be created if a file of size 514MB is copied to HDFS?
>Example_file.txt (514MB)
>Answer: 5 blocks: file_a (128MB), file_b (128MB), file_c (128MB), file_d (128MB), file_e (2MB)

*5. Block Replication*
>Is it safe to have just 1 copy of each block?
>Answer: There are multiple copies present in other DataNodes
- Every block is replicated 3x = 3 copies of each file
- If you copy 1GB of a file into Hadoop Distributed File System, it's actually storing 3GB of files in HDFS.

*6. Rack Awareness*
>How does Hadoop decide where to store the replicas of the blocks created?
Example:
- Block A, Block B, Block C
- Rack-1, Rack-2, Rack-3
- If Block A is created in Rack-1, the replicas can only be stored on Racks 2 and 3
- (More than one replica can be stored in the same Rack)
- (Why store 2 copies in the same rack? Bandwidth)

*7. HDFS Architecture*

*8. HDFS Read/Write Mechanism*
- Write Mechanism:
- Clients connect to the DataNodes, if they're ready, at the same time.
- The Write Request goes to Block A (or Replica 1), then it passes to the second and third replica.
- The very first copy of every block will be created paralelly, not sequentially
- The replicas of those blocks are created sequentially by their subsequent DataNodes
- Blocks are written in paralel and replicas are created in sequence

- Read Mechanism:
- Clients send a Read Request to the NameNode, then the NameNode sends back the IP addresses of the DataNodes which contain the file


**HDFS COMMANDS:**
- hadoop version - Check Hadoop's Version
- hdfs fsck / - Check HDFS Health
- hdfs dfs -ls / - List all the HDFS files/directories
- hdfs dfs -put /home/edureka/test /user - Copy data from local system to HDFS
- hdfs dfs -help - List os commands

**Learning Resources:**
- Hadoop Tutorial: www.edureka.co/blog/hadoop-tutorial
- HDFS Tutorial: www.edureka.co/blog/hdfs-tutorial
- Hadoop Architecture: www.edureka.co/blog/apache-hadoop-hdfs-architecture
