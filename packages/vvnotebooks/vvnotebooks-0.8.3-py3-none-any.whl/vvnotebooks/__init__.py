import os.path, yaml

configs = None
def config(file = None):
  """
  Memoize the configuration from the named file,
  interpreted as a YAML file, and return it.
  """

  global configs

  if file is None:
    file = 'notebook.yml'

  if configs is None:
    if not os.path.exists(file):
      print(f'Configuration file "{file}" not found, you may want to create it first.')
      return None

    with open(file) as f:
      configs = yaml.safe_load(f)

  return configs

def config_needed(pattern, file = None):
  """
  Assert (and communicate) requirements for notebook
  configuration, by checking a pattern object against
  the actual configuration parsed from the given file.

  Objects in the pattern are processed recursively,
  and string _values_ are taken as error messages to
  emit when the preceding keys have not been found.
  def check_config(obj, prefix, pattern):
  """

  def check_config(obj, prefix, pattern):
    """
    A helper function to recursively check a pattern
    against a real configuration (sub-)object.
    """

    ok = True
    for k in pattern:
      if not k in obj:
        if type(pattern[k]) == str:
          print(f'[{file}] Missing {prefix}.{k}: {pattern[k]}')
        else:
          print(f'[{file}] Missing {prefix}.{k}.* configuration')
        ok = False
      elif type(pattern[k]) != str:
        if not check_config(obj[k], f'{prefix}.{k}', pattern[k]):
          ok = False
    return ok

  if file is None:
    file = 'notebook.yml'
  return check_config(config(file), '$', pattern)
