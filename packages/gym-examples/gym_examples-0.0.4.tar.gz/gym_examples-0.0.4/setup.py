from setuptools import setup

setup(
    name="gym_examples",
    version="0.0.4",
    install_requires=["numpy", "gym==0.21.0",
                      "scipy", "msgpack_numpy", 
                      "tqdm", "msgpack"],
)
