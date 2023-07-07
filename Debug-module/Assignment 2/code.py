import logging
logging.basicConfig(filename="codeLog.log",format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
logger = logging.getLogger()

def divide_numbers(a, b):
    try:
        # Add a logging statement here to log the division operation
        logger.setLevel(logging.INFO)
        logger.info("Variable a will be divided by variable b")
        logger.warning("Make sure that the denominator is not zero.")
        # result = a / b
        a=10 
        b=int('valueerror') 
        
        result = a / b + "s"

        # Add a logging statement here to log the result of the division
        logger.setLevel(logging.INFO)
        logger.info("A/B is equal to :"+str(result))

        return result
    except ZeroDivisionError as e:
        logger.error("ZeroDivisionError: Cannot divide the number by zero")
        raise e
    except ValueError as e:
        logger.exception("Exception occurred: %s", str(e))
    except Exception as e:
        logger.error("Try again, error occured ")
        raise e

def perform_task(a, b):
    try:
        # Add a logging statement here to log the start of the task
        logger.info("Dividing the numbers")
        result = divide_numbers(a, b)
        # a = 2/0
        logger.info("Successfully completed the operation")
        # Add a logging statement here to log the successful completion of the task
        
    except Exception as e:
        # Add a logging statement here to log the task failure
        # Handle the exception or take appropriate actions
        logger.error(e)
        raise e



# Example usage
perform_task(10, 2)
