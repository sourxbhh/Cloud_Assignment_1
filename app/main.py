import os
import sys
import time
import json
import psycopg

# Get database connection details from environment variables with defaults [cite: 112-120]
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "secretpw")
DB_NAME = os.getenv("DB_NAME", "appdb")
TOP_N = int(os.getenv("APP_TOP_N", "5"))

def connect_with_retry(retries=10, delay=2):
    """Attempt to connect to the database with retries."""
    last_err = None
    for i in range(retries):
        try:
            # Attempt to connect to the database
            conn = psycopg.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASS,
                dbname=DB_NAME,
                connect_timeout=3,
            )
            print("Successfully connected to the database!")
            return conn
        except Exception as e:
            last_err = e
            print(f"Waiting for database... (attempt {i+1}/{retries})", file=sys.stderr)
            time.sleep(delay)
    # If all retries fail, print error and exit [cite: 140]
    print("Failed to connect to Postgres:", last_err, file=sys.stderr)
    sys.exit(1)

def main():
    """Main function to query database and generate summary."""
    conn = connect_with_retry()
    # Use a 'with' statement to ensure the connection is closed
    with conn, conn.cursor() as cur:
        # 1. Query for the total number of trips
        cur.execute("SELECT COUNT(*) FROM trips;")
        total_trips = cur.fetchone()[0]

        # 2. Query for the average fare by city
        cur.execute("SELECT city, AVG(fare) FROM trips GROUP BY city ORDER BY city;")
        by_city = [{"city": c, "avg_fare": float(a)} for (c, a) in cur.fetchall()]

        # 3. Query for the top N longest trips
        cur.execute("SELECT city, minutes, fare FROM trips ORDER BY minutes DESC LIMIT %s;", (TOP_N,))
        top_trips_raw = cur.fetchall()
        top = [
            {"city": row[0], "minutes": row[1], "fare": float(row[2])}
            for row in top_trips_raw
        ]
        
        # Assemble the final summary dictionary [cite: 157-160]
        summary = {
            "total_trips": int(total_trips),
            "avg_fare_by_city": by_city,
            "top_n_longest_trips": top
        }

        # Write the summary to a JSON file in the /out directory [cite: 161-163]
        os.makedirs("/out", exist_ok=True)
        with open("/out/summary.json", "w") as f:
            json.dump(summary, f, indent=2)
        
        # Print the summary to standard output [cite: 164-166]
        print("\n=== Summary ===")
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()