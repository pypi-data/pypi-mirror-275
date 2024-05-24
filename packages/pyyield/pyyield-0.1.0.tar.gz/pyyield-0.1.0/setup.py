from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="pyyield",  # as it would be imported
            # may include packages/namespaces separated by `.`
            sources=[
                "src/pyyieldModule.cpp"
            ],  # all sources are compiled into a single binary file
        ),
    ]
)
