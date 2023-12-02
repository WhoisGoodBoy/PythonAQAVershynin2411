from lesson15.len_example import Company, Building
import pytest

class TestBuilding:
    def setup(self):
        self.building1 = Building('Hilton','Sofiivska sq')

    def setup_class(self):
        print('we`re in setup Class method')

    @pytest.mark.regression
    def test_check_building_length(self):
        self.building1[1] = Company('Kanye west', 'artist')
        self.building1[2] = Company('Kim Kardashian', 'artist')
        assert len(self.building1) == 2

    @pytest.mark.regression
    def test_building_is_opened(self):
        congratulations_message = self.building1.grand_opening()
        assert congratulations_message == 'Congratulations. prepare to live in horror world you built'

    def teardown(self):
        print('we`re in teardown method')

    def teardown_class(self):
        print('we`re in teardown Class method')