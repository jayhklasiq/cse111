from final_project import get_otp, sys_data
import pytest
def test_sys_data():
    KEY_INDEX = 0
    filename = ('wk12\coded_files\username.csv')
    with pytest.raises(FileNotFoundError, FileExistsError):
        sys_data(filename, KEY_INDEX)
        pytest.fail('sys_data function must use its filename parameter')
        
    filename = path.join(path.dirname(__file__), "products.csv")
    products_dict = read_dictionary(filename, PRODUCT_NUM_INDEX)
        
pytest.main(["-v", "--tb=line", "-rN", __file__])        