from distutils.core import setup
setup(name='personis',
      version='1.0',
      py_modules=['Src/connection.py',
                'Src/__init__.py',
                'Src/argparse.py',
                'Src/consumer.py',
                'Src/cronserver.py',
                'Src/Ev_filters.py',
                'Src/jsoncall.py',
                'Src/mypyparsing.py',
                'Src/Personis_a.py',
                'Src/Personis_base.py',
                'Src/Personis_exceptions.py',
                'Src/Personis_mkmodel.py',
                'Src/Personis.py',
                'Src/Personis_server.py',
                'Src/Personis_util.py',
                'Src/Resolvers.py',
                'Src/Subscription.py'],
      )
