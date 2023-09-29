from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color

class BannerVenda(GridLayout):

    def __init__(self, **kwargs):
        self.rows=1
        super().__init__()
        
        # kwargs = {"cliente": "Carrefour", "data": "26/09/2023", "foto_cliente": "carrefour.png", "foto_produto": "feijao.png",}

        with self.canvas:
            Color(rgb=(0, 0, 0, 1))
            self.rec = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.atualizar_rec, size=self.atualizar_rec)

        cliente = kwargs["cliente"]
        data = kwargs["data"]
        foto_cliente = kwargs["foto_cliente"]
        foto_produto = kwargs["foto_produto"]
        preco = float(kwargs["preco"])
        produto = kwargs["produto"]
        quantidade = float(kwargs["quantidade"])
        unidade = kwargs["unidade"]
        
        esquerda = FloatLayout()
        esquerda_imagem = Image(pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.75), 
                                source=f"icones/fotos_clientes/{foto_cliente}")
        esquerda_label = Label(pos_hint={"right": 1, "top": 0.2}, size_hint=(1, 0.2), text=cliente)
        esquerda.add_widget(esquerda_imagem)
        esquerda.add_widget(esquerda_label)

        meio = FloatLayout()
        meio_imagem = Image(pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.75), 
                                source=f"icones/fotos_produtos/{foto_produto}")
        meio_label = Label(pos_hint={"right": 1, "top": 0.2}, size_hint=(1, 0.2), text=produto)
        meio.add_widget(meio_imagem)
        meio.add_widget(meio_label)

        direita = FloatLayout()
        direita_label_data = Label(text = f"Data: {data}", pos_hint={"right": 1, "top": 0.9}, size_hint=(1, 0.33))
        direita_label_preco = Label(text = f"Preco: R${preco:,.2f}", pos_hint={"right": 1, "top": 0.65}, size_hint=(1, 0.33))
        direita_label_quantidade = Label(text = f"Quantidade: {quantidade} unidades", pos_hint={"right": 1, "top": 0.4}, size_hint=(1, 0.33))
        direita.add_widget(direita_label_data)
        direita.add_widget(direita_label_preco)
        direita.add_widget(direita_label_quantidade)

        self.add_widget(esquerda)
        self.add_widget(meio)
        self.add_widget(direita)

    def atualizar_rec(self, *args):
        self.rec.pos = self.pos
        self.rec.size = self.size