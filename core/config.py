import environ

env = environ.Env()
environ.Env.read_env('../.env')


API_KEY = env('NP_API_KEY')