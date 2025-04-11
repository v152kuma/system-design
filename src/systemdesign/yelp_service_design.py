from diagrams import Diagram
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
from diagrams.aws.compute import EC2
from diagrams.programming.flowchart import Action

with Diagram("Yelp Service Design", show=False):
    # Load Balancer
    load_balancer = ELB("Load Balancer")

    # Web Servers
    location_based_service = EC2("location_based_service")
    bussiness_service = EC2("bussiness_service")


    # Database
    primary_database = RDS("Primary")
    replica_database = RDS("Replica")
    replica_database2 = RDS("Replica 2")
    replica_database3 = RDS("Replica 3")
    primary_database >> replica_database
    primary_database >> replica_database2
    primary_database >> replica_database3
    database = [primary_database, replica_database, replica_database2, replica_database3]
    


    # Connections
    load_balancer >> [location_based_service, bussiness_service]
    [location_based_service] >> replica_database
    [location_based_service] >> replica_database2
    [location_based_service] >> replica_database3
    [bussiness_service] >> primary_database