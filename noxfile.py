import nox


@nox.session()
@nox.parametrize(
    "pandas,numpy,scipy",
    [
        (pandas, numpy, scipy)
        for pandas in ("0.24.1", "0.25.3", "1.0")
        for numpy in ("1.17.4", "1.19.5")
        for scipy in ("1.5.0", "1.6.1")
    ],
)
def tests(session, pandas, numpy, scipy):

    session.run("python", "-m", "pip", "install", "--upgrade", "pip")
    session.install("pytest")
    session.install(f"numpy=={numpy}", "--no-deps")
    session.install(f"pandas=={pandas}")
    session.install(f"scipy=={scipy}", "--no-deps")

    session.run("pytest", "-v", "-W", "ignore::DeprecationWarning")
