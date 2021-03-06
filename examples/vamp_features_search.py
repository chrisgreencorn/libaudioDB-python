#!/usr/bin/env python

# This script loads some features from a CSV file as generated by Sonic Annotator and then searches an audioDB for those features.

from pyadb.utils import vamp

# add feature and power filenames here
(t, f, p) = vamp.features(featuresfile='.csv', powersfile='.csv', withtimes=True)

from pyadb import adb

# add audioDB database file here
db = adb.Pyadb(path = '.adb', mode = 'r')

# add some query parameters
db.configQuery['ntracks']   =  # int
db.configQuery['seqStart']  =  # int
db.configQuery['seqLength'] =  # int
db.configQuery['absThres']  =  # float
db.configQuery['relThres']  =  # float
db.configQuery['distance']  = 'eucNorm' # e.g.
db.configQuery['resFmt']    = 'list' # or 'dict'

res = db.query_data(featData=f, powerData=p, timesData=t)

from pprint import pprint

pprint(res)
