# Load Balancer

## What is Load Balancer?
A Load Balancer is a server (or service) that sits between clients and application servers and distributes incoming requests across multiple servers.

Architecture:

              Users
                 │
                 ▼
          +----------------+
          | Load Balancer  |
          +----------------+
           /      |      \
          /       |       \
         ▼        ▼        ▼
   Server 1  Server 2  Server 3

## Why do we need it?
### 1. Better Performance
Instead of handling all the request by one server. Load balance split the request among all the available servers. 

### 2. High Availablity
If server 2 crash then load balancer send the request to the remaining available server. So application continuous running.

### 3. Scalablity
If user request incrasing more then we will add more servers to the load balancer without any code changes.

## Types

- Layer 4(Transport Layer)
- Layer 7
### Layer 4:
* When the user connects, the load balancer only knows
```
Source IP        : 192.168.1.10
Destination IP   : 20.10.15.40
Protocol         : TCP
Destination Port : 443
``` 
* It doesn't know:
It doesn't know:
❌ /chat
❌ /upload
❌ /search
❌ HTTP Headers
❌ Cookies
❌ JWT Token

It only knows:
"Someone wants to connect to port 443."

## Algorithms

- Round Robin
- Least Connections
- IP Hash
- Weighted Round Robin

### Round Robin:
* Request are distributed one by one.
* Example: If we have 3 servers(Server A, Server B, Server C).
   Request 1 -> Server A
   Request 2 -> Server B
   Request 3 -> Server C
   Request 4 -> Server A
   Request 5 -> Server B
* Best when servers have similar capacity

### Lease Connection:
* Instead of equal distribution, choose the server with fewest active users.
* Example:
  Server A → 100 users
  Server B → 30 users
  Server C → 20 users
* Good when request have different processing times.

### IP Hash:
* Request from the same client IP always go to the same server.
* Useful For:
  -> Shopping Carts
  -> Banking session
  -> Gaming

### Weighted Round Robin
* Suppose Servers are different
```
Server A
32 CPU
128 GB RAM

Server B
8 CPU
32 GB RAM
```
* Both server receives same traffic? No
* Assign Weights
```
Server A -> 70%
Server B -> 30%
```

## Health Check
* Most important feature
* Suppose 
```
Server B crashes
```
How does the load balancer know? 
Load balancer send request 'Get /Health'
 -> If the server replies 200 Ok then server is 'healthy'.
 -> If no response/timeout then mark it unhealthy and load balancer stop sending request to Server B.

## Real-world Example

## AI Chatbot Example

## Advantages

## Disadvantages