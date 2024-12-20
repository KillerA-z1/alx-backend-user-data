#!/usr/bin/env python3
"""Session database authentication module for the API."""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Session database authentication class."""

    def create_session(self, user_id=None):
        """Create and store new instance of UserSession and return
        the Session ID."""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return the User ID by requesting UserSession in the
        database based on session_id."""
        if session_id is None:
            return None
        try:
            user_sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user_sessions:
            return None
        return user_sessions[0].user_id

    def destroy_session(self, request=None):
        """Destroy the UserSession based on the Session ID from the
        request cookie."""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            user_sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not user_sessions:
            return False
        user_session = user_sessions[0]
        user_session.remove()
        return True
