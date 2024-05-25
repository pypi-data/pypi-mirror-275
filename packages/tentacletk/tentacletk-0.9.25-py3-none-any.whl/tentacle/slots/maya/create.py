# !/usr/bin/python
# coding=utf-8
try:
    import pymel.core as pm
except ImportError as error:
    print(__file__, error)
import mayatk as mtk
from tentacle.slots.maya import SlotsMaya


class Create(SlotsMaya):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def cmb001_init(self, widget):
        """ """
        items = ["Polygon", "NURBS", "Light"]
        widget.add(items)

        widget.currentIndexChanged.connect(
            lambda i, w=widget: self.cmb002_init(w.ui.cmb002)
        )

    def cmb002_init(self, widget):
        """ """
        index = widget.ui.cmb001.currentIndex()

        if index == 1:
            items = [
                "Cube",
                "Sphere",
                "Cylinder",
                "Cone",
                "Plane",
                "Torus",
                "Circle",
                "Square",
            ]

        elif index == 2:
            items = ["Ambient", "Directional", "Point", "Spot", "Area", "Volume"]

        else:  # Default to polygon  primitives.
            items = [
                "Cube",
                "Sphere",
                "Cylinder",
                "Plane",
                "Circle",
                "Cone",
                "Pyramid",
                "Torus",
                "Tube",
                "GeoSphere",
                "Platonic Solids",
                "Text",
            ]

        widget.add(items, clear=True)

    def tb000_init(self, widget):
        """ """
        widget.menu.add(
            "QCheckBox",
            setText="Translate",
            setObjectName="chk000",
            setChecked=True,
            setToolTip="Move the created object to the center point of any selected object(s).",
        )
        widget.menu.add(
            "QCheckBox",
            setText="Scale",
            setObjectName="chk001",
            setChecked=True,
            setToolTip="Uniformly scale the created object to match the averaged scale of any selected object(s).",
        )

    def tb000(self, widget):
        """Create Primitive"""
        baseType = self.sb.create.cmb001.currentText()
        subType = self.sb.create.cmb002.currentText()
        scale = widget.menu.chk001.isChecked()
        translate = widget.menu.chk000.isChecked()

        hist_node = self.createDefaultPrimitive(baseType, subType, scale, translate)
        pm.selectMode(object=True)  # place scene select type in object mode.
        pm.select(hist_node)  # select the transform node so that you can see any edits

    def b001(self):
        """Create poly cube"""
        self.createDefaultPrimitive("Polygon", "Cube")

    def b002(self):
        """Create poly sphere"""
        self.createDefaultPrimitive("Polygon", "Sphere")

    def b003(self):
        """Create poly cylinder"""
        self.createDefaultPrimitive("Polygon", "Cylinder")

    def b004(self):
        """Create poly plane"""
        self.createDefaultPrimitive("Polygon", "Plane")

    def b005(self):
        """Create 6 sided poly cylinder"""
        cyl = self.createDefaultPrimitive("Polygon", "Cylinder")
        mtk.set_node_attributes(cyl, subdivisionsAxis=6)

    def createDefaultPrimitive(
        self, baseType, subType, scale=False, translate=False, axis=[0, 90, 0]
    ):
        """ """
        baseType = baseType.lower()
        subType = subType.lower()

        selection = pm.ls(sl=True, transforms=1)

        primitives = {
            "polygon": {
                "cube": "pm.polyCube(axis=axis, width=5, height=5, depth=5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1)",
                "sphere": "pm.polySphere(axis=axis, radius=5, subdivisionsX=12, subdivisionsY=12)",
                "cylinder": "pm.polyCylinder(axis=axis, radius=5, height=10, subdivisionsX=12, subdivisionsY=1, subdivisionsZ=1)",
                "plane": "pm.polyPlane(axis=axis, width=5, height=5, subdivisionsX=1, subdivisionsY=1)",
                "circle": "self.createCircle(axis=axis, numPoints=12, radius=5, mode=0)",
                "cone": "pm.polyCone(axis=axis, radius=5, height=5, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1)",
                "pyramid": "pm.polyPyramid(axis=axis, sideLength=5, numberOfSides=5, subdivisionsHeight=1, subdivisionsCaps=1)",
                "torus": "pm.polyTorus(axis=axis, radius=10, sectionRadius=5, twist=0, subdivisionsX=5, subdivisionsY=5)",
                "pipe": "pm.polyPipe(axis=axis, radius=5, height=5, thickness=2, subdivisionsHeight=1, subdivisionsCaps=1)",
                "geosphere": "pm.polyPrimitive(axis=axis, radius=5, sideLength=5, polyType=0)",
                "platonic solids": 'pm.mel.eval("performPolyPrimitive PlatonicSolid 0;")',
            },
            "nurbs": {
                "cube": "pm.nurbsCube(ch=1, d=3, hr=1, p=(0, 0, 0), lr=1, w=1, v=1, ax=(0, 1, 0), u=1)",
                "sphere": "pm.sphere(esw=360, ch=1, d=3, ut=0, ssw=0, p=(0, 0, 0), s=8, r=1, tolerance=0.01, nsp=4, ax=(0, 1, 0))",
                "cylinder": "pm.cylinder(esw=360, ch=1, d=3, hr=2, ut=0, ssw=0, p=(0, 0, 0), s=8, r=1, tolerance=0.01, nsp=1, ax=(0, 1, 0))",
                "cone": "pm.cone(esw=360, ch=1, d=3, hr=2, ut=0, ssw=0, p=(0, 0, 0), s=8, r=1, tolerance=0.01, nsp=1, ax=(0, 1, 0))",
                "plane": "pm.nurbsPlane(ch=1, d=3, v=1, p=(0, 0, 0), u=1, w=1, ax=(0, 1, 0), lr=1)",
                "torus": "pm.torus(esw=360, ch=1, d=3, msw=360, ut=0, ssw=0, hr=0.5, p=(0, 0, 0), s=8, r=1, tolerance=0.01, nsp=4, ax=(0, 1, 0))",
                "circle": "pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tolerance=0.01, nr=(0, 1, 0))",
                "square": "pm.nurbsSquare(c=(0, 0, 0), ch=1, d=3, sps=1, sl1=1, sl2=1, nr=(0, 1, 0))",
            },
            "light": {
                "ambient": "pm.ambientLight()",  # defaults: 1, 0.45, 1,1,1, "0", 0,0,0, "1"
                "directional": "pm.directionalLight()",  # 1, 1,1,1, "0", 0,0,0, 0
                "point": "pm.pointLight()",  # 1, 1,1,1, 0, 0, 0,0,0, 1
                "spot": "pm.spotLight()",  # 1, 1,1,1, 0, 40, 0, 0, 0, 0,0,0, 1, 0
                "area": 'pm.shadingNode("areaLight", asLight=True)',  # 1, 1,1,1, 0, 0, 0,0,0, 1, 0
                "volume": 'pm.shadingNode("volumeLight", asLight=True)',  # 1, 1,1,1, 0, 0, 0,0,0, 1
            },
        }

        node = eval(primitives[baseType][subType])
        # if originally there was a selected object, move the object to that objects's bounding box center.
        if selection:
            if translate:
                mtk.move_to(node, selection)
                # center_pos = mtk.get_center_point(selection)
                # pm.xform(node, translation=center_pos, worldSpace=1, absolute=1)
            if scale:
                mtk.match_scale(node[0], selection, average=True)

        mtk.add_to_isolation_set(node)

        return mtk.get_history_node(node[0])

    @mtk.undo
    def createCircle(
        self, axis="y", numPoints=5, radius=5, center=[0, 0, 0], mode=0, name="pCircle"
    ):
        """Create a circular polygon plane.

        Parameters:
            axis (str): 'x','y','z'
            numPoints(int): number of outer points
            radius=int
            center=[float3 list] - point location of circle center
            mode(int): 0 -no subdivisions, 1 -subdivide tris, 2 -subdivide quads

        Returns:
            (list) [transform node, history node] ex. [nt.Transform('polySurface1'), nt.PolyCreateFace('polyCreateFace1')]

        Example: self.createCircle(axis='x', numPoints=20, radius=8, mode='tri')
        """
        import math

        degree = 360 / float(numPoints)
        radian = math.radians(degree)  # or math.pi*degree/180 (pi * degrees / 180)

        vertexPoints = []
        for _ in range(numPoints):
            # print("deg:", degree,"\n", "cos:",math.cos(radian),"\n", "sin:",math.sin(radian),"\n", "rad:",radian)
            if axis == "x":  # x axis
                y = center[2] + (math.cos(radian) * radius)
                z = center[1] + (math.sin(radian) * radius)
                vertexPoints.append([0, y, z])
            if axis == "y":  # y axis
                x = center[2] + (math.cos(radian) * radius)
                z = center[0] + (math.sin(radian) * radius)
                vertexPoints.append([x, 0, z])
            else:  # z axis
                x = center[0] + (math.cos(radian) * radius)
                y = center[1] + (math.sin(radian) * radius)
                vertexPoints.append([x, y, 0])  # not working.

            # increment by original radian value that was converted from degrees
            radian = radian + math.radians(degree)
            # print(x,y,"\n")

        # pm.undoInfo (openChunk=True)
        node = pm.ls(pm.polyCreateFacet(point=vertexPoints, name=name))
        # returns: ['Object name', 'node name']. pymel 'ls' converts those to objects.
        pm.polyNormal(node, normalMode=4)  # 4=reverse and propagate
        if mode == 1:
            pm.polySubdivideFacet(divisions=1, mode=1)
        if mode == 2:
            pm.polySubdivideFacet(divisions=1, mode=0)
        # pm.undoInfo (closeChunk=True)

        return node


# --------------------------------------------------------------------------------------------


# module name
# print(__name__)
# --------------------------------------------------------------------------------------------
# Notes
# --------------------------------------------------------------------------------------------
