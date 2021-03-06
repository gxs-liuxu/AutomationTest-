#coding:utf-8
from config.api_config import *
from public.common.common import *
from public.requests_handle import *
from public.xlrd_handle import *
from public.api_test.api_global import *
from public.api_test.api_main import *
from scripts.single_scripts.divine_budget import divine_budget_main
from scripts.single_scripts.publish_jn import create_jn
from public.report.report_currency import *
from public.api_test.api_test_case import  *
import HTMLTestRunner
import unittest


if __name__ == '__main__':

    # 神力值
    #divine_budget_main()

    #锦囊发布
    create_jn(3)

    # 接口轮询
    #api_currency_requests()
    # print currency
    # api_common_requests()
    '''
    suite = unittest.TestSuite()

    #apiTestCase.
    
    apiTestCase.loop_create_function(['00000004','00000005','00000006'])
    aaa = apiTestCase("test_api_index")
    print dir(apiTestCase)
    
    #print apiTestCase.__class__.__name__

    #tests = [apiTestCase("test_api_index","00000004"), apiTestCase("test_show"),apiTestCase("test_row"),apiTestCase("test_api_index","00000003"),apiTestCase("test_111"),apiTestCase("test_111"),apiTestCase("test_00000001",'00000004',1)]
    tests = [apiTestCase("test_show")]
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    



    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(apiTestCase))
    
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                title='测试报告',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)
    '''
