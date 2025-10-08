class Point2D:
    def init(self, x, y, color):
        self.x = float(x)
        self.y = float(y)
        self.color = color.strip('"')
    
    def str(self):
        return f"Point2D(x={self.x}, y={self.y}, color='{self.color}')"

class Rhombus:
    def init(self, x1, y1, x2, y2, x3, y3, x4, y4, color, side_length):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.x3 = float(x3)
        self.y3 = float(y3)
        self.x4 = float(x4)
        self.y4 = float(y4)
        self.color = color.strip('"')
        self.side_length = float(side_length)
    
    def str(self):
        return f"Rhombus(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2}, x3={self.x3}, y3={self.y3}, x4={self.x4}, y4={self.y4}, color='{self.color}', side_length={self.side_length})"

def parse_object(line):
    parts = line.split()
    if parts[0] == "Point2D" and len(parts) == 4:
        return Point2D(parts[1], parts[2], parts[3])
    elif parts[0] == "Rhombus" and len(parts) == 11:
        return Rhombus(parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10])
    elif parts[0] == "RhombusSimple" and len(parts) == 5:  # Новый случай
        return Rhombus(parts[1], parts[1], parts[2], parts[2], parts[3], parts[3], parts[4], parts[4], parts[5], 1.0)
    else:
        print("ошибка: неверный формат строки")
        return None

def parse_many_objects(text):
    objects = []
    lines = text.split(';')
    for line in lines:
        line = line.strip()
        if line:
            obj = parse_object(line)
            if obj:
                objects.append(obj)
    return objects

test_cases = [
    'Point2D 1.0 2.0 "red"',
    'Rhombus 0.0 0.0 1.0 1.0 2.0 0.0 1.0 -1.0 "blue" 1.414',
    'RhombusSimple 0.0 1.0 2.0 3.0 "green"',
    'Point2D 0.0 1.0 "green"; Rhombus 0.0 0.0 1.0 1.0 2.0 0.0 1.0 -1.0 "blue" 1.414'
]

for test in test_cases:
    objs = parse_many_objects(test)
    for obj in objs:
        print(obj)