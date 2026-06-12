import contextvars

user_id = contextvars.ContextVar('user_id', default=None)

def process_request(user_id_val):
    token = user_id.set(user_id_val)
    try:
        # Any function can access user_id.get()
        logger.info(f"User: {user_id.get()}")
    finally:
        user_id.reset(token)