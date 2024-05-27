"""
"""


class Reader:
    @staticmethod
    def encode_latin1(file_path):
        """
        Reads an OBJ file and returns a dictionary with the following keys:

        :param file_path: path to the OBJ file
        :return: dictionary with the OBJ data

        The faces are represented as a list of tuples, where each tuple contains the vertex index, texture coordinate index, and normal index.
        """
        data = {
            'vertices': [],
            'texture_coordinates': [],
            'normals': [],
            'faces': []
        }

        with open(file_path, 'r', encoding='latin-1') as f:
            for line in f:
                if line.startswith('v '):
                    vertex = [float(coord) for coord in line.strip().split()[1:]]
                    data['vertices'].append(vertex)
                elif line.startswith('vt '):
                    texture_coord = [float(coord) for coord in line.strip().split()[1:]]
                    data['texture_coordinates'].append(texture_coord)
                elif line.startswith('vn '):
                    normal = [float(coord) for coord in line.strip().split()[1:]]
                    data['normals'].append(normal)
                elif line.startswith('f '):
                    face = [tuple(map(int, vert.split('/'))) for vert in line.strip().split()[1:]]
                    data['faces'].append(face)

        return data
