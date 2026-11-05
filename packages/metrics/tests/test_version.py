import ductus_metrics


# Verifică faptul că pachetul se importă și are o versiune declarată
def test_version_exists():
    assert ductus_metrics.__version__
