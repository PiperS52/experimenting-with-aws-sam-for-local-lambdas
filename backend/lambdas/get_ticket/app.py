import psycopg2
import json
import os   

def lambda_handler(event, context):
    ticket_id = event['pathParameters']['id']

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
        cursor.execute("SELECT * FROM tickets WHERE id = %s", (ticket_id,))
        ticket = cursor.fetchone()

        colnames = [desc[0] for desc in cursor.description]

        def serialize(row):
            return {
                col: (val.isoformat() if hasattr(val, "isoformat") else val)
                for col, val in zip(colnames, row)
            }
        
        ticket_serialized = serialize(ticket)
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps(ticket_serialized)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }