from snowflake.snowpark import Session
from snowflake.snowpark.version import VERSION
import vvnotebooks as vv

session = None
def connect():
  """
  Connect to Snowflake, using the 'snowflake' sub-config
  from the currently loaded configuration.  Details about
  the connection, including current role/database/schema,
  and server and client software versions, is printed upon
  a successful connection + authentication.
  """

  global session
  if not vv.config_needed({
    'snowflake': {
      'account':   'What is the locator / identifier for your Snowflake account?',
      'user':      'Who do you sign into Snowflake as?',
      'password':  'What is your Snowflake secret password?'
    }
  }):
    return None

  session = Session.builder.configs(vv.config()['snowflake']).create()
  sf_env = session.sql('select current_user(), current_version()').collect()
  print('❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️')
  print('❄️ Connected to Snowflake:')
  print('❄️ User                        : {}'.format(sf_env[0][0]))
  print('❄️ Role                        : {}'.format(session.get_current_role()))
  print('❄️ Database                    : {}'.format(session.get_current_database()))
  print('❄️ Schema                      : {}'.format(session.get_current_schema()))
  print('❄️ Warehouse                   : {}'.format(session.get_current_warehouse()))
  print('❄️ Snowflake version           : {}'.format(sf_env[0][1]))
  print('❄️ Snowpark for Python version : {}.{}.{}'.format(VERSION[0],VERSION[1],VERSION[2]))
  print('❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️')
  return session

def query(sql):
  """
  Run a single SELECT query and return its resultset
  as a Pandas dataframe.
  """
  return session.sql(sql).to_pandas()

def count(sql):
  """
  Run a single SELECT query and print the number of
  rows in its resultset to the notebook output stream.
  """
  n = len(session.sql(sql).collect())
  s = '' if n == 1 else 's'
  print(f'{n} record{s} found.')

def sign():
  """
  Sign the current notebook as the authenticated
  Snowflake user, generating a time-sensitive hash
  to help with versioning.
  """
  r = session.sql('''
select current_date as today,
       left(md5(current_timestamp), 11) as sig,
       current_user() as who
''').collect()
  print(f'verified {r[0][0]} sig {r[0][1]} by {r[0][2]}')
