import unittest

from pandas import DataFrame

from brFinance.scraper.cvm.search import SearchDFP
from brFinance.utils.browser import Browser


class TestSearchDFP(unittest.TestCase):
    RESULTS_COLUMNS = ['Código CVM', 'Empresa', 'Categoria', 'Tipo', 'Espécie', 'Data Referência', 'Data Entrega',
                       'Status', 'V', 'Modalidade', 'linkView', 'linkDownload']

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().setUpClass()

    def setUp(self):
        self.driver = Browser.run_chromedriver()
        self.search_object = SearchDFP(driver=self.driver)
        self.search_result = self.search_object.search(cvm_code=21610)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_search_returns_a_dataframe(self):
        self.assertIsInstance(self.search_result, DataFrame,
                              msg="get_search_results returned does not returned a Pandas DataFrame for categoria=21.")

    def test_search_returns_desired_columns(self):
        self.assertEqual(list(self.search_result.columns), TestSearchDFP.RESULTS_COLUMNS,
                         msg="Wrong columns in the financial_reports_search_result ")

    def test_search_dataframe_has_values(self):
        self.assertGreater(len(self.search_result), 0, msg="No results found to cod_cvm = 21610 and category=21")

    def test_assert_raises_for_cvm_code(self):
        # Test if raises exception for invalid CVM code
        self.assertRaises(AssertionError, self.search_object.search, cvm_code=2)
