import json

def lambda_handler(event, context):
    # Extract numbers from the event
    number1 = event.get('number1')
    number2 = event.get('number2')
    
    # Check if both numbers are provided
    if number1 is None or number2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Both numbers must be provided.')
        }
    
    # Ensure the numbers are valid
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Both inputs must be valid numbers.')
        }
    
    # Add the numbers
    result = number1 + number2
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }
