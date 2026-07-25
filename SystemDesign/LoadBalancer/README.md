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
Instead of handling all the request by one server. The Load Balancer distributes requests among multiple servers.

### 2. High Availablity
If server 2 crash then load balancer send the request to the remaining available server. So application continuous running.

### 3. Scalablity
If user traffic increases more then we will add more servers to the load balancer without any code changes.

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

### Layer 7:
* The Layer 7 Load Balancer inspects the HTTP request, including the URL, headers, cookies, host name, and HTTP method, before routing the request.
* Example: If user send the request '/Chat', layer 7 identify the request and send the request to the AI chat server. '/Upload' then it will identify the request and route the traffic to the storage server. '/Search' then it will identify and route the request to the RAG search service.


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
The Load Balancer periodically sends a health check request such as:
GET /health
 -> If the server replies 200 Ok then server is 'healthy'.
 -> If no response/timeout then mark it unhealthy and load balancer stop sending request to Server B.

## Real-world Example
* If we are going to the restaurant and waiter send customer 1 to the table 1, customer 2 to the table 2 and customer 3 to the table 3. 
* The waiter acts as a Load Balancer.
*                     Internet
                         │
                         ▼
                Load Balancer
                  /    |    \
                 ▼     ▼     ▼
           FastAPI1 FastAPI2 FastAPI3
                 │
                 ▼
              Redis Cache
                 │
                 ▼
            Vector Database
                 │
                 ▼
              Azure OpenAI

## AI Chatbot Example
### Architecture 1: Every FastAPI server has the same code.
* ```
  FastAPI1
  FastAPI2
  FastAPI3
  ```
* Layer 4 is enough.
### Architecture 2: Microservices.
* ```
  Chat Service
  Upload Service
  Search Service
  ```
* Layer 7.
* Example: search service could be host in different server, chat service could be in different server and file upload should be in the storage server.
* So to handle all these request we would have Layer 7 application gateway.
* The Layer 7 Load Balancer inspects the HTTP request, URL, header, cahce. Based on the content it will route the traffic to the respective server.
* For example, In AI chatbot application user want to serach anything then request will route to the RAG search server. '/Upload' request will forward to the file upload server.

## Advantages
* Load Balancer helps avoid a single point of failure by redirecting traffic to healthy servers.
* A Layer 7 Load Balancer can inspect HTTP requests and route them to the appropriate backend service.
* If any server crashed it will forward the request to the remaining servers.

## Disadvantages
* Cost is more expensive
* Need more servers to handle the request.

## Request Flow
          ```
          User
           ↓
          DNS
           ↓
        Load Balancer
           ↓
        FastAPI
           ↓
        Redis Cache
           ↓
        Vector Database
           ↓
        Azure OpenAI
           ↓
        Response
           ↓
          User
          ```

## Interview Questions

### Why not use one large server?
Although vertical scaling is simple, it has hardware limits and creates a single point of failure.

Horizontal scaling with a Load Balancer provides better scalability, fault tolerance, and availability.
----------------------------------------

### When would you choose Layer 4?
When every backend server runs the same application.
----------------------------------------

### When would you choose Layer 7?
When routing decisions depend on URLs, headers, cookies, or HTTP methods.
----------------------------------------

### Why is Layer 4 faster?
Because it works at the TCP/UDP level and doesn't inspect HTTP requests.
----------------------------------------

### Why don't we use Layer 7 everywhere?
Although Layer 7 provides intelligent routing, it performs additional processing by inspecting HTTP requests. If all backend servers are identical and only TCP/UDP distribution traffic is required, Layer 4 is simpler, faster, and better enough.
-----------------------------------------

### Why is a Health Check important?
* A Load Balancer continuously checks the health of backend servers.
* If a server becomes unhealthy, the Load Balancer stops routing requests to it.
* This improves application availability and prevents users from receiving errors.
-----------------------------------------

### What happens if the Load Balancer itself fails?
* The Load Balancer can become a single point of failure.
* In production, organizations usually deploy multiple Load Balancers or use managed cloud Load Balancer services with built-in redundancy.