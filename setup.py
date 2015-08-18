from setuptools import setup, find_packages


name = "kpss"
version = "0.1"
requires = ["setuptools==1.4.2"]


###########################################
# probably no need to edit anything below #
###########################################

kwargs = {
    "name": name,
    "version": version,
    "packages": find_packages(exclude=["tests", "tests.*"]),
    "namespace_packages": ["kpss"],
    "install_requires": requires,
    "test_suite": "nose.collector",
    "tests_require": ["nose"],
    "zip_safe": True
}
kwargs["entry_points"] = {
    # buildout.cfg should be used instead to define entry points,
    # unless they are suitable to be installed globally
    "console_scripts": [
        name + " = " + name + ":main"
    ],
    "setuptools.installation": [
        "eggsecutable = " + name + ":main",
    ]
}
setup(**kwargs)
