# with requests <=2.23.0, requests forced a re-import of ssl libs.
# Once it stopped doing that, the ssl module was imported somewhere
# before eventlet monkey patching occurred, resulting in some
# infinite recursion errors. Putting this in the base test file
# or in the individual test files was not soon enough. Putting this
# here does, however, seem to be early enough to resolve the errors.
from st2common.util.monkey_patch import monkey_patch

monkey_patch()
