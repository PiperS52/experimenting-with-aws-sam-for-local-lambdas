import os
import json
import psycopg2

def lambda_handler(event, context):
    print('new event...', event)
    # Database connection parameters
    db_host = os.getenv('DB_HOST', 'postgres')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'tickets')
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', 'postgres')

    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()
        
        # Execute a simple query
        cursor.execute("SELECT * FROM tickets;")
        tickets = cursor.fetchall()
        print('line 26', tickets)

        # Convert rows to dicts and serialize dates
        def serialize(row):
            return [
                str(item) if hasattr(item, 'isoformat') else item
                for item in row
            ]
        tickets_serialized = [serialize(row) for row in tickets]

        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps(tickets_serialized)
                               
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }   