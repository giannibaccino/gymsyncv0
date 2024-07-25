class Kart():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        kart = self.session.get('kart')
        
        if not kart:
            kart = self.session['kart'] = {}
        # else:
        self.kart=kart
            
    def add_prod(self, producto):
        if(str(producto.id) not in self.kart.keys()):
            
            self.kart[producto.id] = {
                'producto_id':producto.id,
                'nombre':producto.nombre,
                # 'categoria': producto.categoria,
                'precio':str(producto.precio),
                'cantidad':1,
                'stock': producto.stock,
            }
            
        else:
            for key, value in self.kart.items():
                if key == str(producto.id):
                    value['cantidad'] += 1
                    value['precio'] = float(value['precio']) + producto.precio
                    break
        
        self.save_kart()
        
        
    def save_kart(self):
        self.session['kart'] = self.kart
        self.session.modified = True
        
    
    def delete_prod(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.kart:
            del self.kart[producto.id]
            self.save_kart()
            
    
    def remove_prod(self, producto):
        for key, value in self.kart.items():
            if key == str(producto.id):
                value['cantidad'] -= 1
                value['precio'] = float(value['precio']) - producto.precio
                if value['cantidad'] < 1:
                    self.delete_prod(producto)
                break
        self.save_kart()
        
        
    def empty_kart(self):
        self.session['kart'] = {}
        self.session.modified = True