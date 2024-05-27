import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from VisualShape3D.plotable import Plotable, OpenView, Origin
from VisualShape3D.geometry import Point
from VisualShape3D.shapes import add_col, rectangle



# define a collection of classes
__modelClassList = []

def modelClass(each_definition):
    __modelClassList.append(each_definition)
    return each_definition


# 新类 VisualSHape3D 继承自 OpenView
@modelClass
class VisualShape3D(OpenView):

    @staticmethod
    def Usage():
        return  f"vs3D = {VisualShape3D.__name__}(style = None)"
    
    def itsInput(self):
        return self.__repr__()

    def __init__(self, style=None):
        # 初始化父类
        super().__init__()

        self.shapes = []    # 存储所有的形状
        
        if style is None :  # by default
            pass
        else:
            self.set_style(style)

        self.input_str = f"type = {type}"

    def __str__(self):
        return f"{self.__class__.__name__}"
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.input_str})"

    def add_shape(self, shape, style = None):
        """添加形状到视图中"""
        
        if style == None :
            style = {}
            style['facecolor'] = self.facecolor    
            style['edgecolor'] = self.edgecolor    
            style['color']     = self.color      
            style['linewidth'] = self.linewidth   
            style['linestyle'] = self.linestyle   
            style['alpha']     = self.alpha      
            style['marker']    = self.marker     
            
        else :
            if 'facecolor' not in style : style['facecolor'] = self.facecolor    
            if 'edgecolor' not in style : style['edgecolor'] = self.edgecolor    
            if 'color'     not in style : style['color']     = self.color      
            if 'linewidth' not in style : style['linewidth'] = self.linewidth   
            if 'linestyle' not in style : style['linestyle'] = self.linestyle   
            if 'alpha'     not in style : style['alpha']     = self.alpha      
            if 'makrer'    not in style : style['marker']    = self.marker     

        # vertices, _ = self.add_vertice(shape)
        # shape.vertices = vertices

        shape.set_style(style)
        self.shapes.append(shape)
        # print(f"Shape added: {new_shape.get_title()}")

    def show(self, elev= 20.0, azim = -80.0, axes = "off", origin = "on", **kwargs):
        """展示所有形状"""
        ax = self.get_ax()
        if ax is None :
            return
      
        ax.view_init(elev, azim)
        hideAxes = axes.lower() == "off"
        if hideAxes :
            ax.set_axis_off()

        if origin.lower() == "on":
            R0 = Origin()
            self.add_plot(R0)
            
        for shape in self.shapes:
            # print(shape.get_title())
            style = shape.get_style()
            self.add_plot(shape, style = style, hideAxes = hideAxes, **kwargs)

        plt.show()

        return ax        

class simpleShape():
    def __init__(self, title, edges = [(0,0),(1,0),(1,1),(0,1)]):
        vertices = np.asarray(edges)
        if vertices.shape[1] == 2:
            vertices = np.hstack((add_col(vertices.shape[0])*0, vertices))         
        self.vertices = vertices
        self.title = title

@modelClass
class Model(Plotable):
    @staticmethod
    def Usage():
        return  f"class myClass({__class__.__name__})： ... ..."
    
    def itsInput(self):
        return self.__repr__()

    def __init__(self):
        super().__init__()

        # self.vertices = []  # the existing library of vertices
        self.title = ''
        self.hidden = False
        self.shapes = []
        self.vertices = []
        self.input_str = f""

    def __str__(self):
        return f"{self.__repr__()} : \n vertices {len(self.vertices)}"
        
    def __repr__(self):
        return f"{self.title}({self.input_str})"

    def set_title(self,title):
        self.title = title

    def turn_off(self):
        self.hidden = True

    def turn_on(self):
        self.hidden = False

    # For visualization
    def get_instance(self): 
        return self
    
    def get_domain(self):
        """
        :returns: opposite vertices of the bounding prism for this object.
        :       ndarray([min], [max])
        """
        # Min/max along the column
        vertices = np.asarray(self.vertices)
        x,y,z = zip(*vertices)
        min_x, max_x = np.min(x), np.max(x)
        min_y, max_y = np.min(y), np.max(y)
        min_z, max_z = np.min(z), np.max(z)
        
        return np.array([[min_x,min_y,min_z],[max_x,max_y,max_z]])

    def iplot(self, style, ax, **kwargs):
        if self.hidden :
            return

        if self.shapes == [] :
            return

        # Plot the model
        model = []
        for shape in self.shapes:
            model.append(shape.vertices)

        # ax.add_collection3d(Poly3DCollection(model, facecolors='cyan', linewidths=1, edgecolors='r'))
        ax.add_collection3d(Poly3DCollection(model, 
                 facecolors=style['facecolor'], linewidths=style['linewidth'], edgecolors=style['edgecolor']))
        

    # Create the relationship by adding vertices
    def add_shape(self, title, shape = rectangle(1,1)):
        vertices = self.add_vertice(shape)
        self.shapes.append(simpleShape(title,vertices))

    def add_vertice(self,shape):  # merge the identical vertices
        vertices = list()
        indices = list()
        vertice_number = 0
        for P in shape:
            k = self.contain_vertice(P)  
            if k < 0 :
   
                V = list(P)  # V, P 为两块内存的个独立指针
                i = vertice_number
                vertice_number += 1
                self.vertices.append(V)
   
            else :
                V = self.vertices[k]  # 获得指针
                i = k
          
            vertices.append(V)
            indices.append(i)

        return vertices

    def contain_vertice(self, P) :
        a = Point(*list(P))

        for k,v in enumerate(self.vertices) :
            b = Point(*list(v))
            if a == b :
                return k
        return -1


    def show(self, elev= 20.0, azim = -80.0, axes = "off", origin = "off", style = {}, **kwargs):
        
        """展示所有形状"""
        ax = self.get_ax()
        if ax is not None:
            self.close()   #  close the existing figure

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.view_init(elev, azim)

        self.set_ax(ax)
        self.set_fig(fig)

        hideAxes = axes.lower() == "off"
        if hideAxes :
            ax.set_axis_off()

        if origin.lower() == "on":
            R0 = Origin()
            self.add_plot(R0)

        self.plot( style = style, ax = ax, **kwargs )

        plt.show()

@modelClass
class Cube(Model):
    @staticmethod
    def Usage():
        return  f"obj = {__class__.__name__}(width=1,height=1,length=1)"

    def __init__(self,width=1,height=1,length=1):
        super().__init__()
        self.create(width,height,length)
        self.input_str = f" width={width}, height={height} ,length={length} "
 
    def create(self,width,height,length):
        vertices = np.array([[0, 0, 0],
                      [0, length, 0],
                      [width, length, 0],
                      [width, 0, 0],
                      [0, 0, height],
                      [0, length, height],
                      [width, length, height],
                      [width, 0, height]])
        
        face1 = [vertices[0], vertices[1], vertices[2], vertices[3]]
        face2 = [vertices[4], vertices[5], vertices[6], vertices[7]]
        face3 = [vertices[0], vertices[1], vertices[5], vertices[4]]
        face4 = [vertices[1], vertices[2], vertices[6], vertices[5]]
        face5 = [vertices[2], vertices[3], vertices[7], vertices[6]]
        face6 = [vertices[3], vertices[0], vertices[4], vertices[7]]
        
        faces = []
        faces.append(face1)
        faces.append(face2)
        faces.append(face3)
        faces.append(face4)
        faces.append(face5)
        faces.append(face6) 
        for i,face in enumerate(faces) :
            self.add_shape(f'face{i}',face)
            
        self.set_title('Cube')

@modelClass
class Sphere(Model):
    def __init__(self, R=1 , center = (0, 0, 0)):
        super().__init__()
        a,b,c = center
        x,y,z = self.create(R,a,b,c)
        self.vertices = np.array(list(zip(x,y,z)))
        self.input_str = f" R={R} , center = {(a,b,c)}"

    @staticmethod
    def Usage():
        return  f"obj = {__class__.__name__}( R=1 , center = (0, 0, 0))"

    def create(self, R,a=0,b=0,c=0):
        # 参数化方程
        theta = np.linspace(0, 2*np.pi, 100)
        phi = np.linspace(0, np.pi, 100)
        x = a + R * np.outer(np.cos(theta), np.sin(phi))
        y = b + R * np.outer(np.sin(theta), np.sin(phi))
        z = c + R * np.outer(np.ones(np.size(theta)), np.cos(phi))
        # return x.tolist(),y.tolist(),z.tolist()
        return x,y,z

    def iplot(self, style, ax, **kwargs):
        if self.hidden :
            return

        # Plot the model
        x, y, z = zip(*self.vertices)
        x, y, z = np.asarray(x), np.asarray(y), np.asarray(z)
        # ax.plot_surface(x, y, z, color=style['facecolor'], alpha=style['alpha'])
        ax.plot_surface(x, y, z, color='b', alpha=0.6)
@modelClass
class ConicalSurface(Model):
    @staticmethod
    def Usage():
        return  f"obj = {ConicalSurface.__name__}(h,r, a=0,b=0,c=0)"

    def __init__(self, h,r, a=0,b=0,c=0):
        super().__init__()

        # 生成圆锥侧面的直线数据
        theta = np.linspace(0, 2*np.pi, 100)
        x = a + r * np.cos(theta)
        y = b + r * np.sin(theta)
        z = c + np.linspace(0, h, 100) 

        self.vertices = list(zip(x,y,z))
        self.input_str = f" h={h}, r={r}, a={a}, b={b}, c={c}" 
        self.set_title(f"{self.__class__.__name__}")


    def iplot(self, style, ax, **kwargs):
        if self.hidden :
            return

        # Plot the model
        x, y, z = zip(*self.vertices)
        X, Y, Z = np.array([x, x]), np.array([y, y]), np.array([z, np.zeros_like(z)])

        ax.plot_surface(X,Y,Z, color=style['facecolor'], alpha=style['alpha'])



# create a namelist of these function
__classNames = [each.__name__ for each in __modelClassList ]
def visualModelList():
    return __classNames

def howtoUseClass(className):
    name = [x.lower() for x in visualModelList()]
    i = name.index(className.lower())
    return __modelClassList[i].Usage()


# 使用示例
def demo_model():
    vs3d = Model()
    vs3d.add_shape("Sphere")
    vs3d.add_shape("Cube")
    vs3d.show()

def demo_cube():
    cube = Cube(5, 3, 2)
    cube.show(elev= 20.0, azim = -45.0, style={'facecolor':'y'})

if __name__ == "__main__":
    demo_cube()