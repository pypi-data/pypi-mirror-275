import os, sys
import pytuflow as tu
if sys.version_info[0] == 3:
    import unittest
else:
    import unittest2 as unittest
from datetime import datetime, timedelta
from pytuflow.helper import roundSeconds


class TestImportFV(unittest.TestCase):

    def test_tpc_frankenmodel(self):
        dir = os.path.dirname(__file__)
        tpc = os.path.join(dir, '2021', 'frankenmodel.tpc')
        res = tu.ResData()
        err, out = res.load(tpc)
        self.assertFalse(err)
        self.assertEqual(out, '')
        self.assertEqual(res.poNames(), ['ADCP1', 'ADCP2', 'ADCP3', 'NS1', 'NS2', 'NS3', 'NS4', 'NS5', 'NS6'])
        self.assertEqual(res.poResultTypes(),
                         ['Q', 'SALT_FLUX', 'TEMP_FLUX', 'SED_1_FLUX', 'SED_2_FLUX', 'TRACE_1_FLUX', 'TRACE_2_FLUX',
                          'SED_1_BEDLOAD_FLUX', 'SED_2_BEDLOAD_FLUX', 'H', 'Vx', 'Vy', 'temperature', 'salinity',
                          'sediment fraction 1 concentration', 'sediment fraction 2 concentration',
                          'tracer 1 concentration', 'tracer 2 concentration'])
        err, msg, (x,y) = res.getTimeSeriesData('NS3', 'SALT_FLUX')
        self.assertFalse(err)
        self.assertEqual(out, '')