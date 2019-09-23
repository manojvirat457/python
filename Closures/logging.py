import logging
logging.basicConfig(filename='example.log', level=logging.INFO) # Log file details

# Logger function
def logger(func):
    def log_func(*args): # it means this function can have many params
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

# Add Function
def add(x, y):
    return x+y

# Subtract Function
def sub(x, y):
    return x-y

add_logger = logger(add) # the log_func's memory will returned
sub_logger = logger(sub) # the log_func's memory will returned

add_logger(9, 6) # 15
add_logger(4, 5) # 9
sub_logger(10, 5) # 5
sub_logger(20, 10) # 10