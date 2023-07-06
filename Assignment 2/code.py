import logging
logging.basicConfig()
logger = logging.getLogger()

def divide_numbers(a, b):
    try:
        # Add a logging statement here to log the division operation
        logger.setLevel(logging.INFO)
        logger.info("Variable a will be divided by variable b")
        result = a / b
        # Add a logging statement here to log the result of the division
        logger.info("A/B is equal to :"+str(result))

        return result
    except ZeroDivisionError as e:
        logger.error("ZeroDivisionError: Cannot divide the number by zero")
        raise e
    except Exception as e:
        logger.error("Try again, some error occured")
        raise e

def perform_task(a, b):
    try:
        # Add a logging statement here to log the start of the task
        result = divide_numbers(a, b)
        
        # Add a logging statement here to log the successful completion of the task
    except Exception as e:
        # Add a logging statement here to log the task failure
        # Handle the exception or take appropriate actions
        pass



# Example usage
perform_task(10, "s")
