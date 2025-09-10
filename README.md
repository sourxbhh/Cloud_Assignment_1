# Assignment #1 – Docker Containers

This project demonstrates a **two-container stack** using Docker and Docker Compose.  
- **Service 1:** A PostgreSQL database preloaded with sample trip data.  
- **Service 2:** A lightweight Python app that connects to the database, queries trip records, computes statistics, and saves the results to `/out/summary.json`.  

This assignment introduces the fundamentals of multi-container setups, service networking, environment variables, and reproducible workflows.

---

## 🚀 How to Run

### Prerequisites
- Docker Desktop  
- Docker Compose  
- GitHub Desktop (or git CLI)  
- Any IDE (VS Code, PyCharm, etc.)

Verify that:
- Port **5432** is free, or update the `compose.yml` file.
- You can run basic Docker commands (`docker build`, `docker run`, etc.).

---

### One-command run (recommended)
```bash
docker compose up
```

## Obtained output:

```bash
Successfully connected to the database!                                                                                                           
app-1  | 
app-1  | === Summary ===                                                                                                                                   
app-1  | {
app-1  |   "total_trips": 6,                                                                                                                               
app-1  |   "avg_fare_by_city": [
app-1  |     {                                                                                                                                             
app-1  |       "city": "Charlotte",                                                                                                                        
app-1  |       "avg_fare": 16.25                                                                                                                           
app-1  |     },                                                                                                                                            
app-1  |     {
app-1  |       "city": "New York",                                                                                                                         
app-1  |       "avg_fare": 19.0                                                                                                                            
app-1  |     },                                                                                                                                            
app-1  |     {
app-1  |       "city": "San Francisco",                                                                                                                    
app-1  |       "avg_fare": 20.25                                                                                                                           
app-1  |     }                                                                                                                                             
app-1  |   ],
app-1  |   "top_n_longest_trips": [                                                                                                                        
app-1  |     {
app-1  |       "city": "San Francisco",                                                                                                                    
app-1  |       "minutes": 28,                                                                                                                              
app-1  |       "fare": 29.3                                                                                                                                
app-1  |     },                                                                                                                                            
app-1  |     {                                                                                                                                             
app-1  |       "city": "New York",
app-1  |       "minutes": 26,                                                                                                                              
app-1  |       "fare": 27.1                                                                                                                                
app-1  |     },                                                                                                                                            
app-1  |     {                                                                                                                                             
app-1  |       "city": "Charlotte",                                                                                                                        
app-1  |       "minutes": 21,
app-1  |       "fare": 20.0                                                                                                                                
app-1  |     },                                                                                                                                            
app-1  |     {                                                                                                                                             
app-1  |       "city": "Charlotte",                                                                                                                        
app-1  |       "minutes": 12,                                                                                                                              
app-1  |       "fare": 12.5                                                                                                                                
app-1  |     },
app-1  |     {                                                                                                                                             
app-1  |       "city": "San Francisco",                                                                                                                    
app-1  |       "minutes": 11,                                                                                                                              
app-1  |       "fare": 11.2                                                                                                                                
app-1  |     }                                                                                                                                             
app-1  |   ]
app-1  | }                                                                                                                                                 
app-1 exited with code 0
```
