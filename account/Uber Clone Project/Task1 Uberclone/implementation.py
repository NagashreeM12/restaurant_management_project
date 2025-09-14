import time

class SessionManager:
    def __init__(self, expiry_seconds: int):
        """
        Initialize the session manager.
        :param expiry_seconds: Session validity in seconds.
        """
        self.expiry_seconds = expiry_seconds
        self.sessions = {}  # {session_id: creation_time}

    def create_session(self, session_id: str) -> str:
        """
        Create a new session.
        :param session_id: Unique session identifier.
        :return: Confirmation message.
        """
        self.sessions[session_id] = time.time()
        return f"Session '{session_id}' created."

    def is_session_active(self, session_id: str) -> bool:
        """
        Check if a session is active.
        :param session_id: Unique session identifier.
        :return: True if active, else False.
        """
        if session_id not in self.sessions:
            return False

        creation_time = self.sessions[session_id]
        if time.time() - creation_time <= self.expiry_seconds:
            return True
        else:
            # Session expired → delete automatically
            del self.sessions[session_id]
            return False

    def delete_session(self, session_id: str) -> str:
        """
        Delete a session manually.
        :param session_id: Unique session identifier.
        :return: "Deleted" if found, else "Not Found".
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return "Deleted"
        return "Not Found"
if __name__ == "__main__":
    sm = SessionManager(expiry_seconds=3)  # sessions last 3 seconds

    print(sm.create_session("driver123"))        # Create session
    print(sm.is_session_active("driver123"))     # True (active)

    time.sleep(2)  # wait 2 seconds
    print(sm.is_session_active("driver123"))     # True (still active)

    time.sleep(2)  # wait 2 more seconds (total 4 > expiry)
    print(sm.is_session_active("driver123"))     # False (expired)

    print(sm.delete_session("driver123"))        # "Not Found" (already expired)
    print(sm.create_session("rider456"))         # New session
    print(sm.delete_session("rider456"))         # "Deleted"