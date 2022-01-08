from PIL import Image

block_data = { # name = colour, shapeId
    'Concrete Block 1': ('8d8f89', 'a6c6ce30-dd47-4587-b475-085d55c6a3b4'),
    'Wood Block 1': ('9b683a', 'df953d9c-234f-4ac2-af5e-f0490b223e71'),
    'Metal Block 1': ('675f51', '8aedf6c2-94e1-4506-89d4-a0227c552f1e'),
    'Barrier Block': ('ce9e0c', '09ca2713-28ee-4119-9622-e85490034758'),
    'Tile Block': ('bfdfed', '8ca49bff-eeef-4b43-abd0-b527a567f1b7'),
    'Brick Block': ('af967b', '0603b36e-0bdb-4828-b90c-ff19abcdfe34'),
    'Glass Block': ('e4f8ff', '5f41af56-df4c-4837-9b3c-10781335757f'),
    'Glass Tile Block': ('c2f9ff', '749f69e0-56c9-488c-adf6-66c58531818f'),
    'Path Light Block': ('727272', '073f92af-f37e-4aff-96b3-d66284d5081c'),
    'Spaceship Block': ('820a0a', '027bd4ec-b16d-47d2-8756-e18dc2af3eb6'),
    'Cardboard Block': ('a48052', 'f0cba95b-2dc4-4492-8fd9-36546a4cb5aa'),
    'Scrap Wodd Block': ('cd9d71', '1fc74a28-addb-451a-878d-c3c605d63811'),
    'Wood Block 2': ('dc9153', '1897ee42-0291-43e4-9645-8c5a5d310398'),
    'Wood Block 3': ('f2ad74', '061b5d4b-0a6a-4212-b0ae-9e9681f1cbfb'),
    'Scrap Metal Block': ('df6226', '1f7ac0bb-ad45-4246-9817-59bdf7f7ab39'),
    'Metal Block 2': ('869499', '1016cafc-9f6b-40c9-8713-9019d399783f'),
    'Metal Block 3': ('88a5ac', 'c0dfdea5-a39d-433a-b94a-299345a5df46'),
    'Scrap Stone Block': ('848484', '30a2288b-e88e-4a92-a916-1edbfc2b2dac'),
    'Concrete Block 2': ('8d8f89', 'ff234e42-5da4-43cc-8893-940547c97882'),
    'Concrete Block 3': ('c9d7dc', 'e281599c-2343-4c86-886e-b2c1444e8810'),
    'Cracked Concrete Block': ('8d8f89', 'f5ceb7e3-5576-41d2-82d2-29860cf6e20e'),
    'Concrete Slab Block': ('af967b', 'cd0eff89-b693-40ee-bd4c-3500b23df44e'),
    'Rusted Metal Block': ('738192', '220b201e-aa40-4995-96c8-e6007af160de'),
    'Extruded Metal Block': ('858795', '25a5ffe7-11b1-4d3e-8d7a-48129cbaf05e'),
    'Bubble Plastic Block': ('9acfd2', 'f406bf6e-9fd5-4aa0-97c1-0b3c2118198e'),
    'Plastic Block': ('0b9ade', '628b2d61-5ceb-43e9-8334-a4135566df7a'),
    'Insulation Block': ('fff063', '9be6047c-3d44-44db-b4b9-9bcf8a9aab20'),
    'Plaster block': ('979797', 'b145d9ae-4966-4af6-9497-8fca33f9aee3'),
    'Carpet Block': ('368085', 'febce8a6-6c05-4e5d-803b-dfa930286944'),
    'Painted Wall Blovk': ('eeeeee', 'e981c337-1c8a-449c-8602-1dd990cbba3a'),
    'Net Block': ('435359', '4aa2a6f0-65a4-42e3-bf96-7dec62570e0b'),
    'Solid Net Block': ('888888', '3d0b7a6e-5b40-474c-bbaf-efaa54890e6a'),
    'Punched Steel Block': ('888888', 'ea6864db-bb4f-4a89-b9ec-977849b6713a'),
    'Striped Net Block': ('888888', 'a479066d-4b03-46b5-8437-e99fec3f43ee'),
    'Square Mesh Block': ('c36512', 'b4fa180c-2111-4339-b6fd-aed900b57093'),
    'Restroom Block': ('607b79', '920b40c8-6dfc-42e7-84e1-d7e7e73128f6'),
    'Diamond Plate Block': ('43494d', 'f7d4bfed-1093-49b9-be32-394c872a1ef4'),
    'Aluminum Block': ('727272', '3e3242e4-1791-4f70-8d1d-0ae9ba3ee94c'),
    'Worn Metal Block': ('66837c', 'd740a27d-cc0f-4866-9e07-6a5c516ad719'),
    'Spaceship Floor Block': ('dadada', '4ad97d49-c8a5-47f3-ace3-d56ba3affe50'),
    'Sand Block': ('c69146', 'c56700d9-bbe5-4b17-95ed-cef05bd8be1b'),
    'Armored Glass Block': ('3abfb1', 'b5ee5539-75a2-4fef-873b-ef7c9398b3f5')
}

def rgb_to_hex(rgb): # convert an RGB tuple to a hex str
    return '%02x%02x%02x' % rgb

def unwrap_image(image): # open an image and identify all the pixels
    image = Image.open(image)
    pixels = image.load()
    wrap = []
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            wrap.append((x,y,pixels[x,y]))
    return wrap

class part: # class for a part in a blueprint

    def __init__(self,bounds,colour,pos,shapeId,xaxis,zaxis): # bounds=(x,y,z) colour=hex pos=(x,y,z) shapeId=str xaxis=int zaxis=int
                                                              # example: {"bounds":{"x":1,"y":1,"z":1},"color":"820a0a","pos":{"x":-5,"y":-3,"z":2},"shapeId":"027bd4ec-b16d-47d2-8756-e18dc2af3eb6","xaxis":1,"zaxis":3}
        self.bounds = bounds
        self.colour = colour
        self.pos = pos
        self.shapeId = shapeId
        self.xaxis = xaxis
        self.zaxis = zaxis

    def to_str(self): # return the json format for the part
        return '{{"bounds":{{"x":{},"y":{},"z":{}}},"color":"{}","pos":{{"x":{},"y":{},"z":{}}},"shapeId":"{}","xaxis":{},"zaxis":{}}}'.format(self.bounds[0],self.bounds[1],self.bounds[2],self.colour,self.pos[0],self.pos[1],self.pos[2],self.shapeId,self.xaxis,self.zaxis)

class blueprint: # class for a blueprint

    def __init__(self,childs,version): # childs=[] version=int 
                                       # example: {"bodies":[{"childs":[]}],"version":3}
        self.childs = childs
        self.version = version

    def to_str(self): # return the json format for the blueprint
        return '{{"bodies":[{{"childs":[{}]}}],"version":{}}}'.format(','.join([child.to_str() for child in self.childs]),self.version)

    def add(self,child): # add a new part to the blueprint
        self.childs.append(child)

    def save(self,name): # save the blueprint to a usable json file
        file = open(name,'w')
        file.write(self.to_str())
        file.close()

    def from_image(name): # create a blueprint from an image file
        unwrap = unwrap_image(name)
        bp = blueprint([],3)
        for x,y,colour in unwrap:
            bp.add(part((1,1,1),rgb_to_hex(colour),(-x,y,0),'027bd4ec-b16d-47d2-8756-e18dc2af3eb6',1,3))
        return bp

# sample tool usage
# a = part((1,1,1),'ff00ff',(-5,-3,2),'027bd4ec-b16d-47d2-8756-e18dc2af3eb6',1,3)
# b = part((1,1,1),'00ff00',(-5,-3,3),'027bd4ec-b16d-47d2-8756-e18dc2af3eb6',1,3)
# c = blueprint([a,b],3)
# print(c.to_str())

a = blueprint.from_image('image.png')
a.save('output blueprint.json')
