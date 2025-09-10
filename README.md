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
make
