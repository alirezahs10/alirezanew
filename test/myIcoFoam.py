# state file generated using paraview version 5.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [894, 472]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [32.000003814697266, 29.730732917785645, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [74.18531357628378, 25.2980258871169, 262.8099620385791]
renderView1.CameraFocalPoint = [53.51705295344024, 24.60016482770565, -1.6679636104556121]
renderView1.CameraViewUp = [0.3644754825136034, 0.9306988914820971, -0.03093858497850119]
renderView1.CameraParallelScale = 46.89629264249878
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVFoamReader'
testOpenFOAM = PVFoamReader(FileName='/home/naristein/Desktop/nariman/homework_nu_5/test/test.OpenFOAM')
testOpenFOAM.MeshParts = ['internalMesh', 'wall-4 - wall', 'velocity-inlet-5 - patch', 'velocity-inlet-6 - patch', 'pressure-outlet-7 - patch', 'wall-8 - wall']
testOpenFOAM.VolumeFields = ['p', 'U']

# create a new 'Clip'
clip1 = Clip(Input=testOpenFOAM)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 4104.33154296875

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [32.0000038146973, 29.7307329177856, 0.0]
clip1.ClipType.Normal = [0.0, 0.0, -1.0]

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=testOpenFOAM,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 66.48237813949585

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.1, -4.53853416442871, -0.937738299369812]
streamTracer1.SeedType.Point2 = [0.1, 20.0, 0.937738299369812]

# create a new 'Tube'
tube1 = Tube(Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.12984421938657761

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 2.703274715115702, 0.865003, 0.865003, 0.865003, 5.406549430231404, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 5.406549430231404, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from testOpenFOAM
testOpenFOAMDisplay = Show(testOpenFOAM, renderView1)
# trace defaults for the display properties.
testOpenFOAMDisplay.Representation = 'Surface'
testOpenFOAMDisplay.ColorArrayName = ['POINTS', 'U']
testOpenFOAMDisplay.LookupTable = uLUT
testOpenFOAMDisplay.OSPRayScaleArray = 'U'
testOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
testOpenFOAMDisplay.SelectOrientationVectors = 'None'
testOpenFOAMDisplay.ScaleFactor = 6.853853416442871
testOpenFOAMDisplay.SelectScaleArray = 'None'
testOpenFOAMDisplay.GlyphType = 'Arrow'
testOpenFOAMDisplay.GlyphTableIndexArray = 'None'
testOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
testOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# show color legend
testOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# show data from clip1
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'U']
clip1Display.LookupTable = uLUT
clip1Display.OSPRayScaleArray = 'U'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 6.853853416442871
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = uPWF
clip1Display.ScalarOpacityUnitDistance = 9.163016118257065

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', 'U']
streamTracer1Display.LookupTable = uLUT
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 5.193768775463105
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# show color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# show data from tube1
tube1Display = Show(tube1, renderView1)
# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['POINTS', 'U']
tube1Display.LookupTable = uLUT
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 5.232017874717712
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# show color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for vtkBlockColorsLUT in view renderView1
vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
vtkBlockColorsLUTColorBar.ComponentTitle = ''

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(streamTracer1)
# ----------------------------------------------------------------