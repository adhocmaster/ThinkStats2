import pandas as pd
import numpy as np
import thinkstat2


def readGZTable( dctPath = "2002FemResp.dct", dataPath = "2002FemResp.dat.gz" ):
	
	dct = thinkstat2.ReadStataData( dctPath )
	return dct.ReadFixedWidth( "2002FemResp.dat.gz", compression = "gzip" )
