import pytest
from ticket_task import tickets


@pytest.mark.parametrize(('moneys', 'expected_result'), [([25, 25, 25, 25, 50, 100, 50], "YES"),
                                                         ([25, 25, 50, 50, 100], "YES")])
def test_counting_tickets(moneys, expected_result):
    '''

    :return:
    '''
    result = tickets(moneys)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"



