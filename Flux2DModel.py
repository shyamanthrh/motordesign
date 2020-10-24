#! Flux2D 18.1
newProject()
## FluxMotor version
ParameterGeom(name='FLUXMOTOR_VERSION : 2019.1.0', expression='0')
## Geometry
DomainType[1].lengthUnit=LengthUnit['MILLIMETER']
DomainType[1].angleUnit=AngleUnit['DEGREE']
CoordSys['XY1'].parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'], angleUnit=AngleUnit['DEGREE'])
## Periodicity
PeriodicityNumberZaxis(physicalType=PeriodicityCyclicType(), repetitionNumber='4', domainOriginAngle='0')
## Motor structural parameters
ParameterGeom(name='_OS_SN : Number of stator slots', expression='24')
ParameterGeom(name='_IM_PN : Number of rotor poles', expression='8')
ParameterGeom(name='_IM_ID : Rotor inner diameter', expression='20.0')
ParameterGeom(name='_IM_OD : Rotor outer diameter', expression='58.4')
ParameterGeom(name='_IM_SL : Rotor length', expression='20.0')
ParameterGeom(name='_OS_ID : Stator inner diameter', expression='60.0')
ParameterGeom(name='_OS_OD : Stator outer diameter', expression='110.0')
ParameterGeom(name='_OS_SL : Stator length', expression='20.0')
ParameterGeom(name='_L_EX : Additional lamination extension', expression='0.0')
ParameterGeom(name='_VS : Slot angular shift (Recommended value inferior to a slot pitch)', expression='0.0')
ParameterGeom(name='_L_EN : No. repetitions', expression='4')
ParameterGeom(name='_AG_L : Airgap length (thickness)', expression='0.7999999999999986')
ParameterGeom['_IM_OD'].expression='_OS_ID-2*_AG_L'
ParameterGeom['_IM_SL'].expression='_OS_SL'
## Motor geometry
## Inner magnet unit parameters
ParameterGeom(name='_IM_ul : ul', expression='1.0')
ParameterGeom(name='_IM_ua : ua', expression='1.0')
ParameterGeom(name='_IM_uv : uv', expression='1.0')
ParameterGeom(name='_IM_u1 : u1', expression='1.0')
## Inner magnet user parameters
ParameterGeom(name='_IM_TM : Magnet thickness', expression='5.0')
ParameterGeom(name='_IM_WM : Magnet width', expression='10.0')
ParameterGeom(name='_IM_H : Space between bar and outer rotor radius', expression='2.312063999999999')
ParameterGeom(name='_IM_R : Fillet radius', expression='1.1276532757047437')
## Inner magnet internal formulas
ParameterGeom(name='_IM_OR : Outer radius', expression='_IM_OD/2')
ParameterGeom(name='_IM_IR : Inner radius', expression='_IM_ID/2')
ParameterGeom(name='_IM_VE : Half angle of sector', expression='(180*_IM_uv)/_IM_PN')
ParameterGeom(name='_IM_X1 : x-coordinate of P1', expression='_IM_OR-_IM_H-_IM_TM')
ParameterGeom(name='_IM_Y1 : y-coordinate of P1', expression='0*_IM_ul')
ParameterGeom(name='_IM_X2 : x-coordinate of P2', expression='_IM_OR-_IM_H')
ParameterGeom(name='_IM_Y2 : y-coordinate of P2', expression='0*_IM_ul')
ParameterGeom(name='_IM_X3 : x-coordinate of P3', expression='_IM_X2')
ParameterGeom(name='_IM_Y3 : y-coordinate of P3', expression='_IM_WM/2')
ParameterGeom(name='_IM_R3 : Radius to compute P3', expression='Sqrt(_IM_X3**2+_IM_Y3**2)')
ParameterGeom(name='_IM_V3 : Angular coordinate of P3', expression='Atan2d(_IM_Y3,_IM_X3)')
ParameterGeom(name='_IM_X4 : x-coordinate of P4', expression='_IM_X1')
ParameterGeom(name='_IM_Y4 : y-coordinate of P4', expression='_IM_Y3')
ParameterGeom(name='_IM_V4 : Angular coordinate of P4', expression='Atan2d(_IM_Y4,_IM_X4)')
ParameterGeom(name='_IM_R4 : Radius to compute P4', expression='Sqrt(_IM_X4**2+_IM_Y4**2)')
ParameterGeom(name='_IM_Wa : Half tooth width', expression='_IM_R4*Sind(_IM_VE-_IM_V4)')
ParameterGeom(name='_IM_TX5 : x-coordinate (u) of P5', expression='Sqrt((_IM_R3-_IM_R)**2-(_IM_Wa+_IM_R)**2)')
ParameterGeom(name='_IM_V5 : Angle to compute P5', expression='_IM_VE-Atan2d(_IM_Wa,_IM_TX5)')
ParameterGeom(name='_IM_R5 : Radius to compute P5', expression='Sqrt(_IM_TX5**2+_IM_Wa**2)')
ParameterGeom(name='_IM_X5 : x-coordinate of P5', expression='_IM_R5*Cosd(_IM_V5)')
ParameterGeom(name='_IM_Y5 : y-coordinate of P5', expression='_IM_R5*Sind(_IM_V5)')
ParameterGeom(name='_IM_V6 : Angle to compute P6', expression='_IM_VE-Asind((_IM_Wa+_IM_R)/(_IM_R3-_IM_R))')
ParameterGeom(name='_IM_X6 : x-coordinate of P6', expression='_IM_R3*Cosd(_IM_V6)')
ParameterGeom(name='_IM_Y6 : y-coordinate of P6', expression='_IM_R3*Sind(_IM_V6)')
ParameterGeom(name='_IM_X5C6 : x-coordinate of P5C6', expression='(_IM_R3-_IM_R)*Cosd(_IM_V6)')
ParameterGeom(name='_IM_Y5C6 : y-coordinate of P5C6', expression='(_IM_R3-_IM_R)*Sind(_IM_V6)')
ParameterGeom(name='_IM_X7 : x-coordinate of P7', expression='_IM_R4*Cosd(_IM_VE)')
ParameterGeom(name='_IM_Y7 : y-coordinate of P7', expression='_IM_R4*Sind(_IM_VE)')
ParameterGeom(name='_IM_X8 : x-coordinate of P8', expression='_IM_R5*Cosd(_IM_VE)')
ParameterGeom(name='_IM_Y8 : y-coordinate of P8', expression='_IM_R5*Sind(_IM_VE)')
ParameterGeom(name='_IM_X9 : x-coordinate of P9', expression='_IM_OR*Cosd(_IM_V3)')
ParameterGeom(name='_IM_Y9 : y-coordinate of P9', expression='_IM_OR*Sind(_IM_V3)')
ParameterGeom(name='_IM_X10 : x-coordinate of P10', expression='_IM_X1+_IM_TM/2')
ParameterGeom(name='_IM_Y10 : y-coordinate of P10', expression='0*_IM_ul')
ParameterGeom(name='_IM_X11 : x-coordinate of P11', expression='_IM_X10')
ParameterGeom(name='_IM_Y11 : y-coordinate of P11', expression='_IM_Y3')
## Inner magnet geometry
CoordSysCartesian(name='_IM_CART : Inner magnet - Reference cartesian coordinate system', parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'], angleUnit=AngleUnit['DEGREE']), 
                  origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='_VS'),
                  visibility=Visibility['VISIBLE'])
CoordSysCylindrical(name='_IM_POLAR : Inner magnet - Reference polar coordinate system', parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'], angleUnit=AngleUnit['DEGREE']),
                    origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='_VS'),
                    visibility=Visibility['VISIBLE'])
CoordSysCartesian(name='_IM_sym_cart : Inner magnet - Symmetric cartesian coordinate system', parentCoordSys=Local(coordSys=CoordSys['_IM_CART']), 
                  origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='180.0/_IM_PN'),
                  visibility=Visibility['VISIBLE'])
CoordSysCylindrical(name='_IM_sym_polar : Inner magnet - Symmetric polar coordinate system', parentCoordSys=Local(coordSys=CoordSys['_IM_POLAR']),
                    origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='180.0/_IM_PN'),
                    visibility=Visibility['VISIBLE'])
CoordSysCartesian(name='_IM_CS1 : Inner magnet - Polarization coordinate system', parentCoordSys=Local(coordSys=CoordSys['_IM_sym_polar']), 
                  origin=['_IM_X10', '0*_IM_uv'], rotationAngles=RotationAngles(angleZ='(-90)*_IM_uv-0*_IM_uv'),
                  visibility=Visibility['VISIBLE'])
## Points
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X2**2+_IM_Y2**2)', 'Atan2d(_IM_Y2,_IM_X2)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X3**2+_IM_Y3**2)', 'Atan2d(_IM_Y3,_IM_X3)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X4**2+_IM_Y4**2)', 'Atan2d(_IM_Y4,_IM_X4)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X1**2+_IM_Y1**2)', 'Atan2d(_IM_Y1,_IM_X1)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X7**2+_IM_Y7**2)', 'Atan2d(_IM_Y7,_IM_X7)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X9**2+_IM_Y9**2)', 'Atan2d(_IM_Y9,_IM_X9)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['_IM_OR', '_IM_VE'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X5**2+_IM_Y5**2)', 'Atan2d(_IM_Y5,_IM_X5)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X8**2+_IM_Y8**2)', 'Atan2d(_IM_Y8,_IM_X8)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['Sqrt(_IM_X6**2+_IM_Y6**2)', 'Atan2d(_IM_Y6,_IM_X6)'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_sym_polar'],
                 uvw=['_IM_OR', '0*_IM_uv'], nature=Nature['STANDARD'])
## Lines
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[1], Point[2]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[2], Point[3]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[3], Point[4]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_sym_polar'], pivotCoord=['0*_IM_ul', '0*_IM_uv'],
                  defPoint=[Point[3], Point[5]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_sym_polar'], pivotCoord=['0*_IM_ul', '0*_IM_uv'],
                  defPoint=[Point[6], Point[7]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_sym_polar'], pivotCoord=['0*_IM_ul', '0*_IM_uv'],
                  defPoint=[Point[8], Point[9]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_sym_polar'], pivotCoord=['Sqrt(_IM_X5C6**2+_IM_Y5C6**2)', 'Atan2d(_IM_Y5C6,_IM_X5C6)'],
                  defPoint=[Point[10], Point[8]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_sym_polar'], pivotCoord=['0*_IM_ul', '0*_IM_uv'],
                  defPoint=[Point[2], Point[10]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[2], Point[6]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_sym_polar'], pivotCoord=['0*_IM_ul', '0*_IM_uv'],
                  defPoint=[Point[11], Point[6]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[3], Point[8]], nature=Nature['STANDARD'])
## Outer slot unit parameters
ParameterGeom(name='_OS_ul : ul', expression='1.0')
ParameterGeom(name='_OS_ua : ua', expression='1.0')
ParameterGeom(name='_OS_uv : uv', expression='1.0')
ParameterGeom(name='_OS_u1 : u1', expression='1.0')
## Outer slot user parameters
ParameterGeom(name='_OS_HS : Slot height', expression='14.850000000000005')
ParameterGeom(name='_OS_WS2 : Slot width', expression='5.8736786499023195')
ParameterGeom(name='_OS_H1 : Intermediary height of the slot', expression='1.4142857142857146')
ParameterGeom(name='_OS_WS1 : Intermediary width of the slot', expression='3.5242071899413916')
ParameterGeom(name='_OS_HO : Height of slot opening', expression='1.4142857142857146')
ParameterGeom(name='_OS_WO : Width of slot opening', expression='0.8390969499860457')
## Outer slot internal formulas
ParameterGeom(name='_OS_OR : Outer radius', expression='_OS_OD/2')
ParameterGeom(name='_OS_IR : Inner radius', expression='_OS_ID/2')
ParameterGeom(name='_OS_VE : Half angle of sector', expression='(180*_OS_uv)/_OS_SN')
ParameterGeom(name='_OS_X1 : x-coordinate of P1', expression='_OS_IR*Cosd(Asind(_OS_WO/2/_OS_IR))')
ParameterGeom(name='_OS_Y1 : y-coordinate of P1', expression='_OS_WO/2')
ParameterGeom(name='_OS_X2 : x-coordinate of P2', expression='_OS_X1+_OS_HO')
ParameterGeom(name='_OS_Y2 : y-coordinate of P2', expression='_OS_WO/2')
ParameterGeom(name='_OS_X3 : x-coordinate of P3', expression='_OS_X2+_OS_H1')
ParameterGeom(name='_OS_Y3 : y-coordinate of P3', expression='_OS_WS1/2')
ParameterGeom(name='_OS_X5 : x-coordinate of P5', expression='_OS_X1+_OS_HS')
ParameterGeom(name='_OS_Y5 : y-coordinate of P5', expression='0*_OS_ul')
ParameterGeom(name='_OS_X4C5 : x-coordinate of PT4C5', expression='_OS_X5-_OS_WS2/2')
ParameterGeom(name='_OS_Y4C5 : y-coordinate of PT4C5', expression='0*_OS_ul')
ParameterGeom(name='_OS_V1a : Angle V1 (intermediary parameter a)', expression='_OS_X5-_OS_WS2/2-_OS_X3')
ParameterGeom(name='_OS_V1b : Angle V1 (intermediary parameter b)', expression='Sqrt(_OS_V1a**2-((_OS_WS2/2)**2-_OS_Y3**2))')
ParameterGeom(name='_OS_V1 : Angle between PT4-PT3 versus x axis', expression='2*Atan2d(_OS_V1a-_OS_V1b,_OS_WS2/2+_OS_Y3)')
ParameterGeom(name='_OS_X4 : x-coordinate of PT4', expression='_OS_X4C5-_OS_WS2/2*Sind(_OS_V1)')
ParameterGeom(name='_OS_Y4 : y-coordinate of PT4', expression='_OS_WS2/2*Cosd(_OS_V1)')
ParameterGeom(name='_OS_X6 : x-coordinate of P6', expression='Sqrt(_OS_X4**2+_OS_Y4**2)*Cosd(_OS_VE)')
ParameterGeom(name='_OS_Y6 : y-coordinate of P6', expression='Sqrt(_OS_X4**2+_OS_Y4**2)*Sind(_OS_VE)')
ParameterGeom(name='_OS_X7 : x-coordinate of P7', expression='Sqrt(_OS_X3**2+_OS_Y3**2)*Cosd(_OS_VE)')
ParameterGeom(name='_OS_Y7 : y-coordinate of P7', expression='Sqrt(_OS_X3**2+_OS_Y3**2)*Sind(_OS_VE)')
ParameterGeom(name='_OS_X8 : x-coordinate of P8', expression='_OS_X3')
ParameterGeom(name='_OS_Y8 : y-coordinate of P8', expression='0*_OS_ul')
ParameterGeom(name='_OS_ASa : Slot area (trapezoidal upper)', expression='(_OS_Y2+_OS_Y3)*(_OS_X3-_OS_X2)')
ParameterGeom(name='_OS_ASb : Slot area (trapezoidal middle)', expression='(_OS_Y4+_OS_Y3)*(_OS_X4-_OS_X3)')
ParameterGeom(name='_OS_ASc : Slot area (triangular under bottom)', expression='_OS_Y4*(_OS_X4C5-_OS_X4)')
ParameterGeom(name='_OS_ASd : Slot area (round bottom)', expression='((_OS_WS2/2)**2*(90+_OS_V1/_OS_uv)*Pi())/180')
ParameterGeom(name='_OS_AS : Slot area', expression='_OS_ASb+_OS_ASc+_OS_ASd')
ParameterGeom(name='_OS_K : Coefficient for computing WC & HTC', expression='_OS_Y3**2+(Tand(_OS_V1)*_OS_AS)/2')
ParameterGeom(name='_OS_HTC : Height of the upper layer', expression='(-_OS_Y3+Sqrt(_OS_K))/Tand(_OS_V1)')
ParameterGeom(name='_OS_WC : Width of one layer (Mean value)', expression='2*(_OS_Y3+_OS_HTC*Tand(_OS_V1))')
ParameterGeom(name='_OS_XI1 : x-coordinate of Pi1', expression='_OS_X2')
ParameterGeom(name='_OS_YI1 : y-coordinate of Pi1', expression='0*_OS_ul')
ParameterGeom(name='_OS_XI2 : x-coordinate of Pi2', expression='_OS_X3+_OS_HTC')
ParameterGeom(name='_OS_YI2 : y-coordinate of Pi2', expression='_OS_WC/2')
ParameterGeom(name='_OS_XI3 : x-coordinate of Pi3', expression='_OS_XI2')
ParameterGeom(name='_OS_YI3 : y-coordinate of Pi3', expression='0*_OS_ul')
ParameterGeom(name='_OS_YI4 : y-coordinate of Pi4', expression='_OS_WS2/2')
## Outer slot geometry
CoordSysCartesian(name='_OS_CART : Outer slot - Reference cartesian coordinate system', parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'], angleUnit=AngleUnit['DEGREE']), 
                  origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='_VS'),
                  visibility=Visibility['VISIBLE'])
CoordSysCylindrical(name='_OS_POLAR : Outer slot - Reference polar coordinate system', parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'], angleUnit=AngleUnit['DEGREE']),
                    origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='_VS'),
                    visibility=Visibility['VISIBLE'])
CoordSysCartesian(name='_OS_sym_cart : Outer slot - Symmetric cartesian coordinate system', parentCoordSys=Local(coordSys=CoordSys['_OS_CART']), 
                  origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='180.0/_OS_SN'),
                  visibility=Visibility['VISIBLE'])
CoordSysCylindrical(name='_OS_sym_polar : Outer slot - Symmetric polar coordinate system', parentCoordSys=Local(coordSys=CoordSys['_OS_POLAR']),
                    origin=['0.0', '0.0'], rotationAngles=RotationAngles(angleZ='180.0/_OS_SN'),
                    visibility=Visibility['VISIBLE'])
## Points
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X4', '_OS_Y4'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X6', '_OS_Y6'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X5', '_OS_Y5'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X3', '_OS_Y3'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X7', '_OS_Y7'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_XI2', '_OS_YI2'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X1', '_OS_Y1'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X2', '_OS_Y2'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_polar'],
                 uvw=['_OS_IR', '_OS_VE'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_XI3', '_OS_YI3'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_X8', '_OS_Y8'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_sym_cart'],
                 uvw=['_OS_XI1', '_OS_YI1'], nature=Nature['STANDARD'])
## Lines
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_OS_sym_polar'], pivotCoord=['0*_OS_ul', '0*_OS_uv'],
                  defPoint=[Point[12], Point[13]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_OS_sym_cart'], pivotCoord=['_OS_X4C5', '_OS_Y4C5'],
                  defPoint=[Point[14], Point[12]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_OS_sym_polar'], pivotCoord=['0*_OS_ul', '0*_OS_uv'],
                  defPoint=[Point[15], Point[16]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[15], Point[17]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[17], Point[12]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[18], Point[19]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_OS_sym_polar'], pivotCoord=['0*_OS_ul', '0*_OS_uv'],
                  defPoint=[Point[18], Point[20]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[19], Point[15]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[17], Point[21]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[21], Point[22]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[22], Point[15]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[14], Point[21]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[23], Point[19]], nature=Nature['STANDARD'])
## Shaft unit parameters
ParameterGeom(name='_S_ul : ul', expression='1.0')
ParameterGeom(name='_S_ua : ua', expression='1.0')
ParameterGeom(name='_S_uv : uv', expression='1.0')
ParameterGeom(name='_S_u1 : u1', expression='1.0')
## Shaft user parameters
ParameterGeom(name='_S_D1 : Connection Side end-shaft diameter D1', expression='12.0')
ParameterGeom(name='_S_L1 : Connection Side end-shaft extension L1', expression='25.0')
ParameterGeom(name='_S_D2 : Opposite Connection Side end-shaft diameter D2', expression='12.0')
ParameterGeom(name='_S_L2 : Opposite Connection Side end-shaft extension L2', expression='25.0')
## Shaft internal formulas
ParameterGeom(name='_S_V : V', expression='(_S_uv*360)/_IM_PN')
ParameterGeom(name='_S_X1 : X1', expression='0')
ParameterGeom(name='_S_Y1 : Y1', expression='0')
ParameterGeom(name='_S_X2 : X2', expression='_IM_ID/2')
ParameterGeom(name='_S_X3 : X3', expression='_S_X2*Cosd(_S_V)')
ParameterGeom(name='_S_Y3 : Y3', expression='_S_X2*Sind(_S_V)')
## Shaft geometry
## Points
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_CART'],
                 uvw=['_S_X2', '_S_Y1'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_IM_CART'],
                 uvw=['_S_X3', '_S_Y3'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['XY1'],
                 uvw=['0.0', '0.0'], nature=Nature['STANDARD'])
## Lines
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_IM_CART'], pivotCoord=['_S_X1', '_S_Y1'],
                  defPoint=[Point[24], Point[25]], nature=Nature['STANDARD'])
## Lamination unit parameters
ParameterGeom(name='_L_ul : ul', expression='1.0')
ParameterGeom(name='_L_ua : ua', expression='1.0')
ParameterGeom(name='_L_uv : uv', expression='1.0')
ParameterGeom(name='_L_u1 : u1', expression='1.0')
## Lamination user parameters
ParameterGeom(name='_L_R : Lamination fillet radius', expression='10.0')
## Lamination internal formulas
ParameterGeom(name='_L_V : V', expression='(_L_uv*360)/_L_EN')
ParameterGeom(name='_L_X0 : X0', expression='0')
ParameterGeom(name='_L_Y0 : Y0', expression='0')
ParameterGeom(name='_L_X1 : X1', expression='Tand(_VS)*(_OS_OD/2+_L_EX)*(-1)')
ParameterGeom(name='_L_Y1 : Y1', expression='_OS_OD/2+_L_EX')
ParameterGeom(name='_L_X2 : X2', expression='_OS_OD/2+_L_EX-_L_R')
ParameterGeom(name='_L_Y2 : Y2', expression='_OS_OD/2+_L_EX')
ParameterGeom(name='_L_X3 : X3', expression='_OS_OD/2+_L_EX')
ParameterGeom(name='_L_Y3 : Y3', expression='_OS_OD/2+_L_EX-_L_R')
ParameterGeom(name='_L_X4 : X4', expression='_OS_OD/2+_L_EX')
ParameterGeom(name='_L_Y4 : Y4', expression='Tand(_VS)*(_OS_OD/2+_L_EX)')
ParameterGeom(name='_L_X5 : X5', expression='Cosd(_VS)*_OS_OD/2')
ParameterGeom(name='_L_Y5 : Y5', expression='Sind(_VS)*_OS_OD/2')
ParameterGeom(name='_L_X6 : X6', expression='Sind(_VS)*_OS_OD/2*(-1)')
ParameterGeom(name='_L_Y6 : Y6', expression='Cosd(_VS)*_OS_OD/2')
## Lamination geometry
## Points
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['XY1'],
                 uvw=['_L_X1', '_L_Y1'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['XY1'],
                 uvw=['_L_X2', '_L_Y2'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['XY1'],
                 uvw=['_L_X3', '_L_Y3'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['XY1'],
                 uvw=['_L_X4', '_L_Y4'], nature=Nature['STANDARD'])
## Lines
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[27], Point[28]], nature=Nature['STANDARD'])
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['XY1'], pivotCoord=['_L_X2', '_L_Y3'],
                  defPoint=[Point[29], Point[28]], nature=Nature['STANDARD'])
LineSegment(color=Color['White'], visibility=Visibility['VISIBLE'],
            defPoint=[Point[29], Point[30]], nature=Nature['STANDARD'])
## Airgap unit parameters
ParameterGeom(name='_AG_ul : ul', expression='1.0')
ParameterGeom(name='_AG_ua : ua', expression='1.0')
ParameterGeom(name='_AG_uv : uv', expression='1.0')
ParameterGeom(name='_AG_u1 : u1', expression='1.0')
## Airgap user parameters
## Airgap internal formulas
ParameterGeom(name='_AG_V : V', expression='(_AG_uv*360)/_IM_PN')
ParameterGeom(name='_AG_X0 : X0', expression='0')
ParameterGeom(name='_AG_Y0 : Y0', expression='0')
ParameterGeom(name='_AG_X1 : X1', expression='_IM_OD/2')
ParameterGeom(name='_AG_Y1 : Y1', expression='0')
ParameterGeom(name='_AG_X2 : X2', expression='_IM_OD/2*Cosd(_AG_V)')
ParameterGeom(name='_AG_Y2 : Y2', expression='_IM_OD/2*Sind(_AG_V)')
ParameterGeom(name='_AG_X4 : X4', expression='_OS_ID/2*Cosd(_AG_V)')
ParameterGeom(name='_AG_Y4 : Y4', expression='_OS_ID/2*Sind(_AG_V)')
ParameterGeom(name='_AG_X3 : X3', expression='_OS_ID/2')
ParameterGeom(name='_AG_Y3 : Y3', expression='0')
ParameterGeom(name='_AG_X5 : X5', expression='(_IM_OD+_OS_ID)/4')
ParameterGeom(name='_AG_Y5 : Y5', expression='0')
ParameterGeom(name='_AG_X6 : X6', expression='(_IM_OD+_OS_ID)/4*Cosd(_AG_V)')
ParameterGeom(name='_AG_Y6 : Y6', expression='(_IM_OD+_OS_ID)/4*Sind(_AG_V)')
## Airgap geometry
## Points
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_CART'],
                 uvw=['_AG_X5', '_AG_Y5'], nature=Nature['STANDARD'])
PointCoordinates(color=Color['White'], visibility=Visibility['VISIBLE'], coordSys=CoordSys['_OS_CART'],
                 uvw=['_AG_X6', '_AG_Y6'], nature=Nature['STANDARD'])
## Lines
LineArcPivotCoord(color=Color['White'], visibility=Visibility['VISIBLE'],
                  coordSys=CoordSys['_OS_CART'], pivotCoord=['_AG_X0', '_AG_Y0'],
                  defPoint=[Point[31], Point[32]], nature=Nature['STANDARD'])
## Inner magnet transformations
TransfSymmetryLine2PT(name='_IM_magnetSym : Inner magnet - Symetry', coordSys=CoordSys['_IM_sym_polar'],
                      firstPoint=['0.0', '0.0' , '0'], secondPoint=['100.0', '0.0' , '0'])
sym=Line[1,2,3,4,5,6,7,8,9,10,11].propagate(transformation=Transf['_IM_magnetSym'], repetitionNumber=1)
symLines=sym.get('lines')
lines=symLines.union(Line[1,2,3,4,5,6,7,8,9,10,11])
TransfRotation3AnglesPivotCoord(name='_IM_magnetRot : Inner magnet - Propagation', coordSys=CoordSys['_IM_POLAR'],
                                pivotCoord=['0.0', '0.0' , '0'], rotationAngles=RotationAngles(angleZ='45.0'))
lines.propagate(transformation=Transf['_IM_magnetRot'], repetitionNumber=1)
## Outer slot transformations
TransfSymmetryLine2PT(name='_OS_Slot_sym : Outer slot - Symmetry', coordSys=CoordSys['_OS_sym_polar'],
                      firstPoint=['0.0', '0.0' , '0'], secondPoint=['100.0', '0.0' , '0'])
sym=Line[12,13,14,15,16,17,18,19,20,21,22,23,24].propagate(transformation=Transf['_OS_Slot_sym'], repetitionNumber=1)
symLines=sym.get('lines')
lines=symLines.union(Line[12,13,14,15,16,17,18,19,20,21,22,23,24])
TransfRotation3AnglesPivotCoord(name='_OS_slotRot : Outer slot - Propagation', coordSys=CoordSys['_OS_POLAR'],
                                pivotCoord=['0.0', '0.0' , '0'], rotationAngles=RotationAngles(angleZ='14.999999999999998'))
lines.propagate(transformation=Transf['_OS_slotRot'], repetitionNumber=5)
## Shaft transformations
TransfRotation3AnglesPivotCoord(name='_S_shaftRot : Shaft - Propagation', coordSys=CoordSys['_IM_POLAR'],
                                pivotCoord=['0.0', '0.0' , '0'], rotationAngles=RotationAngles(angleZ='45.0'))
Line[25].propagate(transformation=Transf['_S_shaftRot'], repetitionNumber=1)
## Lamination transformations
## Airgap transformations
TransfRotation3AnglesPivotCoord(name='_AG_airgapRot : Airgap - Propagation', coordSys=CoordSys['_OS_POLAR'],
                                pivotCoord=['0.0', '0.0' , '0'], rotationAngles=RotationAngles(angleZ='45.0'))
Line[29].propagate(transformation=Transf['_AG_airgapRot'], repetitionNumber=1)
## Infinite box
InfiniteBoxDisc(DISCOID=['(_OS_OD+2*_L_EX)*0.75*Sqrt(2)', '(_OS_OD+2*_L_EX)*1.05*Sqrt(2)'])
InfiniteBoxDisc['InfiniteBoxDisc'].complete2D(buildingOption='FACES', coordSys=CoordSys['XY1'], linkMesh='LinkMesh')
## Application
ApplicationMagneticDC2D(domain2D=Domain2DPlane(lengthUnit=LengthUnit['MILLIMETER'], depth='_OS_SL'),
                        coilCoefficient=CoilCoefficientAutomatic())
## Physic
## Mechanical sets
MechanicalSetFixed(name='STATOR : Stator Mechanical Set')
MechanicalSetRotation1Axis(name='ROTOR : Rotor Mechanical Set', kinematics=RotatingMultiStatic(),
                           rotationAxis=RotationZAxis(coordSys=CoordSys['XY1'],
                           pivot=['0', '0']))
## Circuit
CurrentStrandedCoil(name='PHASE_1 : Phase 1 - Coil conductor', rmsModulus='0')
CurrentStrandedCoil(name='PHASE_2 : Phase 2 - Coil conductor', rmsModulus='0')
CurrentStrandedCoil(name='PHASE_3 : Phase 3 - Coil conductor', rmsModulus='0')
SensorPredefinedMagneticFlux(name='MAG_FLUX_PH1 : Magnetic flux linkage - Phase 1', support=ComputationSupportCoilConductorMagneticFlux(coilConductor=[CoilConductor['PHASE_1']]))
SensorPredefinedMagneticFlux(name='MAG_FLUX_PH2 : Magnetic flux linkage - Phase 2', support=ComputationSupportCoilConductorMagneticFlux(coilConductor=[CoilConductor['PHASE_2']]))
SensorPredefinedMagneticFlux(name='MAG_FLUX_PH3 : Magnetic flux linkage - Phase 3', support=ComputationSupportCoilConductorMagneticFlux(coilConductor=[CoilConductor['PHASE_3']]))
VariationParameterPilot(name='TURNS : Number of turns per coil', referenceValue=200.0)
## Colors
Color(name='FLUID', code=[190, 240, 255])
Color(name='SHAFT', code=[168, 168, 168])
Color(name='SHAFT_RING', code=[70, 70, 70])
Color(name='YOKE', code=[100, 100, 100])
Color(name='NORTH_MAGNET', code=[255, 100, 1])
Color(name='SOUTH_MAGNET', code=[255, 200, 69])
Color(name='BAR', code=[255, 200, 69])
Color(name='INSULATOR', code=[255, 255, 190])
Color(name='PHASE_1_POS', code=[255, 0, 0])
Color(name='PHASE_1_NEG', code=[140, 0, 0])
Color(name='PHASE_2_POS', code=[0, 255, 0])
Color(name='PHASE_2_NEG', code=[0, 140, 0])
Color(name='PHASE_3_POS', code=[0, 0, 255])
Color(name='PHASE_3_NEG', code=[0, 0, 140])
Color(name='QUOTE', code=[16, 16, 16])
Color(name='MECHANICAL_DEVICE', code=[44, 44, 44])
Color(name='FERROMAGNETIC_WEDGE', code=[70, 70, 70])
Color(name='HUB', code=[44, 44, 44])
## Materials
Material(name='_B_NdFeB_1320_1400',
         propertyBH=PropertyBhMagnetOneDirection(br='1.32', mur='1.1'),
         propertyJE=PropertyJeTLinearFunction(slope='0.0', rhoConstant='1.6E-6', 
                          referenceTemperature=Temperature(temperature='20.0', unit=Unit['CELSIUS_DEGREE']),
                          temperature=Temperature(temperature='20.0', unit=Unit['CELSIUS_DEGREE'])))
Material(name='_B_M400_65A',
         propertyBH=PropertyBhNonlinearJmuknee(initialMur='10000.0', js='1.9', knee='1.3'),
         propertyJE=None,
         propertyLosses=PropertyLossesModifiedBertotti(k1Coefficient=181.0,
                               k2Coefficient=1.44,
                               k3Coefficient=1.05E-8,
                               a1Exponent=2.0,
                               a2Exponent=2.0,
                               a3Exponent=0.0))
# Fluid _B_Air is set to air.
Material(name='_B_M330_35A',
         propertyBH=PropertyBhNonlinearJmuknee(initialMur='10000.0', js='1.85', knee='1.4'),
         propertyJE=None,
         propertyLosses=PropertyLossesModifiedBertotti(k1Coefficient=179.0,
                               k2Coefficient=0.5495,
                               k3Coefficient=1.0E-8,
                               a1Exponent=1.6,
                               a2Exponent=2.0,
                               a3Exponent=0.0))
Material(name='_B_Copper',
         propertyBH=PropertyBhLinear(mur='1.0'),
         propertyJE=PropertyJeTLinearFunction(slope='0.00393', rhoConstant='1.724E-8', 
                          referenceTemperature=Temperature(temperature='20.0', unit=Unit['CELSIUS_DEGREE']),
                          temperature=Temperature(temperature='20.0', unit=Unit['CELSIUS_DEGREE'])))
Material(name='_B_Nomex_130',
         propertyBH=PropertyBhLinear(mur='1.0'),
         propertyJE=None)
Material(name='_B_EN_1_1151',
         propertyBH=PropertyBhNonlinearJmuknee(initialMur='1800.0', js='1.98', knee='0.71'),
         propertyJE=PropertyJeTLinearFunction(slope='0.0038', rhoConstant='1.68E-7', 
                          referenceTemperature=Temperature(temperature='20.0', unit=Unit['CELSIUS_DEGREE']),
                          temperature=Temperature(temperature='20.0', unit=Unit['CELSIUS_DEGREE'])),
         propertyLosses=PropertyLossesModifiedBertotti(k1Coefficient=0.0,
                               k2Coefficient=0.0,
                               k3Coefficient=0.0,
                               a1Exponent=0.0,
                               a2Exponent=0.0,
                               a3Exponent=0.0))
## Regions
airFaces=Face[ALL]
## Shaft regions
SHAFT_Faces=Line[ALL].complement(Line[ALL])
## Shaft regions
RegionFace(name='_S_Shaft : Shaft', 
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['_B_EN_1_1151']), 
           color=Color['SHAFT'], visibility=Visibility['VISIBLE'])
RegionFace['_S_Shaft'].mechanicalSet=MechanicalSet['ROTOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[4.619397662556434,1.913417161825449], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
regionFaces.assignRegion(region=RegionFace['_S_Shaft'])
SHAFT_Faces=SHAFT_Faces.union(regionFaces)
airFaces=airFaces.complement(SHAFT_Faces)
## Magnet regions
magnetFaces=Line[ALL].complement(Line[ALL])
## _IM_MAGNET_1 regions
RegionFace(name='_IM_MAGNET_1 : _IM_MAGNET_1', 
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['_B_NdFeB_1320_1400']), 
           color=Color['NORTH_MAGNET'], visibility=Visibility['VISIBLE'])
orientRegSurfMaterial(region=RegionFace['_IM_MAGNET_1'], 
                      coordSys=CoordSys['_IM_CS1'], orientation='Direction', angle='90.0')
RegionFace['_IM_MAGNET_1'].mechanicalSet=MechanicalSet['ROTOR']
magnetRegionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[21.574806329682453,11.642557888058354], coordSys=CoordSys['XY1'])
magnetRegionFaces=magnetRegionFaces.union(face)
magnetRegionFaces.assignRegion(region=RegionFace['_IM_MAGNET_1'])
magnetFaces=magnetFaces.union(magnetRegionFaces)
CoordSysPropagated(name='_IM_CS1_1 : Inner magnet - Polarization coordinate system',
                  visibility=Visibility['VISIBLE'],
                  transf=Transf['_IM_magnetRot'],
                  coordSys=CoordSys['_IM_CS1'])
## _IM_MAGNET_2 regions
RegionFace(name='_IM_MAGNET_2 : _IM_MAGNET_2', 
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['_B_NdFeB_1320_1400']), 
           color=Color['SOUTH_MAGNET'], visibility=Visibility['VISIBLE'])
orientRegSurfMaterial(region=RegionFace['_IM_MAGNET_2'], 
                      coordSys=CoordSys['_IM_CS1_1'], orientation='Direction', angle='270.0')
RegionFace['_IM_MAGNET_2'].mechanicalSet=MechanicalSet['ROTOR']
propFaces=Line[ALL].complement(Line[ALL])
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[7.023160225501922,23.488223491507902], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
propFaces.assignRegion(region=RegionFace['_IM_MAGNET_2'])
magnetFaces=magnetFaces.union(propFaces)
airFaces=airFaces.complement(magnetFaces)
## Inner magnet regions
INNER_MAGNET_Faces=Line[ALL].complement(Line[ALL])
## Yoke regions
RegionFace(name='_IM_YOKE : Yoke', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M400_65A'],
                                              sheetIronThickness='6.500000000000001E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_IM_YOKE'].mechanicalSet=MechanicalSet['ROTOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[13.25692489152419,8.857994017017077], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[3.11051385133485,15.63760912562013], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[15.63760912562013,3.1105138513348503], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[8.857994017017077,13.25692489152419], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_IM_YOKE'])
INNER_MAGNET_Faces=INNER_MAGNET_Faces.union(regionFaces)
## Bridge regions
RegionFace(name='_IM_BRIDGE : Bridge', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M400_65A'],
                                              sheetIronThickness='6.500000000000001E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_IM_BRIDGE'].mechanicalSet=MechanicalSet['ROTOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[21.968050216513213,17.800243179750886], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[2.9470846183716546,28.120429936714544], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[28.120429936714537,2.947084618371656], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[17.800243179750883,21.968050216513213], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_IM_BRIDGE'])
INNER_MAGNET_Faces=INNER_MAGNET_Faces.union(regionFaces)
## Pole shoe regions
RegionFace(name='_IM_POLE_SHOE : Pole shoe', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M400_65A'],
                                              sheetIronThickness='6.500000000000001E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_IM_POLE_SHOE'].mechanicalSet=MechanicalSet['ROTOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[25.018595465418144,13.172462507491625], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[8.3764809453873,27.005156073333062], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[27.005156073333062,8.3764809453873], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[13.172462507491627,25.018595465418144], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_IM_POLE_SHOE'])
INNER_MAGNET_Faces=INNER_MAGNET_Faces.union(regionFaces)
## Interpole regions
RegionFace(name='_IM_INTER_POLE : Interpole', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M400_65A'],
                                              sheetIronThickness='6.500000000000001E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_IM_INTER_POLE'].mechanicalSet=MechanicalSet['ROTOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[18.337726846123694,15.857596890839167], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[1.7537167096055803,24.17974529927575], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[24.179745299275755,1.7537167096055806], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[15.857596890839169,18.337726846123697], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_IM_INTER_POLE'])
INNER_MAGNET_Faces=INNER_MAGNET_Faces.union(regionFaces)
## Edge regions
RegionFace(name='_IM_EDGE : Edge', 
           magneticDC2D=MagneticDC2DFaceVacuum(), 
           color=Color['FLUID'], visibility=Visibility['VISIBLE'])
RegionFace['_IM_EDGE'].mechanicalSet=MechanicalSet['ROTOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[21.73776885170857,15.479015014064505], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[4.4256072803754485,26.31624024544223], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[26.31624024544223,4.425607280375451], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[15.479015014064501,21.73776885170857], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_IM_EDGE'])
INNER_MAGNET_Faces=INNER_MAGNET_Faces.union(regionFaces)
airFaces=airFaces.complement(INNER_MAGNET_Faces)
## Outer slot regions
OUTER_SLOT_Faces=Line[ALL].complement(Line[ALL])
## Yoke regions
RegionFace(name='_OS_YOKE : Yoke', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M330_35A'],
                                              sheetIronThickness='3.5E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_OS_YOKE'].mechanicalSet=MechanicalSet['STATOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[48.9642663976968,9.73959814617411], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[44.77505598695828,22.080614060264033], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[37.53449950498714,32.916872616087], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[27.736028910444375,41.50990070082764], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[16.047393781609802,47.27409765116124], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[3.265155286130634,49.81664297070841], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[49.81664297070841,3.2651552861306237], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[47.27409765116125,16.047393781609795], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[41.50990070082766,27.73602891044437], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[32.91687261608701,37.53449950498714], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[22.080614060264043,44.77505598695828], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[9.739598146174119,48.964266397696804], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_OS_YOKE'])
OUTER_SLOT_Faces=OUTER_SLOT_Faces.union(regionFaces)
## Tooth regions
RegionFace(name='_OS_TOOTH : Tooth', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M330_35A'],
                                              sheetIronThickness='3.5E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_OS_TOOTH'].mechanicalSet=MechanicalSet['STATOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[36.28811324537569,8.41131229604812], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[32.874617954488535,17.516758598475953], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[27.22077177787786,25.428466750229934], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[19.711874989057115,31.60726691548394], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[10.859646495145762,35.63208407392598], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[1.2673510390045948,37.22863358753307], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[37.22863358753307,1.2673510390045912], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[35.63208407392598,10.859646495145759], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[31.607266915483947,19.71187498905711], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[25.42846675022994,27.22077177787786], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[17.51675859847596,32.874617954488535], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[8.411312296048127,36.2881132453757], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_OS_TOOTH'])
OUTER_SLOT_Faces=OUTER_SLOT_Faces.union(regionFaces)
## Tooth foot regions
RegionFace(name='_OS_TOOTH_FOOT : Tooth foot', 
           magneticDC2D=MagneticDC2DFaceLaminatedNonConducting(sheetIronMaterial=Material['_B_M330_35A'],
                                              sheetIronThickness='3.5E-4',
                                              stackingFactor='0.95'), 
           color=Color['YOKE'], visibility=Visibility['VISIBLE'])
RegionFace['_OS_TOOTH_FOOT'].mechanicalSet=MechanicalSet['STATOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[30.65088018303969,6.956038594232402], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[27.80612150063433,14.65204886735869], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[23.066421589749197,21.3495462238301], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[16.754783166586662,26.592107286940802], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[9.301333959209593,30.022460183981597], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[1.214014213693531,31.406832033945356], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[31.406832033945353,1.2140142136935275], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[30.022460183981597,9.30133395920959], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[26.592107286940806,16.75478316658666], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[21.349546223830103,23.066421589749194], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[14.652048867358697,27.80612150063433], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[6.956038594232409,30.650880183039693], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_OS_TOOTH_FOOT'])
OUTER_SLOT_Faces=OUTER_SLOT_Faces.union(regionFaces)
## Insulating wedge regions
RegionFace(name='_OS_INSULATING_WEDGE : Insulating wedge', 
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['_B_Nomex_130']), 
           color=Color['INSULATOR'], visibility=Visibility['VISIBLE'])
RegionFace['_OS_INSULATING_WEDGE'].mechanicalSet=MechanicalSet['STATOR']
regionFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[31.78821593738299,4.599025711284157], coordSys=CoordSys['XY1'])
regionFaces=regionFaces.union(face)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[29.51474330257549,12.669713404723016], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[25.229889687116955,19.87698106732137], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[19.225660783845484,25.729665318446106], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[11.91123487006162,29.828915398401108], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
propFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[3.785077984129382,31.8953741885685], coordSys=CoordSys['XY1'])
propFaces=propFaces.union(face)
regionFaces=regionFaces.union(propFaces)
symFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[31.895374188568503,3.7850779841293787], coordSys=CoordSys['XY1'])
symFaces=symFaces.union(face)
regionFaces=regionFaces.union(symFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[29.828915398401115,11.91123487006162], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[25.729665318446113,19.225660783845488], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[19.876981067321374,25.22988968711696], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[12.669713404723018,29.514743302575493], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
symPropFaces=Line[ALL].complement(Line[ALL])
face=Face.selectByCoordinates(coordinates=[4.599025711284157,31.788215937382994], coordSys=CoordSys['XY1'])
symPropFaces=symPropFaces.union(face)
regionFaces=regionFaces.union(symPropFaces)
regionFaces.assignRegion(region=RegionFace['_OS_INSULATING_WEDGE'])
OUTER_SLOT_Faces=OUTER_SLOT_Faces.union(regionFaces)
airFaces=airFaces.complement(OUTER_SLOT_Faces)
## Airgap Region
airgapFaces=Line[ALL].complement(Line[ALL])
## Inner regions
RegionFace(name='_AG_INNER : Inner', 
           magneticDC2D=MagneticDC2DFaceVacuum(), 
           color=Color['FLUID'], visibility=Visibility['VISIBLE'])
RegionFace['_AG_INNER'].mechanicalSet=MechanicalSet['ROTOR']
## Outer regions
RegionFace(name='_AG_OUTER : Outer', 
           magneticDC2D=MagneticDC2DFaceVacuum(), 
           color=Color['FLUID'], visibility=Visibility['VISIBLE'])
RegionFace['_AG_OUTER'].mechanicalSet=MechanicalSet['STATOR']
airgapPointSet=Point.selectByCoordinates(coordinates=[29.6,0.0], coordSys=CoordSys['XY1'])
airgapFaceSet=Face.selectByRelation(formule='Face.edge Line.extrema',entities=airgapPointSet)
Fmin=None
Fmax=None
srmin=1e16
srmax=0
for f in airgapFaceSet:
    tP = Point.selectByRelation(formule='inv.Line.extrema inv.Face.edge',entities=f)
    for p in tP:
        coo = p.globalCoordinates
        sr = coo[0]**2+coo[1]**2+coo[2]**2
        if sr > srmax:
            srmax=sr
            Fmax=f
        if sr < srmin:
            srmin=sr
            Fmin=f
airgapFaceSet = [Fmin, Fmax]
face=airgapFaceSet[0]
face.assignRegion(region=RegionFace['_AG_INNER'])
airFaces=airFaces.complement(face)
face=airgapFaceSet[1]
face.assignRegion(region=RegionFace['_AG_OUTER'])
airFaces=airFaces.complement(face)
## Winding regions
windingFaces=Line[ALL].complement(Line[ALL])
faces=Line[ALL].complement(Line[ALL])
faces=Face.selectByCoordinates(coordinates=[43.006861226891786,4.193630045516825], coordSys=CoordSys['XY1'])
face=Face.selectByCoordinates(coordinates=[42.62682929057864,7.080259188734253], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[35.858499133670115,3.745871560501997], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[35.60615330554196,5.662628422335454], coordSys=CoordSys['XY1'])
faces=faces.union(face)
RegionFace(name='PHASE_1_GO : Winding phase 1 - Positive direction', 
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='1*TURNS', seriesParallel=ParallelSolidConductorNumber(number=4),
                        electricComponent=CoilConductor['PHASE_1']),
                              material=Material['_B_Copper']), 
           color=Color['PHASE_1_POS'], visibility=Visibility['VISIBLE'])
RegionFace['PHASE_1_GO'].mechanicalSet=MechanicalSet['STATOR']
faces.assignRegion(region=RegionFace['PHASE_1_GO'])
windingFaces=windingFaces.union(faces)
faces=Line[ALL].complement(Line[ALL])
faces=Face.selectByCoordinates(coordinates=[27.445098968111388,33.37578745405658], coordSys=CoordSys['XY1'])
face=Face.selectByCoordinates(coordinates=[25.13522076693716,35.148219336761855], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[22.70705671870529,28.004519082474875], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[21.173269497543444,29.181435411089602], coordSys=CoordSys['XY1'])
faces=faces.union(face)
RegionFace(name='PHASE_1_RET : Winding phase 1 - Negative direction', 
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='1*TURNS', seriesParallel=ParallelSolidConductorNumber(number=4),
                              electricComponent=CoilConductor['PHASE_1']),
                              material=Material['_B_Copper']), 
           color=Color['PHASE_1_NEG'], visibility=Visibility['VISIBLE'])
RegionFace['PHASE_1_RET'].mechanicalSet=MechanicalSet['STATOR']
faces.assignRegion(region=RegionFace['PHASE_1_RET'])
windingFaces=windingFaces.union(faces)
faces=Line[ALL].complement(Line[ALL])
faces=Face.selectByCoordinates(coordinates=[35.14821933676186,25.135220766937152], coordSys=CoordSys['XY1'])
face=Face.selectByCoordinates(coordinates=[33.375787454056585,27.44509896811138], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[29.181435411089613,21.173269497543444], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[28.00451908247487,22.707056718705278], coordSys=CoordSys['XY1'])
faces=faces.union(face)
RegionFace(name='PHASE_2_GO : Winding phase 2 - Positive direction', 
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='1*TURNS', seriesParallel=ParallelSolidConductorNumber(number=4),
                        electricComponent=CoilConductor['PHASE_2']),
                              material=Material['_B_Copper']), 
           color=Color['PHASE_2_POS'], visibility=Visibility['VISIBLE'])
RegionFace['PHASE_2_GO'].mechanicalSet=MechanicalSet['STATOR']
faces.assignRegion(region=RegionFace['PHASE_2_GO'])
windingFaces=windingFaces.union(faces)
faces=Line[ALL].complement(Line[ALL])
faces=Face.selectByCoordinates(coordinates=[7.08025918873426,42.62682929057864], coordSys=CoordSys['XY1'])
face=Face.selectByCoordinates(coordinates=[4.193630045516839,43.00686122689178], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[5.662628422335464,35.606153305541966], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[3.7458715605020014,35.858499133670115], coordSys=CoordSys['XY1'])
faces=faces.union(face)
RegionFace(name='PHASE_2_RET : Winding phase 2 - Negative direction', 
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='1*TURNS', seriesParallel=ParallelSolidConductorNumber(number=4),
                              electricComponent=CoilConductor['PHASE_2']),
                              material=Material['_B_Copper']), 
           color=Color['PHASE_2_NEG'], visibility=Visibility['VISIBLE'])
RegionFace['PHASE_2_RET'].mechanicalSet=MechanicalSet['STATOR']
faces.assignRegion(region=RegionFace['PHASE_2_RET'])
windingFaces=windingFaces.union(faces)
faces=Line[ALL].complement(Line[ALL])
faces=Face.selectByCoordinates(coordinates=[17.871640459954634,39.34184938227868], coordSys=CoordSys['XY1'])
face=Face.selectByCoordinates(coordinates=[15.181730322467269,40.456046642790824], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[14.68522963612668,32.927306971591605], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[12.899096586836682,33.66714750481032], coordSys=CoordSys['XY1'])
faces=faces.union(face)
RegionFace(name='PHASE_3_GO : Winding phase 3 - Positive direction', 
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='1*TURNS', seriesParallel=ParallelSolidConductorNumber(number=4),
                        electricComponent=CoilConductor['PHASE_3']),
                              material=Material['_B_Copper']), 
           color=Color['PHASE_3_POS'], visibility=Visibility['VISIBLE'])
RegionFace['PHASE_3_GO'].mechanicalSet=MechanicalSet['STATOR']
faces.assignRegion(region=RegionFace['PHASE_3_GO'])
windingFaces=windingFaces.union(faces)
faces=Line[ALL].complement(Line[ALL])
faces=Face.selectByCoordinates(coordinates=[40.45604664279083,15.181730322467258], coordSys=CoordSys['XY1'])
face=Face.selectByCoordinates(coordinates=[39.34184938227869,17.871640459954627], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[33.66714750481033,12.899096586836679], coordSys=CoordSys['XY1'])
faces=faces.union(face)
face=Face.selectByCoordinates(coordinates=[32.9273069715916,14.68522963612667], coordSys=CoordSys['XY1'])
faces=faces.union(face)
RegionFace(name='PHASE_3_RET : Winding phase 3 - Negative direction', 
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='1*TURNS', seriesParallel=ParallelSolidConductorNumber(number=4),
                              electricComponent=CoilConductor['PHASE_3']),
                              material=Material['_B_Copper']), 
           color=Color['PHASE_3_NEG'], visibility=Visibility['VISIBLE'])
RegionFace['PHASE_3_RET'].mechanicalSet=MechanicalSet['STATOR']
faces.assignRegion(region=RegionFace['PHASE_3_RET'])
windingFaces=windingFaces.union(faces)
airFaces=airFaces.complement(windingFaces)
## Infinite box regions
RegionFace['INFINITE'].mechanicalSet=MechanicalSet['STATOR']
infiniteFaces=Face.selectByRelation(formule='Face.region',entities=RegionFace['INFINITE'])
RegionFace['INFINITE'].magneticDC2D=MagneticDC2DFaceVacuum()
airFaces=airFaces.complement(infiniteFaces)
## Air regions
## Air regions
RegionFace(name='AIR : Air', 
           magneticDC2D=MagneticDC2DFaceVacuum(), 
           color=Color['FLUID'], visibility=Visibility['VISIBLE'])
RegionFace['AIR'].mechanicalSet=MechanicalSet['STATOR']
airFaces.assignRegion(region=RegionFace['AIR'])
## Mesh
## Mesh
## Mesh - Geometric parameter
ParameterGeom(name='AG_MESH_COEF : Airgap mesh coefficient', expression='1.5')
## Mesh - General
AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.1)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationHigh()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationHigh())))
RelaxFaceInactive(name='INACTIVFACERELAXATION : Inactive face relaxation', color=Color['Turquoise'])
RelaxLineInactive(name='INACTIVLINERELAXATION : Inactive line relaxation', color=Color['Turquoise'])
## Mesh - Infinite
infiniteFaces=Face.selectByRelation(formule='Face.region',entities=RegionFace['INFINITE'])
infiniteFaces.meshGenerator=None
infiniteFaces.relaxation=RelaxFace['INACTIVFACERELAXATION']
infiniteLines=Line.selectByRelation(formule='inv.Face.edge',entities=infiniteFaces)
infiniteLines.relaxation=RelaxLine['INACTIVLINERELAXATION']
MeshPoint(name='INFINITEMESHPOINT : Infinite box mesh - Point discretization', lengthUnit=LengthUnit['MILLIMETER'], value='(_OS_OD+2*_L_EX)*Sqrt(2)*0.1', color=Color['White'])
infinitePoints=Point.selectByRelation(formule='inv.Line.extrema',entities=infiniteLines)
infinitePoints.mesh=MeshPoint['INFINITEMESHPOINT']
## Mesh - Airgap
AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.1)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationHigh()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationHigh())))
airgapFaces=Face.selectByRelation(formule='Face.region',entities=RegionFace['_AG_INNER','_AG_OUTER'])
airgapFaces.relaxation=RelaxFace['INACTIVFACERELAXATION']
airgapLines=Line.selectByRelation(formule='inv.Face.edge',entities=airgapFaces)
airgapLine1=Line.selectByCoordinates(coordinates=[1.800230794746609E-15,29.4])
airgapLines=airgapLines.complement(airgapLine1)
airgapLine2=Line.selectByCoordinates(coordinates=[1.8247237307295562E-15,29.8])
airgapLines=airgapLines.complement(airgapLine2)
airgapLines.mesh=None
airgapLines.relaxation=RelaxLine['INACTIVLINERELAXATION']
MeshPoint(name='AIRGAPMESHPOINT : Airgap mesh - Point discretization', lengthUnit=LengthUnit['MILLIMETER'], value='(_OS_ID-_IM_OD)/2*AG_MESH_COEF', color=Color['White'])
airgapPoints=Point.selectByRelation(formule='inv.Line.extrema',entities=airgapLines)
airgapPoints.mesh=MeshPoint['AIRGAPMESHPOINT']
MeshLineRelativeDeviation(name='MESHLINE_DEFLR : Airgap mesh - Line deflection', color=Color['White'], relativeDeviationValue=0.1)
airgapMeshPointValue=MeshPoint['AIRGAPMESHPOINT'].value
ParameterGeom(name='TMP : TMP', expression=airgapMeshPointValue)
advanceMode()
ListeLineSegment = []
for i in Line[ALL] : 
    if int(i.coefficients[0]) == 1 :
        ListeLineSegment.append(i)
advanceMode()
ListeLineRegions=Line.selectByRelation(formule='inv.Face.edge Face.region',entities=RegionFace['_AG_INNER','_AG_OUTER'])
ListeInter = [ e for e in ListeLineRegions if not e in ListeLineSegment]
for e in ListeInter :
    res = e.computeLengthLines()
    if ( res[0] < 2*float(ParameterGeom['TMP'].value)/1000 ) :
        e.mesh=MeshLine['MESHLINE_DEFLR']
ParameterGeom['TMP'].delete()
## Mesh - Stator
RelaxFaceUser(name='STATORTOOTHFACERELAXATION : Stator tooth mesh - Face relaxation', color=Color['Turquoise'], r=0.25)
RelaxLineUser(name='STATORTOOTHLINERELAXATION : Stator tooth mesh - Line relaxation', color=Color['Turquoise'], r=0.15)
toothFaces=Face.selectByRelation(formule='Face.region',entities=RegionFace['_OS_TOOTH'])
toothFaces.relaxation=RelaxFace['STATORTOOTHFACERELAXATION']
toothLines=Line.selectByRelation(formule='inv.Face.edge',entities=toothFaces)
toothLines.relaxation=RelaxLine['STATORTOOTHLINERELAXATION']
yokeLines=Line.selectByRelation(formule='inv.Face.edge Face.region',entities=RegionFace['_OS_YOKE'])
airLines=Line.selectByRelation(formule='inv.Face.edge Face.region',entities=RegionFace['AIR'])
interfaceLines=yokeLines.intersection(airLines)
interfaceLines.mesh=None
yokeFaces=Face.selectByRelation(formule='Face.region',entities=RegionFace['_OS_YOKE'])
yokeFaces.relaxation=RelaxFace['STATORTOOTHFACERELAXATION']
yokeLine=Line.selectByCoordinates(coordinates=[54.9,0.0])
yokeLine.relaxation=RelaxLine['STATORTOOTHLINERELAXATION']
meshFaces()
generateSecondOrderElements()
## Parameters
VariationParameterFormula(name='ROTOR_INIT_POS : Rotor initial position', formula='52.498')
VariationParameterFormula(name='REPRESENTED_POLE_NUMBER : Represented pole number', formula='2')
VariationParameterPilot(name='TEMP_MAGNET : Magnet temperature during the test (Tmag)', referenceValue=20.0)
VariationParameterPilot(name='CTRL_ANGLE : Control angle', referenceValue=45.0)
VariationParameterPilot(name='I_RMS : Line current, rms value', referenceValue=103.00634335833354)
VariationParameterFormula(name='I_PEAK : Line current, peak value', formula='I_RMS*Sqrt(2)')
VariationParameterFormula(name='THETA : Variation of angular position', formula='AngPos(ROTOR)-ROTOR_INIT_POS')
VariationParameterFormula(name='I1 : Line current - Phase 1', formula='-I_PEAK*Sin(THETA*_IM_PN/2*Pi()/180+CTRL_ANGLE*Pi()/180)')
VariationParameterFormula(name='J1 : Phase current - Phase 1', formula='I1')
CoilConductor['PHASE_1'].rmsModulus='J1'
VariationParameterFormula(name='I2 : Line current - Phase 2', formula='-I_PEAK*Sin(THETA*_IM_PN/2*Pi()/180+CTRL_ANGLE*Pi()/180-2*Pi()/3)')
VariationParameterFormula(name='J2 : Phase current - Phase 2', formula='I2')
CoilConductor['PHASE_2'].rmsModulus='J2'
VariationParameterFormula(name='I3 : Line current - Phase 3', formula='-I_PEAK*Sin(THETA*_IM_PN/2*Pi()/180+CTRL_ANGLE*Pi()/180-4*Pi()/3)')
VariationParameterFormula(name='J3 : Phase current - Phase 3', formula='I3')
CoilConductor['PHASE_3'].rmsModulus='J3'
Material['_B_NdFeB_1320_1400'].propertyBH=PropertyBhMagnetOneDirection(br='1.32*(1+(-0.001)*(TEMP_MAGNET-20.0))', mur='1.1')
VariationParameterFormula(name='X_PHASE : Phase 1 reference angular position', formula='-30.000000000000004')
## Footer
## Rename geometic parameters
ParameterGeom['_IM_ul'].name='ZIM_ul : Inner magnet - ul'
ParameterGeom['_IM_ua'].name='ZIM_ua : Inner magnet - ua'
ParameterGeom['_IM_uv'].name='ZIM_uv : Inner magnet - uv'
ParameterGeom['_IM_u1'].name='ZIM_u1 : Inner magnet - u1'
ParameterGeom['_IM_TM'].name='IM_TM : Inner magnet - Magnet thickness'
ParameterGeom['_IM_WM'].name='IM_WM : Inner magnet - Magnet width'
ParameterGeom['_IM_H'].name='IM_H : Inner magnet - Space between bar and outer rotor radius'
ParameterGeom['_IM_R'].name='IM_R : Inner magnet - Fillet radius'
ParameterGeom['_IM_OR'].name='ZIM_OR : Inner magnet - Outer radius'
ParameterGeom['_IM_IR'].name='ZIM_IR : Inner magnet - Inner radius'
ParameterGeom['_IM_VE'].name='ZIM_VE : Inner magnet - Half angle of sector'
ParameterGeom['_IM_X1'].name='ZIM_X1 : Inner magnet - x-coordinate of P1'
ParameterGeom['_IM_Y1'].name='ZIM_Y1 : Inner magnet - y-coordinate of P1'
ParameterGeom['_IM_X2'].name='ZIM_X2 : Inner magnet - x-coordinate of P2'
ParameterGeom['_IM_Y2'].name='ZIM_Y2 : Inner magnet - y-coordinate of P2'
ParameterGeom['_IM_X3'].name='ZIM_X3 : Inner magnet - x-coordinate of P3'
ParameterGeom['_IM_Y3'].name='ZIM_Y3 : Inner magnet - y-coordinate of P3'
ParameterGeom['_IM_R3'].name='ZIM_R3 : Inner magnet - Radius to compute P3'
ParameterGeom['_IM_V3'].name='ZIM_V3 : Inner magnet - Angular coordinate of P3'
ParameterGeom['_IM_X4'].name='ZIM_X4 : Inner magnet - x-coordinate of P4'
ParameterGeom['_IM_Y4'].name='ZIM_Y4 : Inner magnet - y-coordinate of P4'
ParameterGeom['_IM_V4'].name='ZIM_V4 : Inner magnet - Angular coordinate of P4'
ParameterGeom['_IM_R4'].name='ZIM_R4 : Inner magnet - Radius to compute P4'
ParameterGeom['_IM_Wa'].name='ZIM_Wa : Inner magnet - Half tooth width'
ParameterGeom['_IM_TX5'].name='ZIM_TX5 : Inner magnet - x-coordinate (u) of P5'
ParameterGeom['_IM_V5'].name='ZIM_V5 : Inner magnet - Angle to compute P5'
ParameterGeom['_IM_R5'].name='ZIM_R5 : Inner magnet - Radius to compute P5'
ParameterGeom['_IM_X5'].name='ZIM_X5 : Inner magnet - x-coordinate of P5'
ParameterGeom['_IM_Y5'].name='ZIM_Y5 : Inner magnet - y-coordinate of P5'
ParameterGeom['_IM_V6'].name='ZIM_V6 : Inner magnet - Angle to compute P6'
ParameterGeom['_IM_X6'].name='ZIM_X6 : Inner magnet - x-coordinate of P6'
ParameterGeom['_IM_Y6'].name='ZIM_Y6 : Inner magnet - y-coordinate of P6'
ParameterGeom['_IM_X5C6'].name='ZIM_X5C6 : Inner magnet - x-coordinate of P5C6'
ParameterGeom['_IM_Y5C6'].name='ZIM_Y5C6 : Inner magnet - y-coordinate of P5C6'
ParameterGeom['_IM_X7'].name='ZIM_X7 : Inner magnet - x-coordinate of P7'
ParameterGeom['_IM_Y7'].name='ZIM_Y7 : Inner magnet - y-coordinate of P7'
ParameterGeom['_IM_X8'].name='ZIM_X8 : Inner magnet - x-coordinate of P8'
ParameterGeom['_IM_Y8'].name='ZIM_Y8 : Inner magnet - y-coordinate of P8'
ParameterGeom['_IM_X9'].name='ZIM_X9 : Inner magnet - x-coordinate of P9'
ParameterGeom['_IM_Y9'].name='ZIM_Y9 : Inner magnet - y-coordinate of P9'
ParameterGeom['_IM_X10'].name='ZIM_X10 : Inner magnet - x-coordinate of P10'
ParameterGeom['_IM_Y10'].name='ZIM_Y10 : Inner magnet - y-coordinate of P10'
ParameterGeom['_IM_X11'].name='ZIM_X11 : Inner magnet - x-coordinate of P11'
ParameterGeom['_IM_Y11'].name='ZIM_Y11 : Inner magnet - y-coordinate of P11'
ParameterGeom['_OS_ul'].name='ZOS_ul : Outer slot - ul'
ParameterGeom['_OS_ua'].name='ZOS_ua : Outer slot - ua'
ParameterGeom['_OS_uv'].name='ZOS_uv : Outer slot - uv'
ParameterGeom['_OS_u1'].name='ZOS_u1 : Outer slot - u1'
ParameterGeom['_OS_HS'].name='OS_HS : Outer slot - Slot height'
ParameterGeom['_OS_WS2'].name='OS_WS2 : Outer slot - Slot width'
ParameterGeom['_OS_H1'].name='OS_H1 : Outer slot - Intermediary height of the slot'
ParameterGeom['_OS_WS1'].name='OS_WS1 : Outer slot - Intermediary width of the slot'
ParameterGeom['_OS_HO'].name='OS_HO : Outer slot - Height of slot opening'
ParameterGeom['_OS_WO'].name='OS_WO : Outer slot - Width of slot opening'
ParameterGeom['_OS_OR'].name='ZOS_OR : Outer slot - Outer radius'
ParameterGeom['_OS_IR'].name='ZOS_IR : Outer slot - Inner radius'
ParameterGeom['_OS_VE'].name='ZOS_VE : Outer slot - Half angle of sector'
ParameterGeom['_OS_X1'].name='ZOS_X1 : Outer slot - x-coordinate of P1'
ParameterGeom['_OS_Y1'].name='ZOS_Y1 : Outer slot - y-coordinate of P1'
ParameterGeom['_OS_X2'].name='ZOS_X2 : Outer slot - x-coordinate of P2'
ParameterGeom['_OS_Y2'].name='ZOS_Y2 : Outer slot - y-coordinate of P2'
ParameterGeom['_OS_X3'].name='ZOS_X3 : Outer slot - x-coordinate of P3'
ParameterGeom['_OS_Y3'].name='ZOS_Y3 : Outer slot - y-coordinate of P3'
ParameterGeom['_OS_X5'].name='ZOS_X5 : Outer slot - x-coordinate of P5'
ParameterGeom['_OS_Y5'].name='ZOS_Y5 : Outer slot - y-coordinate of P5'
ParameterGeom['_OS_X4C5'].name='ZOS_X4C5 : Outer slot - x-coordinate of PT4C5'
ParameterGeom['_OS_Y4C5'].name='ZOS_Y4C5 : Outer slot - y-coordinate of PT4C5'
ParameterGeom['_OS_V1a'].name='ZOS_V1a : Outer slot - Angle V1 (intermediary parameter a)'
ParameterGeom['_OS_V1b'].name='ZOS_V1b : Outer slot - Angle V1 (intermediary parameter b)'
ParameterGeom['_OS_V1'].name='ZOS_V1 : Outer slot - Angle between PT4-PT3 versus x axis'
ParameterGeom['_OS_X4'].name='ZOS_X4 : Outer slot - x-coordinate of PT4'
ParameterGeom['_OS_Y4'].name='ZOS_Y4 : Outer slot - y-coordinate of PT4'
ParameterGeom['_OS_X6'].name='ZOS_X6 : Outer slot - x-coordinate of P6'
ParameterGeom['_OS_Y6'].name='ZOS_Y6 : Outer slot - y-coordinate of P6'
ParameterGeom['_OS_X7'].name='ZOS_X7 : Outer slot - x-coordinate of P7'
ParameterGeom['_OS_Y7'].name='ZOS_Y7 : Outer slot - y-coordinate of P7'
ParameterGeom['_OS_X8'].name='ZOS_X8 : Outer slot - x-coordinate of P8'
ParameterGeom['_OS_Y8'].name='ZOS_Y8 : Outer slot - y-coordinate of P8'
ParameterGeom['_OS_ASa'].name='ZOS_ASa : Outer slot - Slot area (trapezoidal upper)'
ParameterGeom['_OS_ASb'].name='ZOS_ASb : Outer slot - Slot area (trapezoidal middle)'
ParameterGeom['_OS_ASc'].name='ZOS_ASc : Outer slot - Slot area (triangular under bottom)'
ParameterGeom['_OS_ASd'].name='ZOS_ASd : Outer slot - Slot area (round bottom)'
ParameterGeom['_OS_AS'].name='ZOS_AS : Outer slot - Slot area'
ParameterGeom['_OS_K'].name='ZOS_K : Outer slot - Coefficient for computing WC & HTC'
ParameterGeom['_OS_HTC'].name='ZOS_HTC : Outer slot - Height of the upper layer'
ParameterGeom['_OS_WC'].name='ZOS_WC : Outer slot - Width of one layer (Mean value)'
ParameterGeom['_OS_XI1'].name='ZOS_XI1 : Outer slot - x-coordinate of Pi1'
ParameterGeom['_OS_YI1'].name='ZOS_YI1 : Outer slot - y-coordinate of Pi1'
ParameterGeom['_OS_XI2'].name='ZOS_XI2 : Outer slot - x-coordinate of Pi2'
ParameterGeom['_OS_YI2'].name='ZOS_YI2 : Outer slot - y-coordinate of Pi2'
ParameterGeom['_OS_XI3'].name='ZOS_XI3 : Outer slot - x-coordinate of Pi3'
ParameterGeom['_OS_YI3'].name='ZOS_YI3 : Outer slot - y-coordinate of Pi3'
ParameterGeom['_OS_YI4'].name='ZOS_YI4 : Outer slot - y-coordinate of Pi4'
ParameterGeom['_S_ul'].name='ZS_ul : Shaft - ul'
ParameterGeom['_S_ua'].name='ZS_ua : Shaft - ua'
ParameterGeom['_S_uv'].name='ZS_uv : Shaft - uv'
ParameterGeom['_S_u1'].name='ZS_u1 : Shaft - u1'
ParameterGeom['_S_D1'].name='S_D1 : Shaft - Connection Side end-shaft diameter D1'
ParameterGeom['_S_L1'].name='S_L1 : Shaft - Connection Side end-shaft extension L1'
ParameterGeom['_S_D2'].name='S_D2 : Shaft - Opposite Connection Side end-shaft diameter D2'
ParameterGeom['_S_L2'].name='S_L2 : Shaft - Opposite Connection Side end-shaft extension L2'
ParameterGeom['_S_V'].name='ZS_V : Shaft - V'
ParameterGeom['_S_X1'].name='ZS_X1 : Shaft - X1'
ParameterGeom['_S_Y1'].name='ZS_Y1 : Shaft - Y1'
ParameterGeom['_S_X2'].name='ZS_X2 : Shaft - X2'
ParameterGeom['_S_X3'].name='ZS_X3 : Shaft - X3'
ParameterGeom['_S_Y3'].name='ZS_Y3 : Shaft - Y3'
ParameterGeom['_L_ul'].name='ZL_ul : Lamination - ul'
ParameterGeom['_L_ua'].name='ZL_ua : Lamination - ua'
ParameterGeom['_L_uv'].name='ZL_uv : Lamination - uv'
ParameterGeom['_L_u1'].name='ZL_u1 : Lamination - u1'
ParameterGeom['_L_R'].name='L_R : Lamination - Lamination fillet radius'
ParameterGeom['_L_V'].name='ZL_V : Lamination - V'
ParameterGeom['_L_X0'].name='ZL_X0 : Lamination - X0'
ParameterGeom['_L_Y0'].name='ZL_Y0 : Lamination - Y0'
ParameterGeom['_L_X1'].name='ZL_X1 : Lamination - X1'
ParameterGeom['_L_Y1'].name='ZL_Y1 : Lamination - Y1'
ParameterGeom['_L_X2'].name='ZL_X2 : Lamination - X2'
ParameterGeom['_L_Y2'].name='ZL_Y2 : Lamination - Y2'
ParameterGeom['_L_X3'].name='ZL_X3 : Lamination - X3'
ParameterGeom['_L_Y3'].name='ZL_Y3 : Lamination - Y3'
ParameterGeom['_L_X4'].name='ZL_X4 : Lamination - X4'
ParameterGeom['_L_Y4'].name='ZL_Y4 : Lamination - Y4'
ParameterGeom['_L_X5'].name='ZL_X5 : Lamination - X5'
ParameterGeom['_L_Y5'].name='ZL_Y5 : Lamination - Y5'
ParameterGeom['_L_X6'].name='ZL_X6 : Lamination - X6'
ParameterGeom['_L_Y6'].name='ZL_Y6 : Lamination - Y6'
ParameterGeom['_AG_ul'].name='ZAG_ul : Airgap - ul'
ParameterGeom['_AG_ua'].name='ZAG_ua : Airgap - ua'
ParameterGeom['_AG_uv'].name='ZAG_uv : Airgap - uv'
ParameterGeom['_AG_u1'].name='ZAG_u1 : Airgap - u1'
ParameterGeom['_AG_V'].name='ZAG_V : Airgap - V'
ParameterGeom['_AG_X0'].name='ZAG_X0 : Airgap - X0'
ParameterGeom['_AG_Y0'].name='ZAG_Y0 : Airgap - Y0'
ParameterGeom['_AG_X1'].name='ZAG_X1 : Airgap - X1'
ParameterGeom['_AG_Y1'].name='ZAG_Y1 : Airgap - Y1'
ParameterGeom['_AG_X2'].name='ZAG_X2 : Airgap - X2'
ParameterGeom['_AG_Y2'].name='ZAG_Y2 : Airgap - Y2'
ParameterGeom['_AG_X4'].name='ZAG_X4 : Airgap - X4'
ParameterGeom['_AG_Y4'].name='ZAG_Y4 : Airgap - Y4'
ParameterGeom['_AG_X3'].name='ZAG_X3 : Airgap - X3'
ParameterGeom['_AG_Y3'].name='ZAG_Y3 : Airgap - Y3'
ParameterGeom['_AG_X5'].name='ZAG_X5 : Airgap - X5'
ParameterGeom['_AG_Y5'].name='ZAG_Y5 : Airgap - Y5'
ParameterGeom['_AG_X6'].name='ZAG_X6 : Airgap - X6'
ParameterGeom['_AG_Y6'].name='ZAG_Y6 : Airgap - Y6'
## Rename regions
RegionFace['_IM_YOKE'].name='IM_YOKE : Inner magnet - Yoke'
RegionFace['_IM_BRIDGE'].name='IM_BRIDGE : Inner magnet - Bridge'
RegionFace['_IM_POLE_SHOE'].name='IM_POLE_SHOE : Inner magnet - Pole shoe'
RegionFace['_IM_INTER_POLE'].name='IM_INTER_POLE : Inner magnet - Interpole'
RegionFace['_IM_EDGE'].name='IM_EDGE : Inner magnet - Edge'
RegionFace['_OS_YOKE'].name='OS_YOKE : Outer slot - Yoke'
RegionFace['_OS_TOOTH'].name='OS_TOOTH : Outer slot - Tooth'
RegionFace['_OS_TOOTH_FOOT'].name='OS_TOOTH_FOOT : Outer slot - Tooth foot'
RegionFace['_OS_INSULATING_WEDGE'].name='OS_INSULATING_WEDGE : Outer slot - Insulating wedge'
RegionFace['_S_Shaft'].name='S_Shaft : Shaft - Shaft'
RegionFace['_AG_INNER'].name='AG_INNER : Airgap - Inner'
RegionFace['_AG_OUTER'].name='AG_OUTER : Airgap - Outer'
RegionFace['_IM_MAGNET_1'].name='IM_MAGNET_1 : Inner magnet - Magnet'
RegionFace['_IM_MAGNET_2'].name='IM_MAGNET_2 : Inner magnet - Magnet'
RegionFace['INFINITE'].name='INFINITE : Infinite'
## Rename materials
Material['_B_NdFeB_1320_1400'].name='B_NdFeB_1320_1400 : Magnet type material'
Material['_B_M400_65A'].name='B_M400_65A : Lamination type material'
Material['_B_M330_35A'].name='B_M330_35A : Lamination type material'
Material['_B_Copper'].name='B_Copper : Electrical conductor type material'
Material['_B_Nomex_130'].name='B_Nomex_130 : Electrical insulator type material'
Material['_B_EN_1_1151'].name='B_EN_1_1151 : Solid type material'
