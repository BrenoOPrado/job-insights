from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    file = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for item in file:
        assert "title" in item
        assert "salary" in item
        assert "type" in item
