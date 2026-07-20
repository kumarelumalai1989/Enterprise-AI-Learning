# Vertical Scaling vs Horizontal Scaling

## What is Vertical Scaling?
Vertical scaling (Scale Up) means increasing the resources of an existing server, such as CPU, RAM, or storage, to handle additional workload.

## Advantages
• Easy to implement
• Minimal architecture changes
• Lower initial cost
• Faster deployment

## Disadvantages
* We can't increase the system CPU and memory size after certain size because Hardware has physical limits.
* Single point of failure.

## What is Horizontal Scaling?
Horizontal scalling means adding more instances to hangle the user request.

## Advantages
• Provides fault tolerance
• High availability
• Better scalability
• Easy to add more servers

## Disadvantages
• More infrastructure cost
• Requires a load balancer
• Health checks
• Monitoring
• More deployment complexity

## Real-world Examples
Customers arrive.
↓
Waiter
↓
Table A
↓
Table B
↓
Table C

The waiter behaves like a Load Balancer by distributing customers among available tables.

## Which one would you choose for an AI Chatbot and why?
AI chatbot initially I would preger vertical scalling because user is low and also I will monitor the request, When monitoring shows sustained high CPU usage, memory pressure, or increased response times, I would first investigate the bottleneck. If a single server can no longer handle the traffic efficiently, I would move to horizontal scaling by adding more application instances behind a load balancer. Depending on the bottleneck, I might also introduce caching (for read-heavy workloads) or optimize the database before adding servers.