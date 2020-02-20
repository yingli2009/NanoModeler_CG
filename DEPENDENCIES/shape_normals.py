import numpy as np

def sphere_normal(xyz, inp):
    normal = xyz/np.linalg.norm(xyz)
    return normal

def ellipsoid_normal(xyz, inp):
    normal = np.divide(xyz, np.power(inp.core_ellipse_axis,2))
    normal /= np.linalg.norm(normal)
    return normal

def cylinder_normal(xyz, inp):
    if (xyz[0]**2 + xyz[1]**2 + (np.abs(xyz[2])-inp.core_cylinder[1]/2)**2) < (inp.core_cylinder[0]**2):
        normal = np.array([0,0,np.sign(xyz[2])])
    else:
        normal = xyz.copy()
        normal[2] = 0.0
        normal /= np.linalg.norm(normal)
    return normal

def rectangular_prism_normal(xyz, inp):
    a, b, c = inp.core_rect_prism
    plane_normals = np.identity(3)
    pts_inplane = np.array([[a,0,0],[0,b,0],[0,0,c]])/2
    D = -1*np.array([np.dot(plane_normal, pt_inplane) for plane_normal, pt_inplane in zip(plane_normals, pts_inplane)])
    dists = np.divide(np.abs(np.dot(plane_normals,np.abs(xyz))+D), np.linalg.norm(plane_normals, axis=1))
    normals = np.zeros(3)
    normals[np.argmin(dists)] = np.sign(xyz[np.argmin(dists)])
    return normals

def rod_normal(xyz, inp):
    if (xyz[0]**2 + xyz[1]**2 + (np.abs(xyz[2])-inp.core_rod_params[1]/2)**2) < (inp.core_rod_params[0]**2):
        normal = xyz - np.array([0,0,np.sign(xyz[2])*inp.core_rod_params[1]/2])
    else:
        normal = xyz.copy()
        normal[2] = 0.0
    normal /= np.linalg.norm(normal)
    return normal

def pyramid_normal(xyz, inp):
    return xyz

def octahedron_normal(xyz, inp):
    return xyz