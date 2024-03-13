# JumpingMindTask
JumpingMinds Backend Problem Statement  In this challenge, you are asked to implement the business logic for a simplified elevator model in Python. We'll ignore a lot of what goes into a real world elevator, like physics, maintenance overrides, and optimizations for traffic patterns.
 # Elevator System Backend Challenge

## Problem Statement

In this challenge, you are asked to implement the business logic for a simplified elevator model in Python. We'll ignore a lot of what goes into a real-world elevator, like physics, maintenance overrides, and optimizations for traffic patterns. All you are asked to do is to decide whether the elevator should go up, go down, or stop.

### Table of Contents:

- Each elevator has below capabilities
- Elevator System takes care of
- Assumptions
- Asks
- API’s required
- Submission Process and Judging Criteria

### A. Each elevator has below capabilities:

- Move Up and Down
- Open and Close Door
- Start and Stop Running
- Display Current Status
- Decide whether to move up or down, based on a list of requests from users.

### B. Elevator System takes care of:

- Initializing N elevators
- Maintaining elevator states
- Handling requests from users and deciding elevator movements
- Coordinating actions of multiple elevators if there are more than one

### C. Assumptions:

- The elevator system does not consider complex factors like physics, maintenance overrides, or traffic patterns.
- Only basic functionalities as mentioned above are implemented.

### D. Asks:

Implement the business logic for a simplified elevator model in Python using Django.

### E. API’s required:

1. API to receive user requests for elevator movement.
2. API to query the current status of elevators.



- Should include the Python code implemented using Django, including Models, ViewSets, Serializers, etc.
- Judging criteria may include the correctness of the implemented functionalities, code quality, adherence to Django best practices, and efficiency of the elevator system.

Create a simple diagram representing the solution to the elevator system problem statement using Django.
+-------------------------------------------+ 
|             Elevator System               | 
+-------------------------------------------+ 
|               /            \              | 
|    Elevator Management    API Endpoints   |
|               \            /              |
+-------------------------------------------+
|               Models                      |
+-------------------------------------------+
|               Business Logic              |
+-------------------------------------------+
|               Database                    |
+-------------------------------------------+

Business Logic: This layer contains the core business logic of the elevator system. It includes functions and methods for elevator operations like moving up and down, opening and closing doors, determining the next destination floor, etc.

Database: This is the storage layer where data related to the elevator system is stored. It can be a PostgreSQL database as mentioned in the problem statement.


## API Endpoint

The API endpoint for elevators is:
Checking the elevator
[http://127.0.0.1:8001/api/v1/elevators/](http://127.0.0.1:8001/api/v1/elevators/)

output is EndPoint
[
    {
        "id": 1,
        "status": "STOPPED",
        "current_floor": 0
    },
    {
        "id": 2,
        "status": "STOPPED",
        "current_floor": 0
    },
    {
        "id": 3,
        "status": "STOPPED",
        "current_floor": 0
    },
    {
        "id": 4,
        "status": "UP",
        "current_floor": 1
    },
    {
        "id": 5,
        "status": "OPEN",
        "current_floor": 1
    },
    {
        "id": 6,
        "status": "CLOSED",
        "current_floor": 1
    },
    {
        "id": 7,
        "status": "UP",
        "current_floor": 3
    },
    {
        "id": 8,
        "status": "OPEN",
        "current_floor": 3
    },
    {
        "id": 9,
        "status": "CLOSED",
        "current_floor": 3
    },
    {
        "id": 10,
        "status": "DOWN",
        "current_floor": 1
    }
]

Checking the requests
[http://127.0.0.1:8001/api/v1/requests/](http://127.0.0.1:8001/api/v1/requests/)

Output of this endpoint
[
    {
        "id": 1,
        "direction": "UP",
        "target_floor": 1,
        "processed": true,
        "elevator": 1
    }
]

This endpoint allows you to interact with the elevators in the system.

