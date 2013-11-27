"""Simple lib to handle basic OAuth2 implementation"""

import uuid

TOKEN_MAP = dict()

def generate_token():
  """Create a new token
  """
  return str(uuid.uuid4())


def create_token(user_ctx, scope_list):
  """Create and return a token with this user context and list of scopes.
  """

  data = {'X-Mashery-Oauth-Scope' : scope_list,
          'X-Mashery-Oauth-User-Context' : user_ctx}
  new_token = generate_token()
  TOKEN_MAP[new_token] = data
  return TOKEN_MAP[new_token]


def lookup_token(token):
  """Return the data associated with this token if any
  """
  return TOKEN_MAP[token]


def delete_token(token):
  """Remove this token from the database
  """
  TOKEN_MAP[token] = None
