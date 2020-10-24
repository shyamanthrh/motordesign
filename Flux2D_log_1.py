#! Flux2D 18.1
executeBatchSpy('C:/Users/Shyamanth R H/Documents/Altair/Flux2DModel.py')

exportGeomToSTEP(fileName='Test',
                 entitiesType=Geometry(face=[Face[65]]),
                 tolerance=1.0E-6)

exportGeomToSTEP(fileName='test1',
                 entitiesType=Region(regionFace=RegionFace[ALL]),
                 tolerance=1.0E-6)

exportDXF(fileName='test')

closeProject()

exit()
