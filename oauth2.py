"""Simple lib to handle basic OAuth2 implementation"""


def create_token(user_ctx, scope_list):
  """Create and return a token with this user context and list of scopes.
  """
  user_scopes = user_data.get('X-Mashery-Oauth-Scope')
  user_ctx = user_data.get('X-Mashery-Oauth-User-Context')
  pass


def lookup_token(token):
  """Return the data associated with this token if any
  """
  pass


def delete_token(token):
  """Remove this token from the database
  """
